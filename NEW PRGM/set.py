# set is represented in curley bracket
a={'apple','orange','mango','apple'}
print(a)
print(len(a))
for i in a:
    print(i)
a.add('banana')
print(a)
b={'ball','bat','ground','apple'}
b.update(a)
print(b)
print(a)
c=['shirt','pant','shoes']
b.update(c)
print(b)
b.remove('bat')
print(b)
b.discard('ball')
print(b)
# b.remove('bat')
#print(b)
b.discard('ball')
print(b)
b.pop()
print(b)
b.clear()
print(b)
# del b
#print(b)
c={'car','bike',18,15,'bus'}
d={'bag','book',18,15,'pen'}
f=c.union(d)
print(f)
c.update(d)
print(c)
g=c.intersection(d)
print(g)
c.intersection_update(d)
print(c)
set1={'apple','orange','grapes'}
set2={'apple','banana','orange'}
set3=set1.difference(set2)
print(set3)
set4={1,2,3,4,5}
set5={1,2}
set6=set4.issubset(set5)
print(set6)
set7=set4.issuperset(set5)
print(set7)
