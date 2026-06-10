"""
def greetings(name):
    print("welcome",name)
"""
"""
a=4
b=7
c=a+b
print("the sum:",a+b)
"""
"""
d={"idnos":[10,20,30],
   "names":["charan","harsha","adithya"],
   "marks":[60,70,80]}
"""
"""
if __name__=="__main__":
    a=[10,20,30,40,50]
    a.append("code")
    a.extend("code")
    print(a)

def dummy():
    if __name__=="__main__":#to store dummy files called
        print("script") 
    else:
        print("module")
dummy()
"""
"""#it is a script; if it is module we need to
import from another file example given
"""
#math module
"""
import math
print(math.pi)
print(math.pi*5)
print(math.sqrt(2))
print(math.log(2))
print(math.tan(45))
print(math.sin(30))
print(math.cos(60))
print(math.pow(2,4))
print(math.ceil(5.8))#nxt highest value
print(math.floor(2.9))#lowest value
"""
#sys module--it tells us where python is located in
#system and we can also know its version
"""
import sys
print(sys.path)
for i in sys.path:
    print(i)

print(sys.version)
"""
"""
#os module---module docs to know all things about py
import os
print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.mkdir("june 3"))
"""

#random module
#sample
"""
5numbers will be generated
import random
a=random.sample(range(20,40),5)
print(a)
#donot applyrange with random directly
"""
"""
#randit()--single number
import random
a=random.randint(30,50)
print(a)
"""
"""
#choice---repeated numbers
import random
a=[10,30,50,20,60,70]
b=random.choice(a)
print(b)
"""
#taskk
"""ME
while True:
    n=int(input("enter the roll of dice"))
    import random
    a=random.sample(range(1,7),1)
    print(a)
    choice=int(input("enter the choice 1.enter the game 2.exit the game"))
    if choice==1:
        n=int(input("enter the roll of dice"))
        print(random.sample(range(1,7),1))
        continue
    elif choice==2:
        print("exited")
        break
"""
"""
import random
while True:
    input("enter the roll of dice")
    a=random.randint(1,6)
    print(a)
    option=input("roll dice?(y/n)")
    if option=="y":
        continue
    elif option=="n":
        break
"""
#calendar module
"""
import calendar
year=2026
month=6
print(calendar.month(year,month))
"""
"""
import calendar
year=2026
print(calendar.calendar(year))
"""
"""
import calendar
year=int(input("enter the year"))
month=int(input("enter the month"))
print(calendar.month(year,month))
"""
"""
import calendar
year=int(input("enter the year"))
month=int(input("enter the month"))
print(calendar.month(year,month))
"""
#date and time
"""
from datetime import date
a=date.today()
print(a)
"""
"""
import datetime
a=datetime.datetime.now()
print(a)
"""
#appach timer
"""
import time
a=time.time()
print(a)

b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"today time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")
"""
#task
"""
while True:
    import random
    import time
    a=random.sample(range(10),1)
    for i in a:
        print(a)
        time.sleep(2)
        continue
"""
"""
import random
import time
for i in range(10):
    a=random.randint(1000,9999)
    print(a)
    time.sleep(2)
"""
#REGEX
"""
Regular experssions are powerful tools(module) embedded in python which is mainly used to find a pattern
with in a given string or statements or files and we mainly use it for text manuipulation.
"""
"""
a="codegana"
print(a)

a="codegnan\nis\tin\nvijayawada"
print(a)
"""
#rstring
"""
a=r"codegnan\nis\tin\nvijayawada"
print(a)
"""
#compile(),search(),findall(),split(),sub()
#sequence characters
"""
/w-->it matches alphanumeric
/W-->it matches non-alphanumeric
/d-->matches any digit
/D-->matches non-digit
/s-->it matches white spaces
/S-->it matches non-white spaces
"""
#compile()
import re
a="main mat map cat money cash maths cap cup code monkey"""
"""
b=re.compile(r"m\w\w\w")
print(b)
"""
#search()
"""
c=b.search(a)
print(c)
"""
"""
d=re.search(r"m\w+",a)
print(d)
"""
#find all
"""
d=re.findall(r"m\w+",a)
print(d)
"""
"""
d=re.findall(r"m\w+",a)
print(*d)
"""
#split()
"""
e=re.split(r"m",a)
print(e)
"""
"""
f=re.split(r"\s",a)
print(f)
"""
#sub
"""
x=re.sub(r"maths","science",a)
print(x)
"""
#task
"""
z="1,2,3,4,apple,4,5,6"
y=re.findall("\d",z)
print(y)
"""
"""
z="1,2,3,4,apple,4,5,6"
y=re.findall("\D",z)
print(y)
"""
