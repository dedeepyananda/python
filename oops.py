#oops
#syntax
"""
class classname():
    name="pooja"
    age=22
    city="vij"
    def fname(method_name):
        print("statements---")
obj=classname()
print(dir(a))
obj.fname()
"""
#class declaration
"""
class Details():#class name
    name="pooja"
    age=22
    city="vij"
    def display(self):#function name
        print(self.name,self.age,self.city)
a=Details()
print(dir(a))
a.display()
"""
#object instantiation
"""
class Details():
    def Data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.Data("dede",18,"vij")
a.display()

b=Details()
print(dir(b))
b.Data=("sophia",22,"vij")
b.display()

c=Details()
print(dir(c))
c.Data=("dedhi",22,"vij")
c.display()
"""
#object initialization:must give values to class
"""
class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("dedeepya",21,"vij")
print(dir(a))
a.display()
"""

"""method-1
class Details():
    def __init__(self):
        self.name=input("enter name")
        self.age=int(input("enter age"))
        self.place=input("enter place")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()
"""
"""Method 2
class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details(input(),int(input()),input())
print(dir(a))
a.display()
"""
