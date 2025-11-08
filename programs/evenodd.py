'''lim = int(input('enter a limit'))
i = 0 
even=[]
odd = []
both = []
for i in range(0, lim+1):
    if i%2==0:
        even.append(i)
        both.append(i)
    else:
        odd.append(i)
        both.append(i)
print(f' Even={even} Odd={odd} Both={both}')'''
#wap to calc sum of odd and even btw  2 user given numbers
a = int(input('enter the first number'))
b = int(input('enter the second number: '))
even =[]
odd=[]
both=[]
for i in range(a, b+1):
    if i%2 == 0:
        even.append(i)
        both.append(i)
    else:
        odd.append(i)
        both.append(i)
m = 0
for n in even:
    m = m+n
q=0
for p in odd:
    q = q+p
print(f'sum of even is {m}(type = {type(even)} id = {id(even)}) and sum of odd is {q}(type={type(odd)} id = {id(odd)})')
