#program to calc slope
x1 = int(input("enter x-axis point 1: "))
y1 = int(input("enter y-axis point 1: "))
x2 = int(input("enter x-axis point 2: "))
y2 = int(input("enter y-axis point 2: "))
if x2!=x1:
    s = (y2 - y1)/(x2 - x1)
    print("Slope of line is ",s)
else:
    print("Division by zero not allowed")

#wap to take 2 ints and print sqroot of their sums
import math
a = int(input("enter a number"))
b = int(input("Enter another num"))
s = a^2 + b^2
c = round(math.sqrt(s),2)
print(c)

#wap to input dob and display no of days lived
from datetime import datetime
d = int(input("Enter day of birth"))
m = int(input("Enter month of birth"))
y = int(input("Enter year of birth"))
dmy = datetime(y,m,d)
dn = datetime.now()
s = (dn - dmy).days
print(s)

#wap to gpa
import random
a = round(random.uniform(0,100),2)
b = round(random.uniform(0,100),2)
c = round(random.uniform(0,100),2)
d = round(random.uniform(0,100),2)
e = round(random.uniform(0,100),2)
gpa = ((a+b+c+d+e)/5)/10
Gpa = round(gpa,2)
avg = round((a+b+c+d+e)/5,2)
print("Student: XYZ")
print("Mathematics: ",a)
print("Physics: ",b)
print("Chemistry: ",c)
print("English: ",d)
print("Computer Science: ", e)
print("Average Marks: ", avg)
print("GPA: ",Gpa)


#wap to show calendar of a month and year

import calendar
year = int(input("enter a year: "))
month = int(input("enter a month: "))
print(calendar.month(year, month))

#wap to do physics
u = float(input('enter initial velocity: '))
a = float(input('enter acceleration: '))
t = float(input("enter time"))
v = u + a*t
s = u*t + (1/2)*a*t
print("Final Velocity : ", v ,"m/s")
print("Distance travelled : ", s,"m")



