#swapping 2 numbers without using a temp variable

a = int(input('enter a num'))
b = int(input('enter a num'))
print('Before : a is %d and b = %d' %(a,b) )
a = a+b
b = a-b
a = a-b
print('now: a is {%d} and b is {%d}' %(a,b))

