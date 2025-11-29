#wap to implement power function using closure
def base(x):
    def pow(y):
        return x**y
    return pow
power_of = base(3)
print(power_of(2))
