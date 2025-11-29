def multiply(x):
    return num_list[0]*num_list[1]
def compute(func,x):
    return func(x)
num_list=[2,3]
product = compute(multiply,num_list)
print("multiplication",product)