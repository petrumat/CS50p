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
- [Interactive mode](https://cs50.harvard.edu/python/2022/notes/0/#integers-or-int) is a feature of Python where code can be executed interactively in terminal. Enter *python* in terminal and ">>>" will appear for this feature.

### [Problem Set 0](https://cs50.harvard.edu/python/2022/psets/0/)
- [Indoor Voice](https://cs50.harvard.edu/python/2022/psets/0/indoor/): a python program that converts user input into lowercase.
- [Playback Speed](https://cs50.harvard.edu/python/2022/psets/0/playback/): a python program that outputs the same input, replacing each space with "...".
- [Making Faces](https://cs50.harvard.edu/python/2022/psets/0/faces/): a python program that changes ":)" to 🙂 and ":(" to 🙁.
- [Einstein](https://cs50.harvard.edu/python/2022/psets/0/einstein/): a python program that determines energy based on mass.
- [Tip Calculator](https://cs50.harvard.edu/python/2022/psets/0/tip/): a python program that calculates tips depending on dollar amounts and percentages.


## [Lecture 1: Conditionals](https://cs50.harvard.edu/python/2022/weeks/1/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/1/)
- **Conditionals**: allow the program to make decisions. *Mathematical operators* consist of "<", ">", "<=", ">=", "==" and "!=". *Boolean operators* consist of *and*, *or*, *not*., comparisons
- **if statements**: use boolean values (*true* or *false*) to decide whether or not to execute the code. elif, else
- pythonic way to implement conditional
- match and case (similar to switch and case from Java)

### [Problem Set 1](https://cs50.harvard.edu/python/2022/psets/1/)
- [Deep Thought](https://cs50.harvard.edu/python/2022/psets/1/deep/): 
- [Home Federal Savings Bank](): 
- [File Extensions](): 
- [Math Interpreter](): 
- [Meal Time](): 


## [Lecture 2: Loops](https://cs50.harvard.edu/python/2022/weeks/2/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/2/)
- while, break, continue, return   
- for, range(), [pythonic way], str concatenation     
- data types (list: constructor, assignment, len(); dictionaries: assignment), None   

### [Problem Set 2](https://cs50.harvard.edu/python/2022/psets/2/)
- [](): 
- [](): 
- [](): 
- [](): 
- [](): 


## [Lecture 3: Exceptions](https://cs50.harvard.edu/python/2022/weeks/3/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/3/)
- try, except, else, pass   
- errors: SyntaxError (can't be caught), ValueError, NameError (parameter not defined), KeyboardInterrupt (ctrl+c from user/os)   

### [Problem Set 3](https://cs50.harvard.edu/python/2022/psets/3/)
- [](): 
- [](): 
- [](): 
- [](): 
- [](): 


## [Lecture 4: Libraries](https://cs50.harvard.edu/python/2022/weeks/4/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/4/)
- import, from, modules,   
- random library: choice(), randint(), shuffle()   
- statistics library: mean()   
- sys library: argv[], exit()   
- slicing data structure (list)   
- ANSI color escape codes   
- packages [pip install lib_name --user]: cowsay, requests   
- json library: dumps()   
- importing my own libraries/functionalities in same folder
- __name__ keyword (if __name__ == "__main__")   

### [Problem Set 4](https://cs50.harvard.edu/python/2022/psets/4/)
- [](): 
- [](): 
- [](): 
- [](): 
- [](): 


## [Lecture 5: Unit Tests](https://cs50.harvard.edu/python/2022/weeks/5/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/5/)
- assert, AssertionError, with   
- pytest library: raises()   
- pytest and test folders: __init__.py   

### [Problem Set 5](https://cs50.harvard.edu/python/2022/psets/5/)
- [](): 
- [](): 
- [](): 
- [](): 
- [](): 


## [Lecture 6: File I/O](https://cs50.harvard.edu/python/2022/weeks/6/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/6/)
- os library (builtin python): file object, open(), close(), write(), read()   
- with open() as file pythonic statement   
- os library: readlines() the pythonic way   
- csv library: reader, DictReader, writer, DictWriter   
- sorting list/dict from file or local list/dict
- searching dict by key or value   
- lambda functions for sorting   
- pillow (PIL) library for image/video processing: save()   

### [Problem Set 6](https://cs50.harvard.edu/python/2022/psets/6/)
- [](): 
- [](): 
- [](): 
- [](): 
- [](): 


## [Lecture 7: Regular Expressions (regex)](https://cs50.harvard.edu/python/2022/weeks/7/)

### [Concepts](https://cs50.harvard.edu/python/2022/notes/7/)
- validate email from str: interrogate chars, split(), endswith()   
- re library: search(), sub() [finding and formatting]   
- regex patterns, multiple flags (VERBOSE explanations)   
- walrus operator
- extract username from url [non-capturing group]
- online tools to create, test, visualize regex (regex101.com, debuggex.com, github_regex-visualizer)   
   
### [Problem Set 7](https://cs50.harvard.edu/python/2022/psets/7/)
- [](): 
- [](): 
- [](): 
- [](): 
- [](): 


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
- [](): 
- [](): 
- [](): 
- [](): 
- [](): 


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

### [Problem Set 9](https://cs50.harvard.edu/python/2022/psets/9/)
- [](): 
- [](): 
- [](): 
- [](): 
- [](): 
