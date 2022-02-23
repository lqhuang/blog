＃Apache Spark的结构化流中的事件时间聚合和水印

可伸缩数据@ Databricks的第4部分

连续应用程序通常需要基于实时汇总统计信息的近乎实时的决策-例如IoT设备的运行状况和读数，或者检测异常行为。 在此博客中，我们将探讨如何轻松地在结构化流中表达流聚合，以及如何自然地处理迟到和乱序的数据。

##流式聚合

结构化流允许用户表达与批处理查询相同的流查询，Spark SQL引擎增量化查询并在流数据上执行。 例如，假设您有一个流式DataFrame，其中包含具有来自IoT设备的信号强度的事件的事件，并且您想要计算每个设备的运行平均信号强度，则可以编写以下Python代码：

```python
# DataFrame w/ schema [eventTime: timestamp, deviceId: string, signal: bigint]
eventsDF = ...

avgSignalDF = eventsDF.groupBy("deviceId").avg("signal")
```

如果eventsDF是静态数据上的DataFrame，则此代码没有什么不同。但是，在这种情况下，平均值将随着新事件的到来而不断更新。您可以选择不同的输出模式，以将更新的平均值写入外部系统（例如文件系统和数据库）。此外，您还可以使用Spark的用户定义的汇总功能（UDAF）实施自定义汇总。

Windows上事件时间的##聚合

在许多情况下，您不希望对整个流运行聚合，而是希望对时间窗口存储的数据进行聚合（例如，每5分钟或每小时）。在我们之前的示例中，如果设备开始出现异常情况，那么看看最近5分钟的平均信号强度是很有启发性的。同样，此5分钟的窗口应基于数据中嵌入的时间戳（即事件时间），而不是基于处理时间（即处理时间）。

较早的Spark Streaming DStream API使得很难表达这样的事件时间窗口，因为该API仅用于处理时间窗口（即，数据到达Spark时的时间窗口）。在结构化流中，在事件时间表达这样的窗口只是使用“ window（）”函数执行特殊的分组。例如，事件中eventTime列上超过5分钟的滚动（不重叠）窗口的计数如下。

```python
from pyspark.sql.functions import *

windowedAvgSignalDF = \
  eventsDF \
    .groupBy(window("eventTime", "5 minute")) \
    .count()
```

在上面的查询中，每条记录都将被分配到一个5分钟的滚动窗口，如下所示。

![mapping-of-event-time-to-5-min-tumbling-windows](./mapping-of-event-time-to-5-min-tumbling-windows.png)

每个窗口都是计算运行计数的组。 您还可以通过指定窗口长度和滑动间隔来定义重叠窗口。 例如：

```python
from pyspark.sql.functions import *

windowedAvgSignalDF = \
  eventsDF \
    .groupBy(window("eventTime", "10 minutes", "5 minutes")) \
    .count()
```

在上面的查询中，每个记录将分配给多个重叠的窗口，如下所示。

！[将时间映射到重叠窗口的长度为10分钟和滑动间隔为5分钟]（将事件映射到重叠窗口的时间 长10分钟和滑动间隔5分钟.png）

这种分组策略会自动处理延迟和乱序的数据-延迟事件只会更新较旧的窗口组，而不是最新的窗口组。 这是一个由“ deviceId”和重叠窗口分组的查询的端到端图示。 下图显示了在通过deviceId和滑动窗口进行分组时，用5分钟的触发器处理新数据后，查询的最终结果将如何变化（为简便起见，省略了“信号”字段）。

```python
windowedCountsDF = \
  eventsDF \
    .groupBy(
      "deviceId",
      window("eventTime", "10 minutes", "5 minutes")) \
    .count()
```

![late-data-handling-in-windowed-grouped-aggregation](./late-data-handling-in-windowed-grouped-aggregation.png)

请注意，最新的乱序记录[12:04，dev2]如何更新旧窗口的计数。

##有状态的增量执行

在执行任何流聚合查询时，Spark SQL引擎会在内部将中间聚合保持为容错状态。此状态被构造为键值对，其中键是组，值是中间聚合。这些对存储在Spark执行程序中的内存中，版本控制的键值“状态存储”中，该状态通过使用与HDFS兼容的文件系统（在配置的检查点位置）中的预写日志进行检查点。在每次触发时，都会在状态存储中读取并更新状态，并将所有更新保存到预写日志中。万一发生任何故障，将从检查点信息中还原状态的正确版本，并且从故障点开始进行查询。结合可重播的源和幂等的接收器，结构化流确保对状态流的处理一次保证。

![fault-tolerant-exactly-once-stateful-stream-processing-in-structured-streaming](./fault-tolerant-exactly-once-stateful-stream-processing-in-structured-streaming.png)

这种容错状态管理自然会招致一些处理开销。为了将这些开销限制在可接受的范围内，状态数据的大小不应无限期增长。但是，使用滑动窗口时，窗口/组的数量将无限期增加，状态的大小（与组的数量成正比）也会无限增加。为了限制状态大小，我们必须能够丢弃不再更新的旧聚合，例如7天的平均值。我们使用**水印**实现此目的。

##水印处理后期数据时限制状态

如前所述，迟到数据的到来可能会导致旧窗口的更新。这使定义哪些旧聚合将不被更新的过程变得复杂，因此可以将其从状态存储中删除以限制状态大小。在Apache Spark 2.1中，我们引入了“水印”功能，该功能可以自动删除旧状态数据。

水印是事件时间中的移动阈值，它落后于查询在已处理数据中看到的最大事件时间。尾随间隙定义了我们将等待多久的数据到达。通过知道给定组不再有数据到达的时间点，我们可以限制查询需要维护的状态总量。例如，假设配置的最大延迟为10分钟。这意味着最多延迟10分钟的事件将被允许汇总。如果观察到的最大事件时间是12:33，那么所有事件时间早于12:23的将来事件都将被视为“太迟”并丢弃。此外，将清除所有早于12:23的窗口的状态。您可以根据应用程序的要求设置此参数-此参数的较大值允许数据稍后到达，但以增加状态大小为代价，即内存使用情况，反之亦然。

这是前面的示例，但带有水印。

```python
windowedCountsDF = \
  eventsDF \
    .withWatermark("eventTime", "10 minutes") \
    .groupBy(
      "deviceId",
      window("eventTime", "10 minutes", "5 minutes")) \
    .count()
```

执行此查询时，Spark SQL将自动跟踪eventTime列的最大观察值，更新水印并清除旧状态。 如下所示。

![watermarking-in-windowed-grouped-aggregation.png](./watermarking-in-windowed-grouped-aggregation.png)

请注意在处理时间12:20和12:25之间到达的两个事件。水印用于区分晚期事件和“太迟”事件，并相应地对其进行处理。

##结论

简而言之，我介绍了结构化流的窗口化策略来处理关键的流聚合：事件时间以及延迟和无序数据的窗口。使用这种加窗策略，结构化流引擎可以实现水印处理，其中可以丢弃较晚的数据。这种设计的结果是，我们可以管理状态存储的大小。

在即将发布的Apache Spark 2.2版本中，我们向流数据帧/数据集添加了更多高级状态流处理操作。请继续关注此博客系列，以获取更多信息。如果您想了解有关结构化流的更多信息，请阅读本系列以前的文章。

-Apache Spark中的结构化流
-Apache Spark 2.1中具有结构化流的实时流ETL
-在Apache Spark 2.1中使用结构化流处理复杂的数据格式
-在Apache Spark 2.2中使用结构化流处理Apache Kafka中的数据
