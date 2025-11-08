import csv

"""def bringtostart():
	f.seek(0)
	next(rea)
	
f = open(r'C:\\Users\\apurv\\VSC\\Python\\labs\\programcodeweek7\\pythonlab.csv','r')
rea = csv.reader(f)
next(rea)
bringtostart()

#pgm 2
f = open(r'C:\\Users\\apurv\\VSC\\Python\\labs\\programcodeweek7\\pythonlab.csv','r')
rea = csv.reader(f)
next(rea)
count = 0
for line in rea:
	# print(line)
	count+=1
print('total num of employees: ',count)

# pgm 3
f = open(r'C:\\Users\\apurv\\VSC\\Python\\labs\\programcodeweek7\\pythonlab.csv','r')
rea = csv.reader(f)
f.seek(0)
next(rea)

for line in rea:
	print(line[0] , line[3])
	


#pgm 4
f = open(r'C:\\Users\\apurv\\VSC\\Python\\labs\\programcodeweek7\\pythonlab.csv','r')
rea = csv.reader(f)
f.seek(0)
next(rea)
count = 0
for line in rea:
	if int(line[4])>50000:
		print(line[0],line[4])
		count += 1
print('num of employees sal greater than 50k:',count)


#pgm 5
dic = {}
f = open(r'C:\\Users\\apurv\\VSC\\Python\\labs\\programcodeweek7\\pythonlab.csv','r')
rea = csv.reader(f)
f.seek(0)
next(rea)

for line in rea:
	if line[1] in dic:
		dic[line[1]] += 1
	else:
		dic[line[1]] = 1
for i in dic.items():
	print(i)

# pgm 6
f = open(r'C:\\Users\\apurv\\VSC\\Python\\labs\\programcodeweek7\\pythonlab.csv','r')
rea = csv.reader(f)
f.seek(0)
next(rea)
salary = []
for line in rea:
	salary += [line[4]]
max_sal = max(salary)


for line in rea:
	if line[4] == max_sal:
		print('highest paid employee',line[0])
		print('details:',line)

#pgm 7
f = open(r'C:\\Users\\apurv\\VSC\\Python\\labs\\programcodeweek7\\pythonlab.csv','r')
rea = csv.reader(f)
f.seek(0)
next(rea)
f1 = open('names.txt','w')
for line in rea:
	f1.write(line[0]+'\n')
f1.close()


# pgm 8
f = open(r'C:\\Users\\apurv\\VSC\\Python\\labs\\programcodeweek7\\pythonlab.csv','r')
rea = csv.reader(f)
f.seek(0)
next(rea)
f2 = open('before1990.txt','w')
for line in rea:
	
	if line[2][6:] < '1990':
		f2.write(str(line)+'\n')
#f2.close()



# pgm 9
salary = []
f = open(r'C:\\Users\\apurv\\VSC\\Python\\labs\\programcodeweek7\\pythonlab.csv','r')
rea = csv.reader(f)
f.seek(0)
next(rea)
for line in rea:
	salary += [line[4]]
salary.sort(reverse = True)
f.seek(0)
next(rea)
for i in salary:
	for line in rea:
		if i == line[4]:
			print(line[0],line[4])"""
			
			

# pgm 10
# f = open(r'C:\\Users\\apurv\\VSC\\Python\\labs\\programcodeweek7\\pythonlab.csv','r')
# rea = csv.reader(f)
# f.seek(0)
# next(rea)
# dic = {}
# for line in rea:
# 	if line[3] in dic:
# 		dic[line[3]] += 1
# 	else:
# 		dic[line[3]] = 1
# for i in dic:
# 	if dic[i] == 1:
# 		print(i)

# f.close()

import csv

with open(r'C:\\Users\\apurv\\VSC\\Python\\labs\\programcodeweek7\\pythonlab.csv', 'r') as f:
    rea = csv.reader(f)
    next(rea)  # skip header

    dic = {}
    for line in rea:
        if line[3] in dic:
            dic[line[3]] += 1
        else:
            dic[line[3]] = 1

    for key, value in dic.items():
        if value == 1:
            print(key)

