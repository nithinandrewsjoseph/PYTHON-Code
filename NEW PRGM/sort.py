c=[1,5,7,8,4]
for i in c:
    print(i)
    c.sort()
    print(c)

    c.sort(reverse=True)
    print(c)
    d=c.copy()
    print(d)
    e=list(c)
    print(e)

    f=[1,3,5,7]
    x=f+c
    print(x)

    for i in c:
        f.append(i)
        print(f)

        c.extend(f)
        print(c)
        
        
    


