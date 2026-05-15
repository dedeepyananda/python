#tuple-------------immutable------
a=(5,6.7,"pooja",4+9j,True,False)
print(a)
type(a)
#length
len(a)
#count
a.count(True)
#index()
a.index(4+9j)
#sets-------------semi-mutable----
a={3,5.7,"python",8+9j,True,False}
print(a)
a={1,2,3,4,5,6,7}
a.add(10)
print(a)
#issubset----part of superset
a={1,2,3,4,5,6}
b={4,5,6}
b.issubset(a)

a.issubset(b)

#issuperset
a={1,2,3,4,5,6}
b={1,2,3,8}
a.issuperset(b)
#union
a.union(b)
#intersection()
a={2,3,4,5,6,7,8}
b={1,5,7,9,8,10}
a.intersection(b)
print(a)
#update----difference btw union and update is in update it upadtes the set but in union it doesnt update the set
a={10,11,12,13,14}
b={13,14,15,16,17,30}
a.update(b)
print(a)
b.update(a)
print(b)
#difference
a={2,3,4,5,6,7,8}
b={7,,9,10,11,12}
a.difference(b)
b.difference(a)
#symmetric difference
a={2,3,4,5,6,7,8}
b={1,5,6,7,8,9,10}
a.symmetric_difference(b)
print(a)
b.symmetric_difference(a)
print(b)
#difference update
a={6,7,8,9,10}
b={1,3,5,6,7,8}
a.difference_update(b)
print(a)
b.difference_update(a)
print(b)
#symmetric_difference_update
a={3,4,5,6,7,8}
b={6,7,8,9,10,11}
a.symmetric_difference_update(b)
print(a)
b.symmetric_difference_update(a)
print(b)
#intersetion_update
a={10,20,30,40,50,60}
b={40,50,60,70,80,90}
a.intersection_update(b)
print(a)
b.intersection_update(a)
print(b)
#pop---starting element deletes
a={6,7,8,9,10,11,12,13}
a.pop()
a.pop(9)
#---error---
#remove
a.remove(11)
print(a)
#discard
a={5,6,7,8,9}
a.discard(9)
print(a)
#index----since set is unordered it doesnt have any index
a.index(2)
#count-----no repeated ele
a.count(8)
#isdisjoint()
a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
a.isdisjoint(b)
#false
a={1,2,3,4}
b={5,6,7,8}
a.isdisjoint(a)
#clear()
a={5,6,7,8,9}
a.clear()
print(a)
b=set()
b.add(10)
print(b)







