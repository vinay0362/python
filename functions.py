def prime(n):
    c=0
    for i in range(2,n//2+1):
        if n%i==0:
            c=c+1
            break

    if(c>0):
        return "is not prime"
    else:
        return "prime"

x=prime(int(input()))
print(x)
