CS50p YouTube playlist here: https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V  
Python documentations: https://docs.python.org/3/  
[Compound statements in python docs]: https://docs.python.org/3/reference/compound_stmts.html   
Python Package Index documentation: https://pypi.org/   
Personal CS50p ChatGPT: https://chat.openai.com/c/68fb62eb-bddc-47ee-b7b8-cf9f0a7f0cc8  


Lecture 0 = Variables, Functions:   
- comments   
- variables, data types (int, float, str)   
- functions, arguments, parameters, print(), input()   
- str methods: isalpha(), strip(), title(), split()   
- interactive mode   
- int() and float() type converters, round()  
- formatting numbers for print(), numeric types   

Lecture 1 = Conditionals:   
- conditionals, boolean operations, comparisons   
- if, elif, else, and, or, not   
- pythonic way to implement conditional   
- match and case (similar to switch and case from Java)

Lecture 2 = Loops:
- while, break, continue, return   
- for, range(), [pythonic way], str concatenation     
- data types (list: constructor, assignment, len(); dictionaries: assignment), None   

Lecture 3 = Exceptions:   
- try, except, else, pass   
- errors: SyntaxError (can't be caught), ValueError, NameError (parameter not defined), KeyboardInterrupt (ctrl+c from user/os)   

Lecture 4 = Libraries:   
- import, from, modules,   
- random library: choice(), randint(), shuffle()   
- statistics library: mean()   
- sys library: argv[], exit()   
- slicing data structure (list)   
- ANSI color escape codes   
- packages [pip install lib_name --user]: cowsay, requests   
- json library: dumps()   
- importing my own libraries/functionalities in same folder; __name__ keyword   

Lecture 5 = Unit Tests:   
- assert, AssertionError, with   
- pytest library: raises()   
- pytest and test folders: __init__.py   

Lecture 6 = File I/O:   
- os library (builtin python): file object, open(), close(), write(), read()   
- with open() as file pythonic statement   
- os library: readlines() the pythonic way   
- csv library: reader, DictReader, writer, DictWriter   
- sorting list/dict from file or local list/dict
- searching dict by key or value   
- lambda functions for sorting   
- pillow (PIL) library for image/video processing: save()   

Lecture 7 = Regular Expressions (regex):
- validate email from str: interrogate chars, split(), endswith()   
- re library: search(), sub() [finding and formatting]   
- regex patterns, multiple flags (VERBOSE explanations)   
- walrus operator
- extract username from url [non-capturing group]
- online tools to create, test, visualize regex (regex101.com, debuggex.com, github_regex-visualizer)   
   
Lecture 8 = Object-Oriented Programming:   
- python's programming paradigms: procedural (execute code step by step), functional (powerful functions + lambda), OOP (abstraction, classes, encapsulation, methods, overloading, inheritance etc.)   
- tuples, defensive programming, TypeError   
- classes, "..." to skip, attributes ("." syntax), objects   
- correctness of data, validation, error raising    
- instance variables + private "'_'var_name" convention (honor system)   
- instance methods [self]: __init__ = initializer, @property = getter, @attribute_name.setter = setter, __str__ = print method, __add__ = operator overloading   
- class methods (similar to Singleton) [cls]: @classmethod   
- class variables (shared by all functionality of the class)   
- inheritance, superclasses, super()   

Lecture 9 = Et Cetera:   
- data type -> set   
- global variables, Unbound Local Error   
- constant variables (more like honor system)   