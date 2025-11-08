#Given a list of integers nums and an integer target, find the indices of the two numbers such
#that they add up to target

def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

'''A teacher has two equal groups of students. The first group is seated in the first half of a
row, and the second group in the second half of the row. The teacher now wants to
rearrange the seating so that students from both groups sit alternately.
Write a Python program to read the roll numbers of 2n students (entered in a single line
separated by spaces) and rearrange them in an alternating order.
• The first n roll numbers represent Group A.
• The next n roll numbers represent Group B.
• The output should display the new arrangement as [A1, B1, A2, B2, …, An, Bn'''

students = input("Enter roll numbers: ").split()
n = len(students) // 2
result = []

for i in range(n):
    result.append(students[i])
    result.append(students[n+i])

print(result)


'''Your goal is to write a program that combines two lists into a single new list. The new list
should be created by taking elements from the two input lists in an alternating pattern,
starting with the first element of the first listOnce all the elements from the shorter list have been used, append the rest of the
elements from the longer list to the end of the new list.
Input
Two lists, which may have different lengths. For example:
• List 1: m = [11, 22, 33]
• List 2: n = [66, 55, 77, 44, 88]
Output
A single new list containing the merged elements. Following the example above, the
process would be:
1. Take 11 from m.
2. Take 66 from n.
3. Take 22 from m.
4. Take 55 from n.
5. Take 33 from m.
6. Take 77 from n.
7. List m is now empty. Append the rest of list n ([44, 88]).
The final output should be: [11, 66, 22, 55, 33, 77, 44, 88]'''

def merge_alternate(m, n):
    result = []
    i = j = 0
    while i < len(m) and j < len(n):
        result.append(m[i])
        result.append(n[j])
        i += 1
        j += 1
    result += m[i:] + n[j:]
    return result

m = [11, 22, 33]
n = [66, 55, 77, 44, 88]
print(merge_alternate(m, n))


'''A tuple is used to represent a shopping cart in an online grocery store.
cart = ("Milk", "Bread", "Butter", "Cheese", "Jam", "Eggs")
Tasks:
1. Pack the above items into a tuple. Unpack the first three items into separate
variables and print them. Print the remaining items as a list and check its type.
2. Display all items in the cart using a loop.
3. Print only the first 3 items and the last 2 items using slicing.
4. Check whether "Butter" and "Honey" are present in the cart.
5. Add a new tuple ("Juice", "Fruits") to the cart and display the updated cart.
6. Find the index of "Cheese" in the cart.
7. Count how many times "Butter" appears in the cart.'''
cart = ("Milk", "Bread", "Butter", "Cheese", "Jam", "Eggs")

a, b, c, *rest = cart
print(a, b, c)
print(list(rest))
print(type(list(rest)))

for item in cart:
    print(item)

print(cart[:3])
print(cart[-2:])

print("Butter" in cart)
print("Honey" in cart)

new_cart = cart + ("Juice", "Fruits")
print(new_cart)

print(cart.index("Cheese"))
print(cart.count("Butter"))

'''Write a python program to remove the duplicate elements in the sorted list.
Example:
List1 = [1,1,2,3,3,3,4,4,5,6,6,6]'''

List1 = [1,1,2,3,3,3,4,4,5,6,6,6]

result = []
for num in List1:
    if not result or result[-1] != num:
        result.append(num)

print(result)

'''running sum'''
nums = [1, 2, 3, 4]

result = []
running_sum = 0
for num in nums:
    running_sum += num
    result.append((num, running_sum))

print(result)
