# Inheritance
every class inherits from a built-in base/mother class  i.e "object". This is how all the magic methods comes into user defined/builtin classes.
https://www.geeksforgeeks.org/python-object-method/

# Code 1

x=object()
print(dir(x))
print(type(x))

# Code 2

 class name(object):  # inheriting from object class which is base class for any class.
   def __init__(self, name):
       self.name = name

 person1 = name("jean")     # passing argument to constructor and not to class; Never class will have arguments only constructor and methods.
 person2 = name("dean")    # passing argument to constructor and not to class.
 person1.name
'jean'
person2.name
'dean'
