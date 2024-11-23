# -*- coding: utf-8 -*-
"""python_practice.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VGYtXVYTVEgRxvkhy4f_9tDxVE8owiZ-

Write a Python program that creates a list of integers from 1 to 10, and then prints the square of each number in the list
"""

a=[]
for i in range(1,11):
  a.append(i)
for number in a:
  print(number**2)

"""Write a Python function that takes a list of integers as input and returns the maximum number in the list."""

def max_num(numbers): #function defined
    max_number=numbers[0]
    for num in numbers:
      if num>max_number:
        max_number=num

    return max_number

numbers = [11,22,78,99]
maximum_number = max_num(numbers)
print("The maximum number is:", maximum_number)

"""Write a Python program that takes two lists of integers as input and returns a new list containing only the common elements of both lists"""

x=[1,5,8,9,3]
y=[4,5,7,77,10,9]
z=[]
for i in x:
  if i in y:
    z.append(i)
print(z)

"""Write a Python program that takes a list of strings as input and returns a new list containing only the strings that start with the letter 'a'."""

list1=['ram','raj','bob','robert','ankita','arun']
list2=[]
for name in list1:
  if name.startswith('a'):
    list2.append(name)
print(list2)

"""Write a Python program that takes a list of integers as input and returns a new list containing only the even numbers in the original list"""

list1=[22,15,1,88,99,77,110]
list2=[]
for i in list1:
  if i%2==0:
    list2.append(i)
print(list2)

"""Write a Python function that takes a list of integers as input and returns a new list where each element is the sum of the previous two elements in the original list."""

a=[1,5,6,9,7]
b=[]
for i in a:

""" Write a Python program that takes a list of integers as input and returns a new list containing only the unique elements of the original list."""

a = [5, 8, 9, 6, 4, 7, 88, 99, 66, 11, 55, 11, 88, 99, 110, 110]
c = []

for i in a:
    if i not in c:
        c.append(i)

print(c)

""".Write a Python program that takes a list of strings as input and returns a new list containing only the strings that are palindromes."""

str1=['raj','ranveer','ankit','malayalam']
palindromes = []

for i in str1:
  if i == i[::-1]:
    palindromes.append(i)

print(palindromes)

"""Write a Python function that takes two lists of integers as input and returns a new list containing the elements that are in the first list but not in the second list."""

a=[1,2,3,4,5,6,8,9,7,99,110]
b=[1,2,3,4,5,6,8,9,7,22]
c=[]

for i in a:
  if i not in b:
    c.append(i)

print(c)

"""Write a Python program that takes a list of strings as input and returns a new list where each element is the reverse of the corresponding element in the original list."""

str1=['ram','shyam','ankita','virat']
str2=[]
for i in str1:
  str2.append(i[::-1])
print(str2)

"""# Assignment 2

Write a Python program that takes a list of integers as input and returns a new list where each element is multiplied by 2Write a Python function that takes a list of integers as input and returns the sum of all the even numbers in the list
"""

lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele*2)

print(lst)

"""Write a Python program that takes a list of strings as input and returns a new list containing only the strings that have a length greater than 5"""

str1=['ram','shyam','ankita','virat']
str2=[]
for i in str1:
  if len(i)>5:
    str2.append(i)
print(str2)

"""Write a Python program that takes a list of integers as input and returns a new list containing only the numbers that are divisible by 3"""

list1=[11,55,99,33,110,109,111,112,117,51,200,260,81]
list2=[]
for i in list1:
  if i%3==0:
    list2.append(i)
print(list2)

"""Write a Python function that takes a list of integers as input and returns the second largest number in the list."""

list1=[11,55,99,33,110,109,111,112,117,51,200,260,81]
list1.sort()
print('list after sorting:',list1)
print('2nd largest no:',list1[-2])

"""Write a Python program that takes two lists of integers as input and returns a new list containing the elements that are in both lists

"""

a=[55,44,88,22,33,11]
b=[55,77,99,11,111,66,33]
c=[]
for i in a:
  if i in b:
    c.append(i)
print(c)

"""
Write a Python program that takes a list of strings as input and returns a new list containing only the strings that contain the substring 'ing'.


"""

str1=['second','running','hii','hello','programming','ronit','doing','wrong']
str2=[]
for i in str1:
  if 'ing' in i:
    str2.append(i)
print(str2)

str1=['second','running','hii','hello','programming']
str2=[]
for i in str1:
  if i.endswith('ing'):
    str2.append(i)
print(str2)

str1=['second','running','hii','hello','programming']
str2=[]
for i in str1:
  if i[-3:]=='ing':
    str2.append(i)
print(str2)

str1=['second','running','hii','hello','programming']
str2=[]
for i in str1:
  if i.find('ing')!=-1: #The find() method returns the starting index of 'ing' if it’s found in the string.
                        #If 'ing' is not found, find() returns -1.
    str2.append(i)
print(str2)

"""Write a Python function that takes a list of integers as input and returns a new list where each element is the product of the previous two elements in the original list"""

list1=[1,2,3,4,5,6,7]
list2=[]
for i in range(1,len(list1)):
  list2.append(list1[i-1]*list1[i])
print(list2)
