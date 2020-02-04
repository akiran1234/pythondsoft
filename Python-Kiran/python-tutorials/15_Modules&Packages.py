01) Packages are hierarchically at the top level which is nothing but directory(parent package) having sub directories (sub packages) and modules and again sub packages can have modules with in it.
01) group of packages(parent packages + sub packages with in parent package) is called library

/home/maindir/                                                          # The main point is the script that is importing(mainscript.py ) and package(pack1) should be in the same directory to locate.
							  |- __inti__.py                                  1.  from pack1 import module1  2.  from pack1.pack2 import module2 (from sub package importing module2)
							  |- mainscript.py 
							  |- pack1
							                 |- __init__.py
											 |- module1.py
											 |- pack2
											               |- __init__.py
														   |- module2.py (imported modules, variables, functions, classes)

02) By creating __init__ file in a dir we can tell the interpreter that it is a package but how ever this file is not necessary in the later versions of Python 3.3
03) Modules are nothing but python scripts with .py extension.
04) A module can have variables, functions and classes and a module can also include runnable code.
05) Grouping related code into a module makes the code easier to understand and use.
06) A module can be imported using import statement.
07) import module_name ==> This will import all the attributes of the module into current module.
08) A module will have variables, functions, classes.
09) __name__ will print the module name= __main__ when the script has run as main script.
10) when __name__ is used in import script then it gives the script(module) name.
11) All modules belongs to <class 'module'>; check <type(numpy)>
12) dir('modules') is builtin function to query all the modules available in python library.
13) dir('numpy')   giving only module name will list all the attributes(Var,func,class,implicit builtin attributes) of the module.

import module_math as m        # This is nothing but running module_math.py from top to bottom in the current module namespace.
                                                           # Please note after importing print statements from "SampleTest" module is printed in the current module.
from module_hello import hello,welcome,a
														   # The above import statement will import only specified functions to current namespace and no other attributes are imported.
														   # Please note after importing print statement of module_hello executed.
														   # Using this statement module name is not required, directly function name can be used to refer that module.
# from module_hello import *  # This * will pull all the attributes and functions in to current workspace. But this will create ambiguity problem with other
                                                           # (cont..) modules hence this is not best practise.

print('Value of attribute __name__:',__name__)      # Print the main  script.
print('Printing y value from SampleTest Module',m.y)
print('Printing x value from SampleTest Module',m.x)

print(m.add(10,20))
print(m.mul(100,20))
print(m.sub(10,10))

print(hello())
w=welcome()
print(w)
print(a)

print('************************************************************************************************')
# Members of the module: The modules(imported in the current programme), variables, functions, classes are members of the module (current module)
dir()                                      # This is a bulitin function, when dir() is called with out parameters it will display current module members.
dir(math)                            # This will display the members of the math module. dir() passed with argument module name i.e math.
print(dir(__builtins__))  # will display all the members of the __builtins__ module which is automatically imported in any module.

Ex:
		from Scripts import module_1
		x=10
		y=20
		print(dir())                           # will print the members of the current module. (module_1, x, y and predefined memebers ('__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',))
		print(dir(__builtins__))    # will print the members of the __builtins__ module.
		print(dir(math))                 # will print the members of the math module.

 We can find the module path by: import sys; print(sys.path)
 By default the following below attributes will be created for any module:
 '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__'
 Below are the few important attributes we need to know.
 __builtins__ : This module contains built-in functions which are automatically available in all Python modules that is how builtin functions works with out importing builtins module
 __doc__      : To find the doc string of a function with in a module. print(func_name.__doc__)
 __file__     : To print the module name of a script. Usage print(__file__), this has to be used with in the script.
 __name__     : The value is set to '__main__'  when module run as main script and when it is imported the value of __name__  is set to module name.

