#tuple is unmutable
a=['apple',5,6,7]
print(a)
print(len(a))

b=("hello",)
print(type(b))
c=tuple(("hi", "hello"))
print(c)

print(c[0])
print(c[-1])
print(a[1:4])
print(a[:3])
print(a[1:])
print(a[-4:-1])
print("apple" in a)
print(9 in a)
d=list(a)
d[0]="grapes"
print(d)
a=tuple(d)
print(a)
e=("ginger","lemon","grapes")#packing
(x,y,z)=e
print(x,y,z)#un packing

for i in e:
    print(i)
    f=e+a
    print(f)
    k=e*2
    print(k)
    g=(1,3,7,8,3,1,2,3)
    h=g.count(3)
    print(h)
    i=g.index(3)
    print(i)
    del a
    print(d)

