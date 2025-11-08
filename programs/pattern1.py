# 1 13 135 1357 in diff lines
rows = int(input('enter no of rows: '))
for i in range(1,rows+1):
    for j in range(0,i):
        print(2*j+1, end=' ')
    print()