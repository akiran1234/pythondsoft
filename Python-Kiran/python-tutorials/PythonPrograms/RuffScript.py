class Const(object):

    def method1(self):
        print("I am in method1")
        print(f"I am using instance variables:a={self.a} and b={self.b}")
        self.x=501

    def method2(self):
        print("I am in method2")

    def __init__(self):      # As a best coding practise define at top of the class
        print("I am constructor i will be invoked for object creation")
        print("I am meant for initialing instance variables")
        self.a=100
        self.b=200

c=Const()
c.method1()
print(c.x)