def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
n = gcd(18,12)
print(n)