
def gcd (x,y):
    res=x
    if y!=0:
        return gcd (y,x%y)
    return res
a,b=[int(i) for i in input().split()]
print(gcd(a,b))
