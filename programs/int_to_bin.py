a = int(input('enter an integer: '))
print(f"type before : {type(a)}")
bin_num = ''
temp = a 
while temp != 0:
    remainder = temp%2
    temp = temp//2
    bin_num = str(remainder) + bin_num
print(f'binary number of {a} is {bin_num} and new type is {type(bin_num)}')