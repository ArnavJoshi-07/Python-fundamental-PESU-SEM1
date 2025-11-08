# create pattern like decending no of columns with increasing rows
s = 'abcd'
for i in range(len(s)):
    print(s[i:])
# create pattern of increasing no of rows with columns consisting of the row number
n = int(input('enter no of rows: '))
for i in range(1,n+1):
    print(str(i)*i)
    #or
rows = int(input('enter no of rows: '))
for i in range(rows+1):
    for j in range(i):
        print(i, end='     ')
    print()