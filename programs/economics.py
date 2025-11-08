#wap to calc total cost of a user based on quantity purchased, applying a 10% discount if the cost exceeds 1000 and 15% if it exceeds 2000. One unit costs 100

quan = int(input("enter no of units purchased: "))
a = 100
if a*quan in range(1000,2001):
    print(f'Total cost is {a*quan*0.9}(10% discount applied)')
elif a*quan>2000:
    print(f'Total cost is {a*quan*0.8}(20% discount applied)')
else:
    print(f'total cost is {a*quan} (0 discount)')