#list comprehension
#every list comprehension can be rewritten as a for loop but every for loop cant be rewritten in list comprehension
#task
'''a=["codegnan","python","course"]
for i in a:
    print(i.upper(),end=",")'''

#syntax
#a=[expr for var in collection/range]

'''a=["codegnan","python","course"]
a=[i.upper() for i in a]
print(a)'''

'''a=[1,2,3,5,6,8,12,13]
a=[i*i for i in a]
a=[pow(i,2) for i in a]
a=[i**2 for i in a]
print(a)'''


'''a=["vja","hyd","vza"]
a=[i.title() for i in a]
print(a)'''


#if usage in list comprehension
'''a=[  b for b in range(21) if b%2==0]
print(a)'''

'''a=[b*b for b in range(21) if b%2==0]
print(a)'''

'''a=["apple","grapes","berry","mango","banana","kiwi"]
a=[i for i in a if "a" in i]
print(a)'''

#no elif usage in list comprehension
#if else usage in list comprehension
'''a=[i*2 if i%2==0 else i*5 for i in range(16) ]
print(a)'''
a=[1,2,3,4,5]
b=[5,4,3,2,1]
#c=[a[i]+b[i] for  i in range(5)]
c=[a[i]+b[i] for i in range(len(a))]
print(c)

