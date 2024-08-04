# CS50's Introduction to Programming with Python

Official course link: https://cs50.harvard.edu/python/2022/   
CS50p YouTube playlist: https://www.youtube.com/watch?v=OvKCESUCWII&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&pp=iAQB   
Python documentations: https://docs.python.org/3/   
Python Package Index documentation: https://pypi.org/   
Personal CS50p ChatGPT: https://chat.openai.com/c/68fb62eb-bddc-47ee-b7b8-cf9f0a7f0cc8   


# Lectures

## [Lecture 0: Functions, Variables](https://cs50.harvard.edu/python/2022/weeks/0/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/0/)
- [First Program](https://cs50.harvard.edu/python/2022/notes/0/#creating-code-with-python): *code prog_name.py* to create an empty python program -> *python prog_name.py* to run the program.
- [Functions](https://cs50.harvard.edu/python/2022/notes/0/#functions): are known actions that have side effects and can take arguments. Functions are used to modularize code (even within libraries). From the function's perspective the input variables are called *parameters*, but from the program's perspective that calls the function the input variables are called *arguments*. Positional parameters must be passed in the same order as they appear in the function signature, whereas named parameters can be passed in any order (defined by their specified name!). The position is not relevant for named parameters, but after them no positional parameter can be passed. Used functions: *print()*, *input()* (ALWAYS sanitize user input properly!). Functions can be called right after each other: *name = name.strip().title()*.
- [Bugs](https://cs50.harvard.edu/python/2022/notes/0/#bugs): are mistakes identified by the compiler with a cryptic, but useful message. Solve them to make a working or better program.
- [Variables](https://cs50.harvard.edu/python/2022/notes/0/#variables): are containers for values. Used data types: *int*, *float*, *str*. Used *str* methods: *isalpha()*, *strip()*, *title()*, *split()*. Used numeric methods: *int()*, *float()* type converters, *round()*.
- [Comments](https://cs50.harvard.edu/python/2022/notes/0/#comments): are notes for programmers (ignored by interpreter). Single-line comments are created using the "#" symbol. Multi-line strings are enclosed in triple quotes (""" ... """ or ''' ... '''). Docstrings are strings used to document modules, classes, functions, and methods. They are written as the first statement in the function, method, class, or module definition and are enclosed in triple quotes. Docstrings can be accessed programmatically via the __doc__ attribute and are a key part of Python's documentation system.
- [Escape Character](https://cs50.harvard.edu/python/2022/notes/0/#a-small-problem-with-quotation-marks): "\\" (*backslash*) used for special characters.
- [Formatting Strings](https://cs50.harvard.edu/python/2022/notes/0/#formatting-strings): *print(f"hello, {name}")* where *f* is a special indicator for Python to treat this string a special way. *{name}* is a variable in this case. See documentation for mini language!
- [Formatting Numbers](https://cs50.harvard.edu/python/2022/notes/0/#float-basics): separator for groups of three digits, starting from the decimal point and moving left: *print(f"{x:,}")*. Show decimals (2): *print(f"{x:.2f}")*. Show max (10) decimals, but exclude unnecessary "0": *print(f"{x:.10g}")*.
- [User Functions](https://cs50.harvard.edu/python/2022/notes/0/#def): created with *def* keyword and indentation to understand what is part of the function. To add default values to function parameters assign them in function declaration. A *main()* function is recommended to be created and called in a python program. A function can return one variable. This “passing back” value is called a *return* value.
- [Interactive mode](https://cs50.harvard.edu/python/2022/notes/0/#integers-or-int) is a feature of Python where code can be executed interactively in terminal. Enter *python* in terminal and ">>>" will appear for this feature. To exit use *exit()*.

### [Problem Set 0](https://cs50.harvard.edu/python/2022/psets/0/)
- [Indoor Voice](https://cs50.harvard.edu/python/2022/psets/0/indoor/): a python program that converts user input into lowercase.
- [Playback Speed](https://cs50.harvard.edu/python/2022/psets/0/playback/): a python program that outputs the same input, replacing each space with "...".
- [Making Faces](https://cs50.harvard.edu/python/2022/psets/0/faces/): a python program that changes ":)" to 🙂 and ":(" to 🙁.
- [Einstein](https://cs50.harvard.edu/python/2022/psets/0/einstein/): a python program that determines energy based on mass.
- [Tip Calculator](https://cs50.harvard.edu/python/2022/psets/0/tip/): a python program that calculates tips depending on dollar amounts and percentages.


## [Lecture 1: Conditionals](https://cs50.harvard.edu/python/2022/weeks/1/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/1/)
- [Conditionals](https://cs50.harvard.edu/python/2022/notes/1/#conditionals): allow the program to make decisions. *Mathematical operators* consist of "<", ">", "<=", ">=", "==" and "!=". *Boolean operators* consist of *and*, *or*, *not*.
- [if statements](https://cs50.harvard.edu/python/2022/notes/1/#if-statements): use boolean values (*true* or *false*) to decide whether or not to execute the code.
- [elif, else](https://cs50.harvard.edu/python/2022/notes/1/#control-flow-elif-and-else): *control flow* is the flow of decisions. To improve the code (and control flow) use *elif* and/or *else*.
- [Pythonic conditional](https://cs50.harvard.edu/python/2022/notes/1/#pythonic): represents the code almost like an English sentence *return True if condition==True else False* or *return condition==True*.
- [Match](https://cs50.harvard.edu/python/2022/notes/1/#match): *match* is used to conditionally run code that matches certain values. Is used in conjunction with *case*. The special case for everything else is *case _:*.

### [Problem Set 1](https://cs50.harvard.edu/python/2022/psets/1/)
- [Deep Thought](https://cs50.harvard.edu/python/2022/psets/1/deep/): 
- [Home Federal Savings Bank](https://cs50.harvard.edu/python/2022/psets/1/bank/): 
- [File Extensions](https://cs50.harvard.edu/python/2022/psets/1/extensions/): 
- [Math Interpreter](https://cs50.harvard.edu/python/2022/psets/1/interpreter/): 
- [Meal Time](https://cs50.harvard.edu/python/2022/psets/1/meal/): 


## [Lecture 2: Loops](https://cs50.harvard.edu/python/2022/weeks/2/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/2/)
- [While](https://cs50.harvard.edu/python/2022/notes/2/#while-loops): is a loop with unspecified number of iterations. It will stop if the condition of the loop has been fulfilled.
- [Continue, Break, Return](https://cs50.harvard.edu/python/2022/notes/2/#improving-with-user-input): are used to alter the flow of a loop. *Continue* explicitly tells Python to go to the next iteration of a loop. *Break*, on the other hand, tells Python to "break out" of a loop early before it has finished all of its iterations. *Return* performs similarly to *break*, but also finishes the function containing the loop.
- [List](https://cs50.harvard.edu/python/2022/notes/2/#more-about-lists): a python data type containing multiple values in one place in a contiguous block of memory. Create and assign a list: *my_list = [0, 1, 2]* or using constructor: *my_list=list((1, 2, 3))*.
- [For](https://cs50.harvard.edu/python/2022/notes/2/#for-loops): this loop iterates through a *list* of items. To generate a list of *int* use *range(X)* and it looks like *0, 1, ..., X-1*. The pythonic way of using a for loop if the variable *i* that stores the number of the iteration is not used is to replace it with "_".
- [Dictionaries](https://cs50.harvard.edu/python/2022/notes/2/#dictionaries): is a data structure that allows you to associate keys with values, similar to *hashtable* storing *key-value pairs*. To create a *dict* use *my_dict={ "key": "value", ... }*. Python has a special keyword **None** to specify there is no value associated with a key or absents of value.
- [Str concatenation](https://cs50.harvard.edu/python/2022/notes/2/#mario): is a pythonic way to create new strings by looping through current string *N* number of times and concatenating them (with "\*"): *new_str=current_str\*N*.  

### [Problem Set 2](https://cs50.harvard.edu/python/2022/psets/2/)
- [camelCase](https://cs50.harvard.edu/python/2022/psets/2/camel/): 
- [Coke Machine](https://cs50.harvard.edu/python/2022/psets/2/coke/): 
- [Just setting up my twttr](https://cs50.harvard.edu/python/2022/psets/2/twttr/): 
- [Vanity Plates](https://cs50.harvard.edu/python/2022/psets/2/plates/): 
- [Nutrition Facts](https://cs50.harvard.edu/python/2022/psets/2/nutrition/): 


## [Lecture 3: Exceptions](https://cs50.harvard.edu/python/2022/weeks/3/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/3/)
- [Exceptions](https://cs50.harvard.edu/python/2022/notes/3/#exceptions): 
are things that go wrong within our code. For example: *SyntaxError* are those that require you to double-check that you typed in your code correction, *runtime errors* refer to those created by unexpected behavior within your code, *ValueError* occurs when a variable type is not used correctly, *NameError* describes a parameter not defined, *KeyboardInterrupt* is raised when ctrl+c from user/os stops the code from executing. As programmers, we should be defensive to ensure that our users are entering what we expected. **Never trust users to follow instructions or to comply to inputs or actions**.
- [Try](https://cs50.harvard.edu/python/2022/notes/3/#try): is a block that lets you test code for errors. It is used in conjunction with *except* and *else*.
-  [Pass](https://cs50.harvard.edu/python/2022/notes/3/#pass): is a statement that does nothing. It can be used when a statement is required syntactically but the program requires no action.
- Caller vs. Callee: A caller is a function that calls another function; a callee is a function that was called. Ex: *main()* calls *print()*; *main()* is the **caller** and *print()* is the **callee**.
- [Finally](https://docs.python.org/3/reference/compound_stmts.html#finally-clause): specifies a ‘cleanup’ handler. When a *return*, *break* or *continue* statement is executed in the *try* suite of a *try … finally* statement, the *finally* clause is also executed ‘on the way out.’ The finally block will always be executed if it is implemented in code, no matter if the try block raises an error or not.
- [With](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement): is a statement used to wrap the execution of a block with methods defined by a context manager. It is typically used with file operations or similar contexts. For more info see [PEP 343 – The “with” Statement](https://peps.python.org/pep-0343/).
- [Raise](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement): evaluates the first expression as the exception object.

### [Problem Set 3](https://cs50.harvard.edu/python/2022/psets/3/)
- [Fuel Gauge](https://cs50.harvard.edu/python/2022/psets/3/fuel/): 
- [Felipe’s Taqueria](https://cs50.harvard.edu/python/2022/psets/3/taqueria/): 
- [Grocery List](https://cs50.harvard.edu/python/2022/psets/3/grocery/): 
- [Outdated](https://cs50.harvard.edu/python/2022/psets/3/outdated/): 


## [Lecture 4: Libraries](https://cs50.harvard.edu/python/2022/weeks/4/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/4/)
- [Libraries](https://cs50.harvard.edu/python/2022/notes/4/#libraries): Python supports sharing functions or features through *libraries* and *modules*. Libraries encourage reusability in code. After *installing* any library, to use it you need to *import* it. Python will *import* whole library if the desired functions are not specified: *from lib import func_1, ...*. This is a way to improve code memory / space.
- [Random](https://cs50.harvard.edu/python/2022/notes/4/#random): is a library that comes with Python and implements pseudo-random number generators for various distributions. Functions used in this lecture include: *choice()*, *randint()*, *shuffle()*.
- [Statistics](https://cs50.harvard.edu/python/2022/notes/4/#statistics): is another built-in module that provides functions for calculating mathematical statistics of numeric (Real-valued) data. Function used in this lecture is *mean()*.
- [Command-Line Arguments](https://cs50.harvard.edu/python/2022/notes/4/#command-line-arguments): For increasing functionality, python supports command-line arguments passed directly at execution of the program. *sys* is a module that allows us to take arguments at the command line. *argv[]* is used to access data from command-line, where *argv[0]=program_name* or *argv[0]=path_to_program* (depending on OS). This functionality is used in conjunction with *try ... except* block and, sometimes, with *slicing* and *for* loops. Other used function in this lecture is *exit()*.
- [Slice](https://cs50.harvard.edu/python/2022/notes/4/#slice): is a subset of a data structure (*list* in this case). With this feature the compiler can consider a different start and end of the list.
- [Packages](https://cs50.harvard.edu/python/2022/notes/4/#packages): Python supports numerous powerful third-party libraries that add functionality. Implemented as folders, these are called *packages*. [PyPI](https://pypi.org/) is the place of all available third-party packages. To install a package use *pip install package_name --user*. Packages used in this lecture include: *cowsay*, *requests*.
- [APIs](https://cs50.harvard.edu/python/2022/notes/4/#apis): or **application program interfaces** allow you to connect to the code of others. *requests* is popular for calling HTTP methods like: *get*, *post* etc. Usually the output of APIs is a JSON (*JavaScript Object Notation*) and python comes with a *json* library built-in with *dumps()* function to print result more readable.
- [Making Your Own Libraries](https://cs50.harvard.edu/python/2022/notes/4/#making-your-own-libraries): to upload libraries to PyPI refer to [uploading documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/). To use local libraries make sure they are in the same folder as the program. Use __name__ keyword (if __name__ == "__main__") to divide functionality between main program and module.
- ANSI color escape codes: are used to show terminal output more clearly.

### [Problem Set 4](https://cs50.harvard.edu/python/2022/psets/4/)
- [Emojize](https://cs50.harvard.edu/python/2022/psets/4/emojize/): 
- [Frank, Ian and Glen’s Letters](https://cs50.harvard.edu/python/2022/psets/4/figlet/): 
- [Adieu, Adieu](https://cs50.harvard.edu/python/2022/psets/4/adieu/): 
- [Guessing Game](https://cs50.harvard.edu/python/2022/psets/4/game/): 
- [Little Professor](https://cs50.harvard.edu/python/2022/psets/4/professor/): 
- [Bitcoin Price Index](https://cs50.harvard.edu/python/2022/psets/4/bitcoin/): 


## [Lecture 5: Unit Tests](https://cs50.harvard.edu/python/2022/weeks/5/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/5/)
- [Unit Tests](https://cs50.harvard.edu/python/2022/notes/5/#unit-tests): are a way of testing the code with various measurements (usually automatic testing).
- [Assert](https://cs50.harvard.edu/python/2022/notes/5/#assert): verifies the functionality of functions and if all are correct than no error messages will appear (no *AssertionError* raised). This approach is useful if functions will return something, otherwise it can't be tested with *assert*.
- [pytest](https://cs50.harvard.edu/python/2022/notes/5/#pytest): is a third-party library that allows you to unit test your program. Learn more in [Pytest’s documentation](https://docs.pytest.org/en/7.1.x/getting-started.html). It is possible to group testing files in folders, but a file named "__init__.py" is necessary to tell python this is a package.

### [Problem Set 5](https://cs50.harvard.edu/python/2022/psets/5/)
- [Testing my twttr](https://cs50.harvard.edu/python/2022/psets/5/test_twttr/): 
- [Back to the Bank](https://cs50.harvard.edu/python/2022/psets/5/test_bank/): 
- [Re-requesting a Vanity Plate](https://cs50.harvard.edu/python/2022/psets/5/test_plates/): 
- [Refueling](https://cs50.harvard.edu/python/2022/psets/5/test_fuel/): 


## [Lecture 6: File I/O](https://cs50.harvard.edu/python/2022/weeks/6/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/6/)
- [File I/O](https://cs50.harvard.edu/python/2022/notes/6/#file-io): Program variables are volatile, so storing data in files is essential. *os* library is a builtin python file i/o handling module. It has many functions: *open()*, *close()*, *write()*, *read()*, *readlines()* and others.
- [open](https://cs50.harvard.edu/python/2022/notes/6/#open): Open files with appropriate type: *w*, *r*, *a*, ... Files are created automatically if they don't already exist. The default file location is the same as the program that uses them.
- [with](https://cs50.harvard.edu/python/2022/notes/6/#with): is the pythonic way to handle file objects and automate the closing of a file.
- [csv](https://cs50.harvard.edu/python/2022/notes/6/#csv): means “comma separated values” and is a python builtin library with many functionalities like: *reader()*, *DictReader()*, *writer()*, *DictWriter()*, *writerow()*.   
- Sorting list/dict from file or local list/dict is demonstrated in this course.
- Searching dict by key or value is demonstrated in this course.
- lambda functions for sorting are demonstrated in this course. The syntax is *lambda parameter_of_lambda_func: return_value_of_lambda_func*.
- [pillow (PIL)](https://cs50.harvard.edu/python/2022/notes/6/#binary-files-and-pil): is library for image/video processing and binary files. In this course *save()* function is demonstrated.

### [Problem Set 6](https://cs50.harvard.edu/python/2022/psets/6/)
- [Lines of Code](https://cs50.harvard.edu/python/2022/psets/6/lines/): 
- [Pizza Py](https://cs50.harvard.edu/python/2022/psets/6/pizza/): 
- [Scourgify](https://cs50.harvard.edu/python/2022/psets/6/scourgify/): 
- [CS50 P-Shirt](https://cs50.harvard.edu/python/2022/psets/6/shirt/): 


## [Lecture 7: Regular Expressions (regex)](https://cs50.harvard.edu/python/2022/weeks/7/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/7/)
- [Regular Expressions](https://cs50.harvard.edu/python/2022/notes/7/#regular-expressions): or “regex” is a pattern to match data for validation / cleaning / creation purposes. Example is validating input from user (email address, password, age etc.). In python there are builtin modules and functions to check regex patterns: *re* with *search()*, *sub()*, *match()*, *fullmatch()* functions to find and format data. More about info in [regex documentation](https://docs.python.org/3/library/re.html) about syntax, special characters, flags, exceptions etc.
- Walrus operator *:=* assigns a value from right to left and allows us to ask a boolean question at the same time.
- Online tools to create, test, visualize regex (eg. [regex101.com](https://regex101.com/), [debuggex.com](https://www.debuggex.com/)).
   
### [Problem Set 7](https://cs50.harvard.edu/python/2022/psets/7/)
- [NUMB3RS](https://cs50.harvard.edu/python/2022/psets/7/numb3rs/): 
- [Watch on YouTube](https://cs50.harvard.edu/python/2022/psets/7/watch/): 
- [Working 9 to 5](https://cs50.harvard.edu/python/2022/psets/7/working/): 
- [Regular, um, Expressions](https://cs50.harvard.edu/python/2022/psets/7/um/): 
- [Response Validation](https://cs50.harvard.edu/python/2022/psets/7/response/): 


## [Lecture 8: Object-Oriented Programming](https://cs50.harvard.edu/python/2022/weeks/8/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/8/)
- python's programming paradigms: procedural (execute code step by step), functional (powerful functions + lambda), OOP (abstraction, classes, encapsulation, methods, overloading, inheritance etc.)   
- tuples, defensive programming, TypeError   
- classes, "..." to skip, attributes ("." syntax), objects   
- correctness of data, validation, error raising    
- instance variables + private "'_'var_name" convention (honor system)   
- instance methods [self]: __init__ = initializer, @property = getter, @attribute_name.setter = setter, __str__ = print method, __add__ = operator overloading   
- class methods (similar to Singleton) [cls]: @classmethod   
- class variables (shared by all functionality of the class)   
- inheritance, superclasses, super()   

### [Problem Set 8](https://cs50.harvard.edu/python/2022/psets/8/)
- [Seasons of Love](https://cs50.harvard.edu/python/2022/psets/8/seasons/): 
- [Cookie Jar](https://cs50.harvard.edu/python/2022/psets/8/jar/): 
- [CS50 Shirtificate](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/): 


## [Lecture 9: Et Cetera](https://cs50.harvard.edu/python/2022/weeks/9/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/9/)
- data type -> set   
- global variables, Unbound Local Error   
- constant variables (more like honor system)   
- dynamically typed engine (vs. strongly typed), type hints, mypy, "var: type", "func() -> return_type"   
- document strings, comments conventions, restructured text   
- sys.argv, '\-initial', '\-\-word', argparse library   
- unpacking and operators: '\*', '\*\*', named parameters, variable number of arguments: '\*args', '\*\*kwargs'   
- programming models (procedural, OOP, functional): map(), filter   
- list comprehension, dictionary comprehension   
- enumerate   
- generate, yield statement   
- text-to-speech pyttsx4

### [Final Project](https://cs50.harvard.edu/python/2022/project/)
