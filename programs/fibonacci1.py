#fibonacci series for first 20 elements
l = []
n = 4500
a = 0
b = 1
temp = n
while a<=n:
    print(a, end=' ')
    while len(l)<=20:
        l.append(a)
    a,b = b,b+a
print(l)