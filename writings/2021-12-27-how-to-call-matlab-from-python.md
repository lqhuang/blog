---
title: 'How to call MATLAB from Python'
created: 2021-12-27
updated: 2022-01-03
tags:
  - 'matlab'
  - 'python'
  - 'tutorial'
---

When you want to reuse MATLAB without rerwrite everythings to Python, you're able to call MATLAB functions or scripts directly from Python. That's true!

How? It's like a client/service arch application. Generally, You need to start a MATLAB process as server, and then connect this server as a client session from Python. After session connected, you can run different MATLAB functions which already wrapped as Python functions from official provided Python package to fetch result. Actual calculation is executed under MATLAB process.

Even more, there is also another solution that is creating an individual Python package using MATLAB library compiler. It makes you're able to invoke MATLAB functions like using a Python package **without installation of MATLAB**. But it's not the content this article what to talk about. If you're interested packing method, check [Python Package Integration](https://www.mathworks.com/help/compiler_sdk/python_packages.html) for more information.

## MATLAB cli args

Useful flag for `matlab` command:

```console
    -nodisplay              - Do not display any X commands. The MATLAB
                              desktop will not be started. However, unless
                              -nojvm is also provided the Java virtual machine
                              will be started.
    -nosplash               - Do not display the splash screen during startup.
    -nodesktop              - Do not start the MATLAB desktop. Use the current
                              terminal for commands. The Java virtual machine
                              will be started.
    -nojvm                  - Shut off all Java support by not starting the
                              Java virtual machine. In particular the MATLAB
                              desktop will not be started.
    -batch MATLAB_command   - Start MATLAB and execute the MATLAB command(s) with no desktop
                              and certain interactive capabilities disabled. Terminates
                              upon successful completion of the command and returns exit
                              code 0. Upon failure, MATLAB terminates with a non-zero exit.
                              Cannot be combined with -r.
    -r MATLAB_command       - Start MATLAB and execute the MATLAB_command.
                              Cannot be combined with -batch.
    -sd folder              - Set the MATLAB startup folder to folder, specified as a string.
                              Cannot be combined with -useStartupFolderPref.
    -logfile log            - Make a copy of any output to the command window
                              in file log. This includes all crash reports.
```

## Supports and Limitations

MATLAB Engine API for Python is supported from MATLAB R2014b or later. You need to have a supported version of the reference Python implementation (also known as CPython) installed on your system. And they must be compatible for each other, for more information, see [Versions of Python Compatible with MATLAB Products by Release](https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/support/sysreq/files/python-compatibility.pdf).

The MATLAB® Engine API does not support these features:

- The engine cannot start or connect to MATLAB on a remote machine.
- Python® keyword arguments cannot be input arguments to MATLAB functions called with the engine. The engine passes only positional arguments to MATLAB functions.
- The size of data arrays passed between Python and MATLAB is limited to 2 GB. This limit applies to the data plus supporting information passed between the processes.
- A recursive data structure cannot be passed as an input argument to a MATLAB function, or put into an engine workspace. (A recursive data structure is a Python data structure that includes itself as a value.)

The MATLAB Engine API does not support these Python types.

- `array.array` (use MATLAB numeric array objects instead; see [MATLAB Arrays as Python Variables](https://www.mathworks.com/help/matlab/matlab_external/matlab-arrays-as-python-variables.html))
- `None`
- `module.type` object

## Install Python Interface for MATLAB Engine

> To start the MATLAB® engine within a Python® session, you first must install the engine API as a Python package. MATLAB provides a standard Python `setup.py` file for building and installing the engine using the `distutils` module. You can use the same `setup.py` commands to build and install the engine on Windows®, Mac, or Linux® systems.

Switch to your Python environment

```shell
cd "matlabroot/extern/engines/python"
python setup.py install
```

Here `matlabroot` is where you installed MATLAB.

If you succeed, that's all, then you can call MATLAB from Python :)

## Start and Stop MATLAB Engine for Python

There are two ways to create a MATLAB engine.

First, created directly from Python by calling `start_matlab`. [^start_matlab]

```python
import matlab.engine
eng = matlab.engine.start_matlab()
```

The `start_matlab` function returns a Python object, `eng`, which enables you to pass data and call functions executed by MATLAB. Create multiple engines is available. Also, you could start the engine and pass the options as an input argument string to `matlab.engine.start_matlab`. For example, start MATLAB without jvm and set the numeric display format to short.

```python
eng = matlab.engine.start_matlab("-nojvm -r 'format short'")
# check whether MATLAB session is still alive
# print(eng._check_matlab())
# True
```

Call `eng.quit()` to stop engine. If you exit Python with an engine still running, then Python automatically stops the engine and its MATLAB process.

Second, create from MATLAB itself. [^connect]

> You can connect the MATLAB® Engine for Python® to a shared MATLAB session that is already running on your local machine. You also can connect to multiple shared MATLAB sessions from a single Python session. You can share a MATLAB session at any time during the session, or at start with a startup option.

Convert your MATLAB session to a shared session, just from MATLAB call `matlab.engine.shareEngine`.

Example for open MATLAB session

```matlab
matlab.engine.shareEngine
% or add a name for engine
% matlab.engine.shareEngine("my-engine")
```

Example for running in cli

```shell
matlab -nodisplay -nojvm -nosplash -r "matlab.engine.shareEngine"
# matlab -nodisplay -nojvm -nosplash -r "matlab.engine.shareEngine('my-engine')"
```

Now, you can connect MATLAB shared session to get a engine from Python

```python
import matlab.engine
eng = matlab.engine.connect_matlab()
# You can connect to a shared session by name. To find the name of a shared session, call `matlab.engine.find_matlab` from Python.
print(matlab.engine.find_matlab())
# ('MATLAB_13232', 'your-engine-custom-name')
# Here the default name MATLAB_13232 where 13232 is the ID of the MATLAB process.
# If you do not specify the name of a shared session, `matlab.engine.connect_matlab` connects to the first session named in the tuple returned by `matlab.engine.find_matlab`.
```

## Run MATLAB functions/scripts

Ok, here is the exact part of how to run MATLAB functions or script inside Python.

### Call MATLAB Functions from Python

Generally, you just need to call the specific function name which is in searchable namespace of running MATLAB process.

Content from <https://www.mathworks.com/help/matlab/matlab_external/call-matlab-functions-from-python.html>:

> ### Return Output Argument from MATLAB Function
>
> You can call any MATLAB® function directly and return the results to Python®. For example, to determine if a number is prime, use the engine to call the `isprime` function.
>
> ```python
> import matlab.engine
> eng = matlab.engine.start_matlab()
> tf = eng.isprime(37)
> print(tf)
> # True
> ```
>
> ### Return Multiple Output Arguments from MATLAB Function
>
> When you call a function with the engine, by default the engine returns a single output argument. If you know that the function can return multiple arguments, use the `nargout` argument to specify the number of output arguments.
>
> To determine the greatest common denominator of two numbers, use the `gcd` function. Set `nargout` to return the three output arguments from `gcd`.
>
> ```python
> import matlab.engine
> eng = matlab.engine.start_matlab()
> t = eng.gcd(100.0, 80.0, nargout=3)
> print(t)
> # (20.0, 1.0, -1.0)
> ```
>
> ### Return No Output Arguments from MATLAB Function
>
> Some MATLAB functions return no output arguments. If the function returns no arguments, set `nargout` to 0.
>
> Open the MATLAB Help browser from Python.
>
> ```python
> import matlab.engine
> eng = matlab.engine.start_matlab()
> eng.doc(nargout=0)
> ```
>
> The MATLAB `doc` function opens the browser, but does not return output arguments. If you do not specify `nargout=0`, the engine raises an error.
>
> ### Stop Execution of Function
>
> To stop execution of a MATLAB function press `Ctrl+C`. Control returns to Python.
>
> ### Use Function Names for MATLAB Operators
>
> You can use a MATLAB operator in Python by calling the equivalent function. For a list of operators and associated function names, see [MATLAB Operators and Associated Functions](https://www.mathworks.com/help/matlab/matlab_oop/implementing-operators-for-your-class.html#br02znk-6). For example, to add two numbers, use the `plus` function instead of the `+` operator.
>
> ```python
> import matlab.engine
> eng = matlab.engine.start_matlab()
> a = 2
> b = 3
> eng.plus(a, b)
> ```

### Call User Scripts and Functions from Python

The same, run findable functions or scripts in MATLAB workspace. [This example shows how to call a MATLAB® script to compute the area of a triangle from Python®.](https://www.mathworks.com/help/matlab/matlab_external/call-user-script-and-function-from-python.html):

> In your current folder, create a MATLAB script in a file named `triarea.m`.
>
> ```matlab
> b = 5;
> h = 3;
> a = 0.5*(b.* h)
> ```
>
> After you save the file, start Python and call the script.
>
> ```python
> import matlab.engine
> eng = matlab.engine.start_matlab()
> eng.triarea(nargout=0)
> # a =
> #
> #     7.5000
> ```
>
> Specify `nargout=0`. Although the script prints output, it returns no output arguments to Python.
>
> Convert the script to a function and call the function from the engine. To edit the file, open the MATLAB editor.
>
> `eng.edit('triarea',nargout=0)`
>
> Delete the three statements. Then add a function declaration and save the file.
>
> ```matlab
> function a = triarea(b,h)
> a = 0.5*(b.* h);
> ```
>
> Call the new triarea function from the engine.
>
> ```python
> ret = eng.triarea(1.0,5.0)
> print(ret)
> # 2.5
> ```
>
> The triarea function returns only one output argument, so there is no need to specify nargout.

### Call MATLAB Functions Asynchronously from Python

[This example shows how to call the MATLAB sqrt function asynchronously from Python and retrieve the square root later.](https://www.mathworks.com/help/matlab/matlab_external/call-matlab-functions-asynchronously-from-python.html):

> The engine calls MATLAB functions synchronously by default. Control returns to Python only when the MATLAB function finishes. But the engine also can call functions asynchronously. Control immediately returns to Python while MATLAB is still executing the function. The engine stores the result in a Python variable that can be inspected after the function finishes.
>
> Use the background argument to call a MATLAB function asynchronously.
>
> ```python
> import matlab.engine
> eng = matlab.engine.start_matlab()
> future = eng.sqrt(4.0, background=True)
> ret = future.result()
> print(ret)
> # 2.0
> ```
>
> Use the done method to check if an asynchronous call finished.
>
> ```python
> tf = future.done()
> print(tf)
> # True
> ```
>
> To stop execution of the function before it finishes, call `future.cancel()`.

### Bonus: Get Help for MATLAB Functions from Python [^get-mat-func]

If you don't know the detail input arguments of MATLAB functions, you also can get help documents in python.

It's simple, and the totally the same in MATLAB. To display help text for a function at the Python prompt, call the MATLAB `help` function. For example, display the help text for `erf`.

```python
import matlab.engine
eng = matlab.engine.start_matlab()
eng.help("erf", nargout=0)
# ERF Error function.
#     Y = ERF(X) is the error function for each element of X.  X must be
#     real. The error function is defined as:

#       erf(x) = 2/sqrt(pi) * integral from 0 to x of exp(-t^2) dt.

#     See also ERFC, ERFCX, ERFINV, ERFCINV.

#     Other functions named erf:
#       codistributed/erf
#       gpuArray/erf
#       sym/erf

#     Reference page in Help browser
#       doc erf
```

## Construction of Data Types

Basic scalar types (int, float, string, bool, ...) are simply automatic. MATLAB and Python will convert the data into equivalent data types followed given rules. You can check detailed mapping tables [Pass Data to MATLAB from Python](https://www.mathworks.com/help/matlab/matlab_external/pass-data-to-matlab-from-python.html) and [Handle Data Returned from MATLAB to Python](https://www.mathworks.com/help/matlab/matlab_external/handle-data-returned-from-matlab-to-python.html) for these basic scalar types.

But if you want to manipulate arrays or matrix between MATLAB and Python, you need to construct these data types by yourself [^matarr2pyvar].

> You can create MATLAB numeric arrays in a Python session by calling constructors from the matlab Python package (for example, `matlab.double`, `matlab.int32`). The name of the constructor indicates the MATLAB numeric type.
>
> You can use custom types for initializing MATLAB double arrays in Python. The custom type should inherit from the Python Abstract Base Class `collections.Sequence` to be used as an initializer.
>
> You can pass MATLAB arrays as input arguments to functions called with the MATLAB Engine API for Python. When a MATLAB function returns a numeric array as an output argument, the engine returns the array to Python.

The following example shows signatures of array construction functions:

```python
matlab.double(initializer=None, size=None, is_complex=False)
matlab.int64(initializer=None, size=None, is_complex=False)
```

The optional `size` input argument sets the array size from a sequence. You can create multidimensional arrays by specifying `initializer` to contain multiple sequences of numbers, or by specifying `size` to be multidimensional.

All MATLAB arrays created with matlab package constructors have the attributes and methods listed in this table.

| Attribute or Method | Purpose                                     |
| ------------------- | ------------------------------------------- |
| size                | Size of array returned as a tuple           |
| reshape(size)       | Reshape array as specified by sequence size |

For example, create an array with N elements (**the size is 1-by-N because it is a MATLAB array**). Indexing and slicing are almost the same with Python's rule.

```python
import matlab.engine
A = matlab.int8([1,2,3,4,5])
print(A.size)
# (1, 5)
print(A[0])
# [1,2,3,4,5]
print(A[0][2])
# 3
print(A[0][1:4])
# [2,3,4]
```

> [!NOTE]
>
> Slicing MATLAB arrays behaves differently from slicing a Python `list`. Slicing a MATLAB array returns a view instead of a shallow copy.
>
> Given a MATLAB array and a Python list with the same values, assigning a slice results in different results as shown by the following code.
>
> ```python
> A = matlab.int32([[1,2],[3,4],[5,6]])
> L = [[1,2],[3,4],[5,6]]
> A[0] = A[0][::-1]
> L[0] = L[0][::-1]
> print(A)
> # [[2,2],[3,4],[5,6]]
> print(L)
> # [[2, 1], [3, 4], [5, 6]]
> ```

Create multidimensional MATLAB arrays of any numeric type.

```python
import matlab.engine
A = matlab.double([[1,2,3,4,5], [6,7,8,9,10]])
print(A)
# [[1.0,2.0,3.0,4.0,5.0],[6.0,7.0,8.0,9.0,10.0]]
print(A.size)
# (2, 5)
```

The size attribute of A shows that it is a 2-by-5 array.

You can assign data from a slice, from another MATLAB array, or from any Python iterable that contains numbers. This code shows assignment from a Python list to a slice of an array.

```python
A = matlab.double([[1,2,3,4],[5,6,7,8]])
A[0] = [10,20,30,40]
print(A)
# [[10.0,20.0,30.0,40.0],[5.0,6.0,7.0,8.0]]

A = matlab.int8([1,2,3,4,5,6,7,8])
A[0][2:4] = [30,40]
A[0][6:8] = [70,80]
print(A)
# [[1,2,30,40,5,6,70,80]]
```

Besides, simple array data (aka sequence data) is also native supported without explicit conversion. This example [^matarr-in-py] shows passing a list array as the input argument to the MATLAB `sqrt` function.

```python
import matlab.engine
eng = matlab.engine.start_matlab()
a = matlab.double([1, 4, 9, 16, 25])
b = eng.sqrt(a)
print(b)
# [[1.0,2.0,3.0,4.0,5.0]]
```

Like this example, you can create arrays of any MATLAB numeric or logical type from Python sequence types without manual construction MATLAB defined types. But please notice that the engine returns `b`, which is a 1-by-5 `matlab.double` array. It's actually a 2-D matrix, could only be selected element by `b[i][j]` or selected row by `b[i]`.

Iterator for MATLAB matrix is available. The magic function returns a 2-D `matlab.double` array to Python. Use a for loop to print each row on a separate line.

```python
a = eng.magic(6)
for x in a: print(x)
# [35.0,1.0,6.0,26.0,19.0,24.0]
# [3.0,32.0,7.0,21.0,23.0,25.0]
# [31.0,9.0,2.0,22.0,27.0,20.0]
# [8.0,28.0,33.0,17.0,10.0,15.0]
# [30.0,5.0,34.0,12.0,14.0,16.0]
# [4.0,36.0,29.0,13.0,18.0,11.0]
```

## References

- [Calling MATLAB from Python](https://www.mathworks.com/help/matlab/matlab-engine-for-python.html)
- [Python Package Integration](https://www.mathworks.com/help/compiler_sdk/python_packages.html)
- [Cheat Sheets for Using MATLAB with Python](https://www.mathworks.com/campaigns/offers/matlab-python-cheat-sheets.html)
- [Install MATLAB Engine API for Python](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)
- [Call User Scripts and Functions from Python](https://www.mathworks.com/help/matlab/matlab_external/call-user-script-and-function-from-python.html)

[^start_matlab]: [Start and Stop MATLAB Engine for Python](https://www.mathworks.com/help/matlab/matlab_external/start-the-matlab-engine-for-python.html)
[^connect]: [Connect Python to Running MATLAB Session](https://www.mathworks.com/help/matlab/matlab_external/connect-python-to-running-matlab-session.html)
[^get-mat-func]: [Get Help for MATLAB Functions from Python](https://www.mathworks.com/help/matlab/matlab_external/get-help-for-matlab-functions-from-python.html)
[^matarr2pyvar]: [MATLAB Arrays as Python Variables](https://www.mathworks.com/help/matlab/matlab_external/matlab-arrays-as-python-variables.html)
[^matarr-in-py]: [Use MATLAB Arrays in Python](https://www.mathworks.com/help/matlab/matlab_external/use-matlab-arrays-in-python.html)
