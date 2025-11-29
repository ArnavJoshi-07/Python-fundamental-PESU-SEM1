def divide(x,y):
    if x==0 or y==0:
        print("Division by 0 not allowed")
    else:
        return 1 + divide(x-y,y)
    
x = int(input('enter number 1 '))
y = int(input('enter number 2 '))
print('result', divide(x,y))
