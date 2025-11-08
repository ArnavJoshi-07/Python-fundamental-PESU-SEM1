#wap to check difference bw sucessive elements in a list.
n = int(input('enter no of elements in the list : '))
l = []
for i in range(0,n):
    a = int(input('enter number:'))
    l.append(a)

for j in range(0,len(l)-1):
    d = l[j+1]-l[j]
    print(d)
