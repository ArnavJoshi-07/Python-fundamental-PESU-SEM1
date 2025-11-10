def TowerOfHanoi(n,src,aux,dest):
    if n==1:
        print("Move disk 1 from source ",src," to destination ",dest)
        return
    TowerOfHanoi(n-1,src,dest,aux)
    print("Move disk ",n,'from source ',src,'to destination',dest)
    TowerOfHanoi(n-1,aux,src,dest)
n = int(input('enter no of disks \n'))
TowerOfHanoi(n,'A','B','C')

