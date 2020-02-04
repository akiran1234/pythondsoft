######## Dsoft #####################
Lowest(Machine Code 1's and 0's Very hard for Humans to code),
Assembely(ASM), 
Mid Level(C,C++), 
High Level(Python, Java etc..)

What is low level language
General Purpose High level programming language.
Gudo Van Rossam, Invented by.
1991 it was firtst released to public.
Python language was written in C language.
Cpython is an interpreter written in C, used to read the highlevel source code and converts into byte code. This byte code will be used by PVM (Python Virual Machine) to generate machine code.
source code --> Cpython Interpreter --> byte code --> PVM--> Machine Code --> CPU (Executes the machine code.)
Refer:   https://www.youtube.com/watch?v=aKoGwEPoQ5o
Diff b/w: Compiler vs Interpreter
https://www.geeksforgeeks.org/language-processors-assembler-compiler-and-interpreter/
Flavours of Python:   https://dev.to/alexgascon/cpython-cython-pypy-an-introductory-guide-to-the-different-python-variants-i4h
Statistically type (data types are static we cannot assign other data types)
# In Java
int a=10
a='hello' # this is not allowed 'a' is a static datatype across the programme.
# In Python
a=10
a="hello" # This is allowed, Python is dynamically typed.

Python features has taken from other Languages.
Procedural/Functional Programming (C) # No Class/ object need to run the programe like in Java.
OOPS (C++)
Interpreted (Shell Script)
Modular (Modula 3)
========== Video 2 Features of Python ============================
# Features of Python
Open source.
Platfrom independent (Python applications can be built on any machines Window, Linux etc..)
Portable( code can be easily migrated to other machines with out any changes.)
Extensible (External programms like Java and C++ etc can be imported to existing  Python programming)
Embedded (Python code can be imported to other Programming Languages.)
Dynamically Typed (Data type declaration not required, python interpreter will declare automatically)
Rich API's.
========== Video 3  Identifiers============================
# Identifiers
Names given to variables, functions, classes, objects, methods, modules.
variable name = alpha_numeric and no numeric_alpha and only special character can be used is underscore(_). usually in lower case, constants in UPPER case
identifiers cannot be python key words.
Constants: In java --> final x=10; this value cannot be changed across the programme compiler will not allow.
In python constants will be in upper case VALUE=10, how ever this value can be changed but it is not a good programming practice.
variable name can start with underscore (_marks=20) this is used for  private variable representaion in python.
_marks=20 (private)
__marks=20 (Strongly private)
__marks__=20 (Not suggested to use for user defined variables.)
identifier names start and ends with double underscore belongs python interpreter (Ex: __name__, __init()__) not suggested to use in user defined variables.
================ Video 4 ============================
# Key words
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
 ================ Video 5   Data Types ============================
 primitive datatypes vs Non-Primitive datatypes 
 Primitive datatypes which will have length defined. (int x=10, float y=20.50, char c='d' in Java)
 Non-Primitive: Data type is not defined (Lenght is dynamic in nature)
 In python every data type  is non primitive that is the reason dataypes can take any length.(There is no lenght limit unlike Java)
 int(decimal,binary,octal,hexadecimal),float,bool,str,bytes,bytesarray,range,list,tuple,set,dictionary.
 
 In python 2 we have int, long datatypes and in Python 3 only int datatype it will handle both int and long values in Python3x
 In Python 2 the print statement will have paranthesis and in Python 3 print() statement paranthesis is mandatory.
 
 ================ Video 6   Data Types and Type casting============================
 typecasting: int(54.64),int(True),int(False),    float(True),float(False), float(5),str(34.567),     
 bool(-5),bool(0),bool(6), bool(-0.0001),bool(''),bool(' '),bool('hello')  # Non Zero & Non empty for string is True and only Zero is false for int or float both Positive and negative.
 complex(1), complex(0),complex(True),complex(100+23j)
 String dataype and indexing and slice operator. [Retrive the elements of a string]
 
 ================ Video 7   Mutable vs Immutable============================
 id()
 is()
 python garbage collection
 reusablity of objects concept for int, float, complex and it's behaviour.
 int ==> 0 to 256
 bool==> Always because only 2 values 0 or 1.
 string=> Always it will reuse, because the maximum number of strings we use are very limited.
 float& complex ==> it will reuse the objects because they are infinite values.
 
  ================ Video 8   ============================
 bytes  (immutable), range of data (0-256)
 bytearray (mutable)
 byte and byte array used to strore binary data like pictures, videos, mainly for unstructured data.
 list
  ================ Video 9  ============================
  talked abount various data types and their properties.
  list, tuple, set,frozenset,dictionary
  various types of declaration
  defining one dataype in other datatype and accessing those elements ;  s=(1,2,3,[4,5,6,7])     print(s[3][-1])
  
================ Video 10  ============================
Discussed abount None and pass key words.
None datatype equvalent to Null in Java
def f1():
    pass
print(f1())
Escape characters ; h="hello this is kiran \"I am doing good\" now" or h='hello this is kiran "I am doing good" now'
Constants in pyton discussed.

================ Video 11 Operators  ============================
Operators
Important point is how /,   //(Floor operator returns only int value in float format), %    works in Arithmetic operator works.
Relations operator: Chaining of relation operators -->    1<2<3<4<5>9 (False) once condition fail everything is failed.
Relation operation on strings is possible and comparision will be done by ascii values.
Indentation how it works in Python.
================ Video 12  Operators============================
boolean operators or conditional operators
Myth: only applied on boolean values
Fact: It can be applied on numbers and string and in combination.
Bitwise operators: It can be applied only on int types and binary values
Bitwise comparision will happen internally for this operation.
================ Video 13  Operators============================
Bitwise operators: Can be applied only on int type and boolean types.
Assignment Operators: a=5
compound operators: a=a+5 -->    a+=5
Increment and decrement operators not available in Python.   (++10 = +(+10) )       (---3 = -(-)(-3)=-3),     5++ = In valid.
Ternary Operators:  100 if(5<10) else 200
Nested Ternary Operators:  print(100 if (1000<20) else (300 if(30>250) else 400))
Identity Operators (is, is not)
Membership Operators(in, not in)

================ Video 14  Operator Precedence ============================
Operators precidence in python (Pemdas)
Talked about math module.
In Python 2.x we have 
x=raw_input("enter value x")  # raw_input always reads the data in string datatype only
y=input("enter value of y")      # This will dynamically cast the value i.e dynamicaly typed.
In python 3x we have only input() which always reads data in string datatype, and type casting needs to be taken care by the developer.
raw_input("Enter the value")=input("Enter the value")
x=int(input("enter the x value"))     # The string value is tycasted to int in 3.x

================ Video 15  Input Streams, eval(), command line arguments. ============================
read multiple input values
x=input("enter the numbers with spaces\n").split()
a,b,c=[int(y) for y in x ]
print(a,type(a))
print(a,type(b))
print(a,type(c))

eval() # evaluate function takes string argument and evaluates it's datatypes and perform operation on it.
print(eval("1+2+3+44.5")) # eval function works only int or float values and not string values.
# Command Line arguments 
ex:   python test.py 1 2 3 4        # here 1 2 3 4  are arguments.
from sys import argv     # argv is a list variable and it holds all the arguments that is been passed to script
print(argv)    # o/p ['sample.py', '1', '2', '3', '4']      Note: First element of the list is script name and all the elements of the list are in string datatype.
================ Video 16  command line arguments. ============================
python sample.py "hello this is testing" i am boy  # strings with spaces should be given in "" double quotes.
['sample.py', 'hello this is testing', 'i', 'am', 'boy']

================ Video 17  output streams ============================
print("Sending the message to Screen")
print(1,2,3,4,sep=',',end='*')   # default arguments sep=' ' (space)  end='\n' (New line)
print("Hello my name={}, my age={} and city={}".format('Linux',40,'LA'))   # Passing arguments to string.
================ Video 18  Control Statemetns ============================
# Control statemetns
1) Conditional Statemtns ===>       (if else)   (if elif else)    Based on the conditions statements will be executed.  Note: No Switch statement in Python
2) Loops or Iterative Statements ==> while, for        Note: No do while loop in Python.
when to use while loop and for loop:
when the no of iterations is known then while loop.
when the no of iterations is un-known then for loop.
3) Transfer Statements ==> break, continue, pass      Control will be transfered from one statement to other statement.

================ Video 19  Nested loops  ============================
# Discussed abount pattern programming.

================ Video 20  Transfer Statements  ============================
# Talked about else blocks with for & while loops.
# break, continue, pass
1) break statement is always used in loops for a specific condition. If break is encountered the loop is broken i.e it will not go for next iteration and control comes out of the loop.
2) if there are nested loops, if the  break is in inner loop then it is applicable only for inner/current loop and not for outer loop.

for i in range(3):
    for j in range(5,8):
        print(j)
        break
    print(i)

# continue
1. continue will skip the rest of statements in the loop and goes for next iteration.

for i in range(5):    # Run the code in debugg mode, 2nd print statement will be skipped.
    print("Before:{}".format(i))
    continue
    print("After:{}".format(i))

for i in range(3):      # This example, continue statement will skip the if block statements and as well as statements in the out of if block which is part of for loop.
    print("Before:{}".format(i))
    if(i==1):
        continue
        print("After:{}".format(i))
    print("Out of if block")
    print("In for loop")

# pass is used to define an empty/dummy block of statements in if or else or function or class or method
for i in range(3):
    print("Before:{}".format(i))
    pass    # There is no effect of this pass key word.
    print("After:{}".format(i))

if (False):
    pass   # empty block 
else:
    print("Hello")
	
================ Video 21,22,23,24,25,26   ============================	
del key word and it's uses.
del is used to delete the identifiers(variables, functions, classes, methods) in python programming for better meory utilization.
x=10
del x
def func1():
	pass
del func1  # function name.

string object:
Multi Line string:
s='''hello this
kiran'''   # This is valid and it is multi line string.

# This is applicable for all iterable objects.(String, List, Tuple, set, frozenset)

s[start_position:end_position:stepoperator/increment operator]
# Forward direction
default value for start position is 0, 
default value for end of the string is length of the string, 
default value for step/increment operator is 1.
s[::]

# Backward direction
default value for start position is -1, 
default value for end of the string is -(length of the string), 
default value for step/increment operator is -1.
# Note end_position is always excluded
# step operator will tell the direction. if +ve start to end , if step operator is -ve in reverse direction

s[:5]                # by default step operator will be 1 and positive and 5th position is excluded.
s[::2]              # starts from zero index and till end of the string increment by 2
s[-3:0:-2]      # starts from -3 position and 0th position is excluded, incremented by -2
s[::1]              # starts from 0 to end in postive direction
s[::-1]              # starts from end to start in negative direction

================ Video 28 Lists   ============================================
String programms very important go through it once again.
List basics theory
Collections: A group of elements in a single entity is called collection.
================ Video 29  29 List Functions Part-1  ============================	
Discussed about list methods.

================ 37,38  Functions Part-1, Part-2 ==========================
functions: The block of code which is used in programme repeatedly across the programme with same / different parameters.
1. Functions are used for code re usability 
2. Two type of functions in python.
               1.   In built functions
			   2.   User defined functions (UDF's)
def cal():
        body
		return

def fun():
    """I will return multiple values, it is valid in python"""
    return 1,2,3
	print("I am after the return statement, I will not get executed.")
print(fun.__doc__) # To call doc string
print(fun()) # x,y,z=func()  this is also valid.

* def is used to define function and return is optional. If function doesn't return any thing the returun type is None.
* In python return statement can return multiple values and return type is a set.
* If there are any statements beyond return statement those statements will not be executed.

# Arguments in function;  Actual Arguments (calling function), Formal Arguments (called function)
# Types of Arguments
1. Positional Arguments
2. Key word Arguments
3. Default Arguments
4. Variable length Arguments
================ 39 Functions Part-3 ==========================
# Talked abount global variables but not LEGB.
group of functions in a file           --> module (filename.py) a python script is nothing but a module.
group of modules in a folder      --> package
group of packages in a folder     --> library

globals() # To display the global content of the module.
================ 40 Recursive functions ==========================
Recursive Function: A function calling by itself is called recursive function.
Lambda Function: A function which doesn't have name and implicitly it will return.
s=lambda x,y,z:x*x+y+z
print(s(10,20,30))
Ternary Operator with Lambda:
s=lambda x,y,z:x if(x>10) else (y if x>z else z)
print(s(10,20,30))

Talked about map() and reduce() functions.
================ 41 map function with multiple sequence objects ==========================
done.
Nested functions

================ 42 Decorators ==========================
Decorator function will take some input function and it will produce out put function(with extended functionality)
input function==> decorator==> output function(with extended functionality)
def dec(div):
    def inner(a,b):
        if(a<b):
            a,b=b,a
        div(a,b)
    return inner
@dec
def div(a,b):
    print(a/b)

div(1,10))
---------------------------------------------------------------------------------------------------------
def dec(div):
    def inner(a,b):
        if(a<b):
            a,b=b,a
        div(a,b)
    return inner

def div(a,b):
    print(a/b)

print(div(1,10))
decf=dec(div)     # This is an other way of linking where we can call the individual func and decorator func.
print(decf(1,10))

================ 43,44 Decorators ==========================
# Decorator chaining discussed, I haven't completed.
# Started with generators showed the advantages of time computing and memory utilization with generators.
In the regular collections, when the collection is created it will occupy the sytem memory(RAM) and for large collection values we will see memory error.

l=[x*x for x in range(10)]   # List comprehension
print(l)

t=(t*t for t in range(10))   # No Tuple comprehension, This is generator.
print(t)

for g in t:
    print(g)

================== 45 Generators =========================
Iterators not covered, but learn iterators before jumping into generators.
generator is also a function but it doesn't have return statement rather it will have yield statement.
It will read element by element or record by record.
It's mainly used for reading large files and web scrapping.
================== 46 Modules ======================
discussed about dir() function and points included in main notes.
================== 46 Ramdom Module ======================
print(chr(65))     # print the character of the given ascii number.
print(ord('h'))     # print ascii value of the given character.

import random
l=["hyd","chennai","blr","delhi","ooty"]
print(random.randint(1,100))
for x in range(5):
    print(random.choice(l))  # choice will take any index based sequence like list and tuple and not set(set is not an index based)

import random
import string
a=random.choice(string.ascii_lowercase)
b=random.choice(string.ascii_uppercase)
c=random.choice(string.ascii_lowercase)
x=str(random.randint(0,9))
y=str(random.randint(0,9))
z=str(random.randint(0,9))
print(a+b+c+x+y+z)


============= Naveen Reddy OOPS ====================
Class, Object
constructor
class variables/static variables, instance/object variables.
types of methods in class - instance methods (with self as argument), class methods(with cls as argument and @classmethod decorator), static method (with no self & cls arguments and with staticmethod decorator)




 

