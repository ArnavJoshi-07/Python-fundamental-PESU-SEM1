#wap to find lcm of 2 numbers using loop and comparison operatorsd

a = int(input('enter a number: '))
b = int(input('enter another number: '))
greater = max(a,b)
while True:
    if greater%a == 0 and greater%b == 0: #finding the greater number among the 2 of them and then incrementing it until its divisible by both the numbers
        lcm = greater
        break
    greater+= max(a,b)
print(f'LCM of {a} & {b} = {lcm}')
    