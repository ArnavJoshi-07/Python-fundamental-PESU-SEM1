limit = int(input('enter limit: '))
a = 0
b = 1
while a<=limit:
    print(a, end=" ")
    a,b = b,b+a
    

