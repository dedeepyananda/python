#def
# every list comprehension can be re written as for loop but,every for loop
# cannot be re writen in list comprehension
"""
a=["codegnan","python","course"]
print(str(a).upper())
"""
""""
a=["codegnan","python","course"]
b=str(a)
print(b.upper())
"""
"""
for i in a:
    print(i.upper(),end=" ")"""
#syntax
#a=[expression for var in collection/range]
"""
a=["codegnan","python","course"]
b=[i.upper() for i in a]
print(b)
"""
"""
a=["vij","hyd","vzg"]
b=[i.title() for i in a]
print(b)
"""
"""
a=[2,4,6,7,8,12,13]
b=[i**2 for i in a]
b=[i*i for i in a]
b=[pow(i,2) for i in a]
print(b)
"""
#if usuage in list comprehension
"""
a=[i for i in range(16)]
print(a)
"""
"""
a=[i for i in range(16) if i%2==0]
print(a)
"""
"""
a=[i for i in range(16) if i%2!=0]
print(a)
"""
"""
fruits=["apple","grapes","mango","kiwi","dragon","berry"]
a=[i for i in fruits if "a" in i]
print(a)
"""
"""
fruits=["apple","grapes","mango","kiwi","dragon","berry"]
a=[i for i in fruits if "a" not in i]
print(a)
"""
#no elif usuage in list comprehension
#else ususge in list comprehenson
"""
a=[i**2 if i%2==0 else i*5for i in range(21)]
print(a)
"""
"""
a=[1,2,3,4,5]#[6,6,6,6,6]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(5)]
print(c)
"""
"""
a=[1,2,3,4,5]#[6,6,6,6,6]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]
print(c)
"""
