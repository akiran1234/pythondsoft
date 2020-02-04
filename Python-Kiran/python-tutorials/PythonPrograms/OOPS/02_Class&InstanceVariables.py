###########################################################################################################
# A class variable: is a static variable because no instance creation is required and it is bound to class.
# Instance Variables: A variable that is defined inside a method and belongs only to the current instance of a class.
# For each object that is been created a separate copy will be created in memory.
# The scope of the instance variables that's been passed as arguments will be available to all the methods of the class.
# Instance variable will be prefixed with key word "self" and then only it can be available to all the methods and out side of the class.
# Instance Variable are independent of each object and change in once instance variable will not affect other instance variable.
# Instance variable from a method can only be accessible only when that method is called.
###########################################################################################################

class Student:
    def __init__(self,name,rollno,marks): # Implicit Initialization of instance Variables no explicit method call required.
        self.n=name
        self.rollno=rollno
        self.marks=marks
        temp=name

    def display(self):
        print("Displaying from method",self.n,self.rollno,self.marks)
        # print("temp variable",temp)  # temp is not instance variable hence not able to print.

s1=Student('Kiran',501,600)
s1.display()
print("Printing the Instance Var out of the class=",s1.n,s1.rollno,s1.marks,sep=',')
print(s1.__dict__)
###########################################################################################################
# Instance Variable initialization explicitly via method call.
# Here comes constructor method to initialize instance variables with out explicit method call.

class Student:
    def record(self,name,rollno,marks):
        self.n=name
        self.rollno=rollno
        self.marks=marks
        temp=name

    def display(self):
        print("Displaying from method",self.n,self.rollno,self.marks)
        # print("temp variable",temp)  # temp is not instance variable hence not able to print.

s1=Student()                # No initialisation of instance variables.
s1.record("Kiran",501,600)  # Initialisation by calling the method explicitly
print("Printing the Instance Var out of the class=",s1.n,s1.rollno,s1.marks,sep=',')

###########################################################################################################
# Instance Variable are independent of each object and change in once instance variable will not affect other instance variable.

class Test:
    def __init__(self):
        self.x=100

t1=Test()
t2=Test()
print("Before Change:",t1.x,t2.x)
t1.x=200
print("After Change: ",t1.x,t2.x)

###########################################################################################################
# Class variables share the same value across all the instances of the class.
# Change of value in the class variable will reflect across all the instances.
# A class variable is a static variable because no instance creation is required to access those variables.

class Test:
    v1=10
    def __init__(self):
        print("Hello i'm in constructor")

print(Test.v1)  # Class variable can be directly accessed with class name with out instance creation.
t1=Test()
t2=Test()

print("class variable before change from object t1=",t1.v1)
print("class variable before change from object t2=",t2.v1)
Test.v1=20      # Changing the class variable value.

print("class variable After change from object t1=",t1.v1)
print("class variable After change from object t2=",t2.v1)

###########################################################################################################
# Class Variables vs Instance Variables.
# Class variable is meant to have the same value across all the objects.
# Instance variable is meant to have there own value and isolated between each object.
# Instance variables can be used/modified any where across the class methods.

class Test(object):
    x1=100                         # This is a class variable change in the value of class variable would be same across all the instances/objects.
    y1=200                         # This class variables should be accessed using Classname.Variable Name (Test.x1), how ever this can be accessed using object as well (t1.x1)
    def hello(self):
        a=10                       # This is a local variable to only that method and it is not visible to other methods/out side class because "self" key word is not referred.
        self.b=20                  # This is an instance variable and visible to all the methods of that class/outside of the class and can be modified across any method.
        print(f"I am method specific local variable a:{a}")
        print(f"I am instance specific variable b:{self.b}")
        return a+self.b

    def bolo(self):
        print(f"I can access b variable from hello method in bolo method b:{self.b}")
        self.b=200                 # This variable is declared in hello() method and used/modified in bolo() method.
        print(self.b)

# class variable usage analysis.
Test.x1         # Accessing class variable and this is preferred.
t1=Test()       # object t1 created
t1.x1           # Accessing class variable using instance and this is also possible.
t1.x1=99        # Modifying class variable using instance and this value is applicable to only this t1 object and not for other objects. For other objects the value is 100 only.
Test.x1=11      # Changing the class variable value out of the class and this value will be common to all objects of the class. Now for all the objects the x1 value is 11

# object variable/ instance variable analysis.
# Since there is no constructor we have to explicitly invoke hello() method for variable initialization.
t2=Test()
t2.hello()      # Invoked hello()method now the variables have been initialised.
t2.a            # Trying to access local/method specific variable, this will throw an error.
t2.b            # Any instance variable can be used out side the class but that method has to be invoked for initialisation of variable. (Here hello() is invoked before t2.b is used outside of the class.)
t2.b=300        # Changing the instance variable value from outside the class is possible.






