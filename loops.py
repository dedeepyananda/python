#loops
#for,while,range,break,
#for loop sequence iterator
"""
a=[10,20,30,40,50]
for i in a:
    print(i)
"""    
"""
a=[10,20,30,40,50]
for i in a:
    print(i,end="")
"""
"""
a=[10,20,30,40,50]
for i in a:
    print(a)
    print(i,end=" ")
"""
"""
a=[10,20,30,40,50]
for i in a:
    print(i)
    print(type(a))
    print(type(i))
"""
"""
a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))
"""
"""
a=(10,20,30,40,50)
for i in a:
    print(i)
    print(type(a))
    print(type(i))
"""
"""
a={10,20,30,40,50}
for i in a:
    print(i)
    print(type(a))
    print(type(i))
"""
"""
a={"year":2026,"month":"may","date":16}
for i in a:
    print(i)
    print(type(i))
    print(type(a))
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
    print(type(a))
    print(type(i))
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))
"""
"""
a="codegnan"
for i in a:
    print(i,end=" ")
"""
"""
a=[4.5,6.7]
for i in a:
    print(i)
    print(type(i))
    print(type(a))
"""    
"""
a=[6+2j,6-2j]
for i in a:
    print(i)
    print(type(i))
    print(type(a))
"""
"""
a=[True,False]
for i in a:
    print(i)
    print(type(i))
    print(type(a))
"""
"""
a="code"
for i in a:
    print(i)
    print(type(a))
    print(type(i))
"""
#while loop
#continous iterator
"""
a=10
while a<2:
    print(a)
"""
"""
a=10
while a>1:
    print(a)
"""
"""
a=10
while a>1:
    print(a)
    a=a-1
"""
"""
a=10
while a>=1:
    print(a)
a=a-1
"""
"""
a=10
while a>1:
    a=a-1
    print(a)
"""
"""
a=10
while a>1:
    a=a-1
print(a)
"""
"""
a=20
while a>5:
    print(a)
    a+=3
"""
"""
a=20
while a>5:
    print(a)
    a-=1
"""
"""
a=9
while a<30:
    print(a)
    a+=1
"""
"""
while True:
    age=int(input("enter age"))
    if age<18:
        print("not eligible for vote")
    else:
        print("eligible for vote")
"""
"""
while True:
    n=int(input("enter number"))
    if n%2==0:
        print("n is even number",n)
    else:
        print("n is odd number",n)
"""

#RANGE: the range function returns a sequence of numbers starting from zero by default
#        and increments by one by one and stops before a specified number
# it has start,stop,step
"""
for i in range(15):
    print(i)
"""
"""
for i in range(16):
    print(i)
"""
"""
for i in range(5,20):
    print(i)
"""

#tasks for step
"""
for i in range(0,30,3):
    print(i,end=" ")
"""
"""
for i in range(2,20,2):
    print(i,end=" ")
"""
"""
for i in range(5,50,5):
    print(i,end=" ")
"""
"""
DIFFERENCE BTW BREAK,CONTINUE,PASS:
Break is used to terminate the entire loop
continue statement is used to skip current iteration and rest of code will continue
A pass is a null statement does nothing but syntatically we need
"""
#BREAK--IT MUST HAVE FOR LOOP OR WHILE LOOP TO PERFORM
"""
a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break
"""
"""
a=10
while a>1:
    a=a-1
    if a==5:
        break
    print(a)
"""
"""
for i in range(21):
    if i==14:
        break
    print(i)
"""
"""
a="python"
if a=="h":
    break
print(a)#ERROR
"""
"""
a="python"
for i in a:
    print(i)
"""
"""
a="python"
for i in a:
    if i=="h":
        break
    print(i)
"""
#continue
"""
a=20
while a>5:
    print(a)#the print stmt must always be near condition in continue
    a=a-1
    if a==10:
        continue
"""
"""
a=20
while a>5:
    a=a-1
    if a==10:
        continue
    print(a)
"""
"""
a=20
while a>5:
    a=a-1
    if a==10:
        continue
    print(a)
"""
"""
for i in range(15):
    if i==9:
        continue
    print(i)
"""
"""
a="python"
for i in a:
    if i=="h":
        continue
    print(i)
"""
#pass-example: more like resume button in games or it holds the error
"""
a=25
while a>1:
    print(a)
    a=a-1
    if a==15:
        pass
"""
"""
for i in range(15):
    if i==10:
        pass
    print(i)
"""








