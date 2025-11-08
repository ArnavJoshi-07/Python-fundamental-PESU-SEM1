"""#wap to input a string and print square of all numbers
i = "1str4abc8"
for ele in i:
    if ele.isnumeric() == True:
        a = int(ele)
        print(a**2)

#wap to take 2 strings and take a cartesian product of both strings
s1 = 'abc'
s2 = 'ab'
l = []
for i in s1:
    for j in s2:
        l.append(f'{i}:{j}')
print(l)"""
#write a func to take a string, swap adjacent characters and make a new string
string = str(input('enter a string'))
l = ""
for i in range(0,len(string)):
    l = l + string[i+1]
    l += string[i]
    i = i+2
print(l)
