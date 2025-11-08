rows = int(input('enter no of rows: '))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()
#alternative sol: pythonic way
s1 = {23, 67}
s2 = {21, 79, 23}
# Cartesian Product using set comprehension
cartesian = {(i, j) for i in s1 for j in s2}
print("Set 1:", s1)
print("Set 2:", s2)
print("Cartesian Product:", cartesian)