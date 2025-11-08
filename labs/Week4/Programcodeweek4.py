'''#for 1 to n if multiple of 3 fizz if 5 buzz if 5 and 3 fizzbuzz
n = int(input('enter a num: ' ))
for i in range(1,n+1):
    if i%15==0:
        print('fizzbuzz')
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print('buzz')
    else:
        print(i)

#Given an integer, reverse its digits. The sign of the number should be preserved.
n = int(input("Enter the input: "))
number = 0
sign = 1

if n < 0:
    sign = -1
    n = abs(n)

while n != 0:
    remainder = n % 10
    number = number * 10 + remainder
    n = n // 10
    
print(number * sign)
 
#find if num is a power of 2

num = int(input('enter a number:'))
if num <= 0:
    print(num, 'is not a power of 2')
elif num == 1: # 2^0
    print(num, '= 2^0')
else:
    n = num
    x = 0
    while n > 1 and n % 2 == 0:
        n = n // 2
        x = x + 1
    if n == 1:
        print(num, '= 2^', x)
    else:
        print(num, 'is not a power of 2')

#Given a positive integer num, write a program that returns True if num is a
#perfect square, and False otherwise without using built in functions.
n = int(input('enter a num: '))
is_perfect_square = False
i = 1
while i * i <= n:
    if i * i == n:
    
        is_perfect_square = True
        break
    i += 1

    

print(is_perfect_square)'''

#Given a maximum number n and a target number, find the first pair of two
#different integers between 1 and n (inclusive) that add up to the target
max = int(input('enter a max: '))
targ = int(input('enter a target: '))
for i in range(2,max+1):
    a = targ - i
    if i in range(1,max+1):
        print(i,a)
        break
    else:
        continue