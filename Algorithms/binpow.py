

def binpow (a,n):
    if n==0:
        return 1
    if (n%2==1):
        return binpow(a,n-1)*a
    else:
        return binpow(a,n/2)*binpow(a,n/2)

a,n=[int(i) for i in input().split()]
print(binpow(a,n))
