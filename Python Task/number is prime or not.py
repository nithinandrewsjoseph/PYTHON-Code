a=int(input("enter a number:"))
def pr(b):
    if b==1:
        print("not a prime")
    elif b > 1:
        for i in range(2,b):
            if(b % i==0):
              print("number is not prime")
              break
        else:
            print("number is prime")
    else:
        print("prime number")
pr(a)                   