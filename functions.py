"""-----------------------------------------Functions---------------------------------------------------------
1.A function is a block of organized,reasuabe code and that is used to perform a
single or multiple tasks
2.python gives in-build like print,you can make your own function also and these are
called user defined functions
3.function block begin with keyword "def" followed by function name and paranthesis
"""
"""
a=10
b=20
print("the sum is",a+b)
print("the product is",a*b)
print("the diff is ",a-b)

a=100
b=200
print("the sum is",a+b)
print("the product is",a*b)
print("the diff is ",a-b)

a=1000
b=2000
print("the sum is",a+b)
print("the product is",a*b)
print("the diff is ",a-b)

"""
"""
def calculate(a,b):
    print("the sum is",a+b)
    print("the product is",a*b)
    print("the diff is ",a-b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)
"""

"""
def calculate(a,b):
    print("the integer division",a//b)
    print("the modulous division",a%b)
    print("the power is ",a**b)
calculate(10,20)
calculate(1,2)
calculate(4,2)
"""
"""
def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
add()
"""
"""
def fullname():
    a=input("first name")
    b=input("last name")
    print((a+" "+b).title())
fullname()
"""
#tasks
"""
def maths():
    while True:
        a=int(input("a "))
        b=int(input("b "))
        n=int(input("enter choice 1.add 2.sub 3.mul"))
        if n==1:
            print("ADD:",a+b)
        elif n==2:
            print("SUB:",a-b)
        elif n==3:
            print("mul:",a*b)
        else:
            print("enter valid choice")
maths()
"""
"""
while True:
    a=int(input())
    b=int(input())
    n=int(input("enter choice 1.add 2.mul 3.sub"))
    def add():
        print("ADD",a+b)
    def mul():
        print("MUL",a*b)
    def sub():
        print("sub",a-b)
    def maths():
        if n==1:
            add()
        elif n==2:
            mul()
        elif n==3:
            sub()
        else:
            print("not correct choice")
    maths()
"""
"""-------------------------we can also write functions first-------------------------------------------------
def add():
    print("ADD",a+b)
def mul():
    print("MUL",a*b)
def sub():
    print("sub",a-b)
while True:
    a=int(input())
    b=int(input())
    n=int(input("enter choice 1.add 2.mul 3.sub"))
    if n==1:
        add()
    elif n==2:
        mul()
    elif n==3:
        sub()
    else:
        print("not correct choice")

"""

#print vs return
"""
print:it just shows the human user output in a console
return:it is used to terminate the function and gives back the value from the function
"""
"""
def add(a,b):
    print(a+b)
add(2,3)
"""
"""
def add(a,b):
    return a+b#no output 
add(2,3)
"""
"""
def add(a,b):
    return a+b
print(add(2,3))
"""
"""
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(4,5)
"""
"""
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c
    return d
    return e
print(cal(4,5))
"""
"""
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    return d
    return e
print(cal(4,5))
"""
"""
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    return e
print(cal(4,5))
"""
"""
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
print(cal(4,5))
"""
#keyword and positional arguments
"""
def details(id,name,mailid):
    id=10
    name="pooja"
    mailid="pooja@gmail.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
"""
"""
def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
#1
details(id=20,name="sophia",mailid="s@gmail.com")
#2
details(id=30,name="dedeepya",mailid="d@gmail.com")
#3
details(40,"pooja","p@gmail.com")-------------directly given
#4
details("akhi",50,"a@gmail.com")--------------positional args not given
#5
details(mailid="m@gmail.com",id=60,name="mounika")-----------positional args given
"""
#default arguments
"""
def grocery(item,price):
    print("item is %s"%item)             
    print("price is %d"%price)
grocery("sugar",100)
"""
"""
def grocery(item="rice",price=1500):
    print("item is %s"%item)
    print("price is %d"%price)
grocery()
"""
"""
def grocery(item,price=200):
    print("item is %s"%item)
    print("price is %d",price)
grocery("dhal")
"""
"""
def grocery(item="oil",price):
    #A non-default arg doent follow default arg
    print("item is %s"%item)
    print("price is %d"%price)
grocery(140)
"""

#1
"""
def bakery(cake,price,quantity):
    print("cake_name is %s"%cake)
    print("price is %d"%price)
    print("quantity: %d"%quantity)
bakery("black current",2000,1)
"""
#2
"""
def bakery(cake="black forest",price=1000,quantity=1):
    print("cake_name is %s"%cake)
    print("price is %d"%price)
    print("quantity: %d"%quantity)
bakery()
"""
#3
"""
def bakery(cake,price=1000,quantity=2):
    print("cake_name is %s"%cake)
    print("price is %d"%price)
    print("quantity: %d"%quantity)
bakery("butter scotch")
"""
#4
"""
def bakery(cake="vanila",price,quantity):
     #A non-default arg doent follow default arg
    print("cake_name is %s"%cake)
    print("price is %d"%price)
    print("quantity: %d"%quantity)
bakery(100,1)
"""

#task
"""
def split_bill():
    a=int(input())
    b=int(input())
    c=b//a
    print("perhead bill is {}".format(c))
    print(f"perhead bill is {c}")
split_bill()
"""
"""
def split_bill():
    a=int(input())
    b=int(input())
    print("perhead bill is",b//a)
split_bill()
"""
"""
def split_bill():
    a=int(input())
    b=int(input())
    c=b//a
    print("perhead bill is {}".format(b//a))
    print(f"perhead bill is {b//a}")
split_bill()
"""
#*arguments : It is used to unpack the elements and it is also used to attain multiple values(tuple)
"""
a=[1,2,3,4]
print(a)
print(*a)

a=(1,2,3,4,5,6)
print(a)
print(*a)

a={1,2,3,4}
print(a)
print(*a)

a={"year":2026,"name":"pooja"}
print(a)
print(*a)

a="codegnan"
print(a)
print(*a)
"""
"""
a,b,c="codegnan"
print(a)
print(b)
print(c)#error
"""
"""
a,b,c="cod"
print(a)
print(b)
print(c)
"""
"""
a,b,c=2,3,4
print(a)
print(b)
print(c)
"""
"""
a,b,c=2,3,4,5,6
print(a)
print(b)#error
print(c)
"""
"""
a,b,c=2,3,4,5,6,7,8
print(*a)
print(b)
print(c)
"""

#variable length args
#kwargs(**)



#global and local variables
"""
variables inside and outside tthe function is called global and local variables
a variable define above the function and is accesible to the entire global space is called global variable
a varible inside the function is called local variable
"""
#first case of global variables
"""
a=2
def check1():
    print("a value is",a)
check1()
print("a value is",a)
"""

#second case of global variables
"""
a=3
def check2():
    a=5
    a=a**2
    print("inside value is ",a)
check2()
print("outside value is",a)
"""

#third case of global variables and local variables
"""
a=4
def check3():
    a=6
    print("a value is",a)
    a=10
    print("a value is",a+5)
    b=12#local variable
    b=b+a
    print("b value is ",b)
check3()
print("a value is ",a)
print("b value is ",b)#error because it is local variable
"""
#usuage of global keyword
"""
when user wants to access the global variable inside the function directly and carry forward the updated value
even outside the function then we need  to use "global" keyword.
"""
"""
a=4
def final():
    global a,b
    print("inside value is ",a)
    a=15
    print("updated value is",a)
    #global b
    b=20
    b=b+a
    print("b value is ",b)
final()
print("value of a is",a)
print("value of b is ",b)
"""

#ASCII(AMERICAN STANDARD CODE FOR INFO EXCHANGE

#task
#A-Z
"""
for i in range(65,91):
    print(chr(i),end=" ")
"""
#a-z
"""
for i in range(97,123):
    print(chr(i),end=" ")
"""
"""
n="dedeepya"
for chr in n:
    print(ord(chr),end=" ")
"""
"""
name=input("enter the name")
for i in name:
    print(i,"-",ord(i))
"""

#generators:
#generators:" A generator is also a function which can be used as an iterator(loop) by producing group of values
#where we are using "yield" keyword.

"""
a=[i for i in range(16)]
print(a)
print(type(a))
"""
"""
a=(i for i in range(16))
print(a)
print(type(a))#to print all the elements we must use*
"""
"""
a=(i for i in range(16))
print(*a)
print(type(a))
"""
"""
a=(i for i in range(16))
print(list(a))
print(tuple(a))
print(set(a))
"""
#yeild vs return
"""
return: can terminate the func whereas in 
yeild : yeild can pass the function ang go on with every succesive iteration
"""
"""
a,b=[int(x) for x in input("enter the value").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))
"""
"""
a,b=[int(x) for x in input("enter the value").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))
"""
#"yeild vs return"
"""
def mygen():
   # return "python"
   # return "java"
    #return "DSA"
    return "pyhton","java","dsa"
print(mygen())
"""
"""
def mygen():
    yield "vja"
    yield "vzg"
    yield "hyd"
print(*mygen())

#next: it is used to print in line 
d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
"""
"""
#max
print(max(4,5,6,7,8,9,10,20))
#min
print(min(4,5,6,7,8,9,10,20))
#sum:must no give directly we must store values in variables
a=4,5,6,7,8,9,10,20
print(sum(a))
"""

#built-in-functions
"""
print(dir())
print(dir("__builtins--"))
"""
#fromkeys: only used in from keys
"""
a="codegnan"
print(a)
print(str(a))
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))#here we get error to remove this error we use from keys
b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"pooja")
print(b)

b["o"]="python"
print(b)
"""
#eval:takes any data type
"""
while True:
    a=int(input())
    b=int(input())
    print(a+b)
"""
"""
while True:
    a=float(input())
    b=float(input())
    print(a+b)
"""
"""
while True:
    a=str(input())
    b=str(input())
    print(a+b)
"""
"""
while True:
    a=eval(input())
    b=eval(input())
    print(a+b)
"""
#zip-> we can combine multiple collections into one
"""
a=[10,20,30,40,50]
names=['a','b','c','d','e']
print(a+names)

b=zip(a,names)
print(b)

b=list(zip(a,names))
print(b)

b=tuple(zip(a,names))
print(b)


b=set(zip(a,names))
print(b)


b=dict(zip(a,names))
print(b)
"""
#enumerate()#we can give counter to the collection
names=["hasini","srinidhi","sophia","akaanksha","nakshtra"]
"""
for i in range(len(names)):
    print(i,names[i])
"""
"""
b=list(enumerate(names))
print(b)


b=tuple(enumerate(names))
print(b)

b=set(enumerate(names))
print(b)

b=dict(enumerate(names))
print(b)
"""
#annonymous functions(nameless function or lambda function)
#def: annonymous functions are nameless functions and we use keyword called as lambda to create functions

#problem
"""
def calculate():
    x=int(input())
    a=2*x+5
    print(a)
calculate()
"""
#by using lambda
#syntax: a=lambda arg:expression
"""
a=lambda x:2*x+5
print(a(5))

a=int(input())
b=lambda x:2*x+5
print(b(a))
"""

#task
"""
a="codegnan"
b=lambda a:a.upper()
print(b(a))


a="python course"
b=lambda a:a.title()
print(b(a))

a=input()
b=lambda a:a.upper()
print(b(a))

a=input()
b=lambda a:a.title()
print(b(a))
"""
"""
a=input()
b=input()
c=lambda a,b:a+b
print(c(a,b))
"""
"""
a,b=input("enter names").split(",")
c=lambda a,b:(a+" "+b).title()
print(c(a,b))
"""
"""
a,b=[str(x) for x in input("enter names").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))
"""
"""
#filter
a=[]
print(type(a))
b={}
print(type(b))
c=()
print(type(c))
d=set()
print(type(d))
"""
"""
a=[3,6,8,10,15,20,40,60,100]
if a%2==0:
    print(a)#error
"""
"""
a=[3,6,8,10,20,40,60,100]
for i in a:
    if i%2==0:
        print(i)

"""
"""
b=list(filter(lambda i:i%2==0,a))
print(b)
"""
"""
b=[[],(),{}," ",5,9.0,"python",7+9j,True,False]
c=list(filter(None,b))
print(c)
"""

#map->each object from collection and forms a new collection
"""
a=[20,40,50,5,8,9,30,60]
b=[2,4,6,8,18,25,40,45,60]
c=list(map(max,a,b))
print(c)


a=[20,40,50,5,8,9,30,60]
b=[2,4,6,8,18,25,40,45,60]
c=list(map(min,a,b))
print(c)

a=int(input())
b=int(input())
print(a+b)

a,b=int(input()).split(",")
print(a+b)#erroe
"""
"""
a,b=[int(x) for x in input("enter the values").split(",")]
print(a+b)
"""
"""
a,b=map(int,input("enter").split(","))
print(a+b)
"""
"""
a=input("data1")
b=input("data2")
print(a+b)
"""
"""
a,b=input("enter names").split(",")
print(a+b)
"""
"""
a,b=[x for x in input("names").split(",")]
print(a+b)
"""
"""
a,b=[str,input("names").split(",")]
print(a+b)

a=list(map(int,input("enter names").split(",")))
print(a)
"""
"""
a=tuple(map(int,input("enter").split(",")))
print(a)
"""
"""
a=set(map(int,input("enter").split(",")))
print(a)

a=list(map(str,input("enter").split(",")))
print(a)

a=tuple(map(eval,input("enter").split(",")))
print(a)
"""
"""
a=dict.fromkeys(input("enter").split(","))
print(a)
"""


#difference between  module,lib and package
"""
module: A module is a single python file consists
python code.
2.typically consists of fun,classes ,attributes and variables that
    can be used in other python sripts or programs
3.examples of modules into math.py,random.py or
mymodule.py

package:it is a directory contains one or more py modules
__init.py
the init.py file can be contains initization code
of package or empty
eg of packages numpy,pandas,jambo

library:librarys can consists of multiple modules and
packages,organized to solve a particular purpose or
domine
eg: of lib such as requeses,numpy,pandas and matplotlib

#note:every python file is a module and import is a keyword
and every py file saved in    variable name as __main__

A module is a single file of code,
a package is a directory containing multiple modules,
a library is a broader collection of packages designed to provide specific functionality.

"""
#random module
#regex          ------------>IN mymodule
#time date

#ERROR HANDLING
"""
syntax error-->compile error
run_time error-->during execution time
logical error-->error in logic (it cant be visible)
"""
#syntax error
"""
for i in range(10)
print(i)
"""
#run time error
"""
a=int(input())
b=int(input())
print(a//b)
"""
#logical error
"""
a=10
b=20
if a<b:
    print(True)
"""
#exception handling error
"""try:instructions from which we are expecting the exceptions
except:exception is raised in try block it will be handle by this block
else:optional(no exceptions)
finally:always
"""
"""
while True:
    a=int(input())
    b=int(input())
    try:
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptional error")
    finally:
        print("program ended...")
"""




