original_n = int(input("Enter an integer to check if it's a power of two: "))
n = original_n
exponent = 0

if n <= 0:
    is_power = False
else:
    # A number is a power of two if it can be repeatedly divided by 2 until it becomes 1.
    while n > 1 and n % 2 == 0:
        n //= 2
        exponent += 1
    is_power = (n == 1)

if is_power:
    print(f"{original_n} is a power of two (2^{exponent}).")
else:
    print(f"{original_n} is not a power of two.")
