def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)
def calc(x,y,op):
    op(x,y)
op = input('enter operation(add,sub,multiply,divide)')
if 'add' in op:
    x= int(input('enter number 1 '))
    y= int(input('enter no 2: '))
    calc(x,y,op)
elif 'sub' in op:
    x= int(input('enter number 1 '))
    y= int(input('enter no 2: '))
    calc(x,y,op)
elif 'multiply' in op:
    x= int(input('enter number 1 '))
    y= int(input('enter no 2: '))
    calc(x,y,op)
elif 'divide' in op:
    x= int(input('enter number 1 '))
    y= int(input('enter no 2: '))
    calc(x,y,op)