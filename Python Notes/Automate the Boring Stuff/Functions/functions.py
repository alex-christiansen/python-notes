All Python programs can call a basic set of functions called built-in functions, including the print(), input(), and len() functions you’ve seen before. Python also comes with a set of modules called the standard library. Each module is a Python program that contains a related group of functions that can be embedded in your programs. For example, the math module has mathematics-related functions, the random module has random number–related functions, and so on.
Before you can use the functions in a module, you must import the module with an import statement. In code, an import statement consists of the following:

* The import keyword
* The name of the module
* Optionally, more module names, as long as they are separated by commas

An alternative form of the import statement is composed of the from keyword, followed by the module name, the import keyword, and a star; for example, from random import *.
With this form of import statement, calls to functions in random will not need the random. prefix. However, using the full name makes for more readable code, so it is better to use the normal form of the import statement.

Beyond the standard library of modules packaged with Python, other developers have written their own modules to extend Python’s capabilities even further. The primary way to install third-party modules is to use Python’s pip tool. This tool securely downloads and installs Python modules onto your computer from https://pypi.python.org/, the website of the Python Software Foundation. PyPI, or the Python Package Index, is a sort of free app store for Python modules.

## The pip Tool
The executable file for the pip tool is called pip on Windows and pip3 on OS X and Linux. On Windows, you can find pip at C:\Python34\Scripts\pip.exe. On OS X, it is in /Library/Frameworks/Python.framework/Versions/3.4/bin/pip3. On Linux, it is in /usr/bin/pip3.
While pip comes automatically installed with Python 3.4 on Windows and OS X, you must install it separately on Linux. To install pip3 on Ubuntu or Debian Linux, open a new Terminal window and enter sudo apt-get install python3-pip. To install pip3 on Fedora Linux, enter sudo yum install python3-pip into a Terminal window. You will need to enter the administrator password for your computer in order to install this software.

## Installing Third-Party Modules
The pip tool is meant to be run from the command line: You pass it the command install followed by the name of the module you want to install. For example, on Windows you would enter pip install ModuleName, where ModuleName is the name of the module. On OS X and Linux, you’ll have to run pip3 with the sudo prefix to grant administrative privileges to install the module. You would need to type sudo pip3 install ModuleName.
If you already have the module installed but would like to upgrade it to the latest version available on PyPI, run pip install –U ModuleName (or pip3 install –U ModuleName on OS X and Linux).
After installing the module, you can test that it installed successfully by running import ModuleName in the interactive shell. If no error messages are displayed, you can assume the module was installed successfully.

## Creating Functions
To better understand how functions work, let’s create one. Type this program into the file editor and save it as helloFunc.py:

❶ def hello():
❷     print('Howdy!')
       print('Howdy!!!')
       print('Hello there.')
❸ hello()
   hello()
   hello()
The first line is a def statement ❶, which defines a function named hello(). The code in the block that follows the def statement ❷ is the body of the function. This code is executed when the function is called, not when the function is first defined.

The hello() lines after the function ❸ are function calls. In code, a function call is just the function’s name followed by parentheses, possibly with some number of arguments in between the parentheses. When the program execution reaches these calls, it will jump to the top line in the function and begin executing the code there. When it reaches the end of the function, the execution returns to the line that called the function and continues moving through the code as before.

## def Statements with Parameters

When you call the print() or len() function, you pass in values, called arguments in this context, by typing them between the parentheses. You can also define your own functions that accept arguments. Type this example into the file editor and save it as helloFunc2.py:

❶ def hello(name):
❷     print('Hello ' + name)

❸ hello('Alice')
  hello('Bob')
When you run this program, the output looks like this:


Hello Alice
Hello Bob

The definition of the hello() function in this program has a parameter called name ❶. A parameter is a variable that an argument is stored in when a function is called. The first time the hello() function is called, it’s with the argument 'Alice' ❸. The program execution enters the function, and the variable name is automatically set to 'Alice', which is what gets printed by the print() statement ❷.

One special thing to note about parameters is that the value stored in a parameter is forgotten when the function returns. For example, if you added print(name) after hello('Bob') in the previous program, the program would give you a NameError because there is no variable named name. This variable was destroyed after the function call hello('Bob') had returned, so print(name) would refer to a name variable that does not exist.

## Return Values and return Statements
When you call the len() function and pass it an argument such as 'Hello', the function call evaluates to the integer value 5, which is the length of the string you passed it. In general, the value that a function call evaluates to is called the return value of the function.

When creating a function using the def statement, you can specify what the return value should be with a return statement. A return statement consists of the following:

The return keyword

The value or expression that the function should return

When an expression is used with a return statement, the return value is what this expression evaluates to. For example, the following program defines a function that returns a different string depending on what number it is passed as an argument. Type this code into the file editor and save it as magic8Ball.py:


❶ import random
❷ def getAnswer(answerNumber):
❸     if answerNumber == 1:
           return 'It is certain'
       elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'

❹ r = random.randint(1, 9)
❺ fortune = getAnswer(r)
❻ print(fortune)
When this program starts, Python first imports the random module ❶. Then the getAnswer() function is defined ❷. Because the function is being defined (and not called), the execution skips over the code in it. Next, the random.randint() function is called with two arguments, 1 and 9 ❹. It evaluates to a random integer between 1 and 9 (including 1 and 9 themselves), and this value is stored in a variable named r.

The getAnswer() function is called with r as the argument ❺. The program execution moves to the top of the getAnswer() function ❸, and the value r is stored in a parameter named answerNumber. Then, depending on this value in answerNumber, the function returns one of many possible string values. The program execution returns to the line at the bottom of the program that originally called getAnswer() ❺. The returned string is assigned to a variable named fortune, which then gets passed to a print() call ❻ and is printed to the screen.

## The None Value
In Python there is a value called None, which represents the absence of a value. None is the only value of the NoneType data type. (Other programming languages might call this value null, nil, or undefined.) Just like the Boolean True and False values, None must be typed with a capital N.

Behind the scenes, Python adds return None to the end of any function definition with no return statement. This is similar to how a while or for loop implicitly ends with a continue statement. Also, if you use a return statement without a value (that is, just the return keyword by itself), then None is returned.

## Keyword Arguments and print()
Most arguments are identified by their position in the function call. For example, random.randint(1, 10) is different from random.randint(10, 1). The function call random.randint(1, 10) will return a random integer between 1 and 10, because the first argument is the low end of the range and the second argument is the high end (while random.randint(10, 1) causes an error).

However, keyword arguments are identified by the keyword put before them in the function call. Keyword arguments are often used for optional parameters. For example, the print() function has the optional parameters end and sep to specify what should be printed at the end of its arguments and between its arguments (separating them), respectively.

Parameters and variables that are assigned in a called function are said to exist in that function’s local scope. Variables that are assigned outside all functions are said to exist in the global scope. A variable that exists in a local scope is called a local variable, while a variable that exists in the global scope is called a global variable. A variable must be one or the other; it cannot be both local and global.

## Key Things
1. Local Variables Cannot Be Used in the Global Scope
2. Local Scopes Cannot Use Variables in Other Local Scopes
3. Global Variables Can Be Read from a Local Scope
4. Local and Global Variables with the Same Name

## The global Statement
If you need to modify a global variable from within a function, use the global statement. If you have a line such as global eggs at the top of a function, it tells Python, “In this function, eggs refers to the global variable, so don’t create a local variable with this name.”

There are four rules to tell whether a variable is in a local scope or global scope:

If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.

If there is a global statement for that variable in a function, it is a global variable.

Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.

But if the variable is not used in an assignment statement, it is a global variable.

