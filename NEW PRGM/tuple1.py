a=(1,2,3,4,5,6)
print(a)

print(len(a))
print(a[0])
print(a[-2])
print(a[1:])
print(a[:5])
print(a[-5:-2])

print(type(a))
print(1 in a)
print(9 in a)

b=list(a)
b[5]="mango"
print(b)
a=tuple(b)
print(a)
for i in a:
    print(i)
d=("lemon","onion")
e=a+d
print(e)
(x,y)=d
print(x)
print(y)
f=a*2
print(f)
g=a.count(5)
print(g)
j=d.index("lemon")
print(j)
# delete del d 
#print(d)

    
