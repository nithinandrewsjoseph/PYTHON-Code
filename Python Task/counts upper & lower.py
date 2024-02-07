s="MANgo Juice"
def cnt(s):
    uppercase=0
    lowercase=0
    for x in s:
        if x.isupper():
            uppercase+=1
        elif  x.islower():
            lowercase+=1
    print("upper count",uppercase)
    print("lower count",lowercase)
cnt(s)


            