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
