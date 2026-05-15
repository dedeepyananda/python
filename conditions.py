#conditions
#if-conditions by using comparision operators
#<,>,<=,>=,==,!=
"""
a=2
b=4
if a<b:
    print("true")
"""
"""
a=3
b=7
if a<b:
    print("true")
"""
"""
a=2
b=4
if a<=b:
    print("true")
"""
"""
a=10
b=20
if a>=b:
    print("true")
"""
"""
a=6
b=12
if a!=b:
    print("not equal")
"""
"""
a=2
b=4
if a==b:
    print("true")
"""
"""
a=4
b=4
if a==b:
    print("true")
"""
"""
a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")
"""
"""
a=int(input("a value"))
if a<10:
    print("less")
"""
"""
a="python"
if a=="python":
    print("true")
"""
"""
a=input("data")
if a=="ds":
    print("match")
"""
#if condition by using logical operators and,or,not
"""
a=4
b=8
if a<b and b>a:
    print("true")
"""
"""
a=4
b=8
if a<=b and b>=a:
    print("true")
"""
"""
a=4
b=8
if a!=b and b==a:
    print("true")   
"""
"""
a=5
b=10
if a<=b or b>=a:
    print("true")
"""
"""
a=4
b=8
if a<b or b<a:
    print("true")
"""
"""
a=3
b=6
if not a<b:
    print("true")
"""
"""
a=3
b=6
if not a>b:
    print("true")
"""
"""
a=3
b=6
if not a<b and b>a:
    print("true")

"""
"""
a=int(input("a value"))
b=int(input("b value"))
if a<b and b>a:
    print("less")
"""
"""
a=input("data1")
b=input("data2")
if a==b:
    print("true")
"""
#if-condition using identify operators(is,is not)
"""
a=4
if type(a) is int:
    print("it is int")
"""
"""
a=10
if type(a) is not int:
    print("true")
"""
"""
a=int(input("value"))
if type(a) is int:
    print("true")
"""
"""
a=int(input("value"))
if type(a) is not int:
    print("false")
"""
"""
a=float(input("value"))
if type(a) is float:
    print("true")
"""
"""
a=input("data")
if type(a) is str:
    print("true")
"""
#if-condition using membership(in,not in)
"""
a=[2,3,4,5,6,7,8]
if 8 in a:
    print("true")
"""
"""
a=[2,3,4,5,6,7,8]
if 8 not in a:
    print("true")
"""
"""
a=int(input("a value"))
if 10 in a:
    print("true")#error
"""
"""
a=[2,3,4,5,6,7]
b=int(input("a value"))
if 6 in a:
    print("true")
"""#------------------------------------------------------------------------------------------------------------
#if-else condition using comparision operators
"""
a=2
b=7
if a<b:
    print("true")
else:
    print("false")
"""
"""
a=6
b=7
if a<b:
    print("true")
else:
    print("false")
"""
"""
a=2
b=7
if a>b:
    print("true")
else:
    print("false")
"""
"""
a=11
b=10
if a>b:
    print("true")
else:
    print("false")
    """
"""
a=5
b=9
if a<=b:
    print("true")
else:
    print("false")
"""
"""
a=15
b=9
if a<=b:
    print("true")
else:
    print("false")
"""
"""
a=5
b=9
if a>=b:
    print("true")
else:
    print("false")
"""
"""
a=18
b=9
if a>=b:
    print("true")
else:
    print("false")

"""
"""
a=5
b=10
if a==b:
    print("true")
else:
    print("false")
"""
"""
a=5
b=5
if a==b:
    print("true")
else:
    print("false")
"""
#if else condition by using logical operators and,or,not
"""
a=4
b=8
if a<b and b>a:
    print("true")
else:
    print("false")
"""
"""
a=4
b=8
if a<=b and b>=a:
    print("true")
else:
    print("false")
"""
"""
a=4
b=8
if a!=b and b==a:
    print("true")
else:
    print("false")
"""
"""
a=5
b=10
if a<=b or b>=a:
    print("true")
else:
    print("false")
"""
"""
a=4
b=8
if a<b or b<a:
    print("true")
"""
"""
a=3
b=6
if not a<b:
    print("true")
else:
    print("false")
"""
"""
a=3
b=6
if not a>b:
    print("true")
else:
    print("false")
"""
"""
a=3
b=6
if not a<b and b>a:
    print("true")
else:
    print("false")
"""
#if-else condition using identify operators(is,is not)
"""
a=4
if type(a) is int:
    print("it is int")
else:
    print("not int")
"""
"""
a=10
if type(a) is not int:
    print("true")
else:
    print("false")
"""
"""
a=int(input("value"))
if type(a) is int:
    print("true")
else:
    print("false")
"""
"""
a=int(input("value"))
if type(a) is not int:
    print("false")
else:
    print("true")
"""

#if-else condition using membership(in,not in)
"""
a=[2,3,4,5,6,7,8]
if 8 in a:
    print("true")
else:
    print("false")
"""
"""
a=[2,3,4,5,6,7,8]
if 8 not in a:
    print("true")
else:
    print("false")
"""#---------------------------------------------------------------------------------------------------------
#if-elif-else
"""
a=5
b=10
if a>b:
    print("greater")
elif a<b:
    print("less")
else:
    print("true")
"""
"""
a=5
b=10
if a>b:
    print("greater")
elif a==b:
    print("equal")
else:
    print("true")
"""
"""
a=5
b=10
if a>b:
    print("greater")
elif a==b:
    print("equal")
elif a!=b:
    print("not equal")
else:
    print("true")
"""
#if-elif-else using logical operator
"""
a=5
b=10
if not a<b and b>a:
    print("true")
elif a!=b or b!=a:
    print("not equal numbers")
elif a<b and b>a:
    print("a is greater")
else:
    print("b is greater")
"""
#if-elif-else using identify operator
"""
a=4
if type(a) is int:
    print("it is int")
elif type(a) is not int:
    print("not int")
else:
    print("another")
"""

"""
a=10
if type(a) is not int:
    print("true")
elif type(a) is int:
    print("false")
else:
    print("other data type")
"""
#if-elif-else using membership operator
"""
a=[2,3,4,5,6,7,8]
if 8 in a:
    print("true")
elif 8 not in a:
    print("false")
else:
    print("not present")
"""
"""
a=["apple","banana","orange"]
if "apple" in a:
    print("apple is present")
elif "banana" in a:
    print("banana is present")
else:
    print("a is not set of fruits")
"""
#--------------------------------------------------------------------------------------------------------------
#multiple-if
#we use multilple if when we need to check all conditions at a time
"""
a=7
b=9
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")
"""
"""
a=7
b=9
if a==b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")
"""
#multiple-if using logical operator(and,or,not)
"""
a=7
b=8
if a<b and a!=b:
    print("a is greater")
if b<a or b!=a:
    print("b is greater")
if not a==b and b==a:
    print("not equal numbers")
"""
#multiple-if using identify operator(is,is not)
"""
a=5
if type(a) is int:
    print("it is integer")
if type(a) is not int:
    print("not interger")
"""
#multiple-if using membership operator
"""
a=[1,2,3,4]
b=[4,6,7,8,9]
if 9 in a:
    print("4 is present in a not in b")
if 9 not in a:
    print("9 is present in b")
"""
#------------------------------------------------------------------------------------------------------------
#nested-if
"""
a=4
b=9
if a<b:
    print("less")
    if b>a:
        print("greater")
"""
"""
a=4
b=9
if a>b:
    print("less")
    if b>a:
        print("greater")
"""
"""
a=4
b=9
if a<b:
    print("less")
    if b>a:
        print("greater")
    elif b>a:
        print("true")
"""
"""
a=6
b=12
if a<b:
    print("less")
    if b==a:
        print("greater")
    else:
        print("false")
"""
"""
a=2
b=4
if a>b:
    print("less")
    if b>a:
        print("greater")
else:
    print("true")
"""

a=6
b=10
if a==b:
    print("less")
    if b<a:
        print("greater")
    else:
        print("false")
else:
    print("true")
    
