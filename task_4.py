# 4.1. 
# Write a program to reverse a string.
# Sample data: “1234abcd”
# Expected Output: “dcba4321”

def reverse(string):
    a = list(string)
    left = 0
    right = len(a) - 1
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -=1
    return "".join(a)

print(reverse("abir"))

# 4.2. 	
# Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def calculateCase(string):
    uppercase=0
    for i in string:
        if i.isupper():
            uppercase+=1
    return uppercase

myString = "AbiAbiAbi"
print("No. of Upper case characters : ", calculateCase(myString))
print("No. of lower case characters : ", len(myString)-calculateCase(myString))


# 4.3. 
# Create a function that takes a list and returns a new list with unique elements of the first list.
def uniqueList(list1):
    uniq = {}
    uniq_list = []
    for i in list1:
        if i not in uniq:
            uniq[i] = 1
            uniq_list.append(i)
        else:
            uniq[i] += 1
    return uniq_list

print(uniqueList([1,1,1,1,1,1,2,3,4,5]))


# 4.4 
# Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a 
# hyphen-separated sequence after sorting them alphabetically.

def hyphenSeparatedWord(string):
    a = string.split("-")
    a.sort()
    return "-".join(a)

print(hyphenSeparatedWord("my-name-is-abu-abir"))


# 4.5.
# Write a program that accepts a sequence of lines as input and prints the lines after making all 
# characters in the sentence capitalized.
# Sample input:
# Hello world
# Practice makes perfect
# Expected Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
m = text.upper()
print(m)

# 4.6.          
# Define a function that can receive two integral numbers in string form and compute their sum and 
# print it in console.


def forPrint(str1, str2):
    sum = int(str1) + int(str2)
    print(sum)

forPrint("2", "3")


# 4.7.        
# Define a function that can accept two strings as input and print the string with maximum length in console. 
# If two strings have the same length, then the function should print all strings line by line.

def maxChecker(str1, str2):
    if len(str1) == len(str2):
        return str1 + "\n" + str2
    else:
        return str1 if len(str1) > len(str2) else str2

print(maxChecker("ny",'my1'))


# 4.8
# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.

def squareNumbers():
    xy = ()
    for x in range(1,20):
        if x*x < 20:
            xy += (x,)
    print(xy)
squareNumbers()


# 4.9.         
# Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit 
# with a label to identify the even and odd numbers. 
# Example: If the limit is 3 , it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

def showNumbers(limit):
    for i in range(limit+1):
        if i%2 == 0:
            print(i ," EVEN")
        else:
            print(i,' ODD')

showNumbers(3)


# 4.10
# Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)

even_numbers = list(filter(lambda x: x%2 == 0, [i for i in range(1,21)] ))
print(even_numbers)

# 4.11. 	
# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
# Hints: Use map() to generate a list.
# Use filter() to filter elements of a list
# Use lambda to define anonymous functions

list_map = list(map(lambda z: z*z , range(1,11)))
list_range = list(filter(lambda x: x%2 == 0 , list_map))
print(list_range)


# 4.12. 	
# Write a function to compute 5/0 and use try/except to catch the exceptions

try:
    x = 5/0
except ZeroDivisionError:
    print("The divisor is zero. Check again. ")


# 4.13. 	
# Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567 
from functools import reduce
list1 = [[1,2,3],[4,5],[6,7,8]] 
flatten = reduce((lambda x, y: x + y), list1)
sec_flattened = reduce((lambda x, y : str(x) +''+ str(y)), flatten)
print(sec_flattened)


#  4.14. 		
#(i) 
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

#result is 2



# (ii) 
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')
a()

#it prints the finally block "after f", then NameError comes since function f() is undefined

