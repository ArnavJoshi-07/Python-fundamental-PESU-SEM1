#number guessing
import random
import time
c = random.randint(1,10)
for i in range(0,3):
    n = int(input('enter a number between 1 to 10:'))
    a = 3 - (i+1)
    while a!= 0 and n!=c :
        print('you have ' ,a,' tries.' )
        break
    if a == 0:
        print('No tries left, you lose.')
        
    elif n>c and n<10:
        print("Too high, try again.")
        
    elif n<c:
        print('Too low, try again.')
        
    elif n==c:
        print('You win!')
        break
    elif n>10:
        print('Stupid Mistake.')
    time.sleep(3)
    