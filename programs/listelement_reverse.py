def extract_second_digit(x):
    return int(str(x)[1])
li = eval(input('enter list : '))
print('list before sorting ', li)
print(min(li,key=extract_second_digit))