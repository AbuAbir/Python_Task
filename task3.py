#task 3.1
'''Create a list of the 10 elements of four different types of Data Types like int, 
string, complex, and float.
'''

list1 = [1, 2.4, 2+3j, 'abir']
print(list1)

#task 3.2
'''Create a list of size 5 and execute the slicing structure 
'''
list2 = [10, 20, 30, 40, 50]
print(list2[2:4]) #prints [30, 40]
print(list2[-3:-1]) #prints [30, 40]


#task 3.3
'''Write a program to get the sum and multiply of all the items in a given list.
'''
list2 = [10, 20, 30, 40, 50]
sum_result = 0
multiply_result = 1
for i in list2:
    sum_result+=i
    multiply_result*=i
print(sum_result)
print(multiply_result)


#task 3.4
'''Find the largest and smallest number from a given list. '''
list2 = [50, 20, 40, 10, 30]
smallest = list2[0]
largest = list2[0]
for i in range(len(list2)):
    if list2[i] < smallest:
        smallest = list2[i]
    elif list2[i] > largest:
        largest = list2[i]
print(smallest)
print(largest)

#task 3.5
'''Create a new list that contains the specified numbers after 
removing the even numbers from a predefined list. 
'''
list2 = [51, 20, 40, 15, 30]
print([x for x in list2 if x%2 != 0])


#task 3.6
'''Create a list of first and last 5 elements where the values are square of numbers 
between 1 and 30 (both included). '''
square = [i*i for i in range(1,31)]
new_list_with_first_and_last_5_elements = square[:5] + square[25:]
print(new_list_with_first_and_last_5_elements)


#task 3.7
'''Write a program to replace the last element in a list with another list.
Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
Expected output: [1,3,5,7,9,2,4,6,8]
'''
list1 = [1,3,5,7,9,10]
list2 = [2,4,6,8]
temp = list1[:len(list1)-1]
temp.extend(list2)
print(temp)



#task 3.8
'''
Create a new dictionary by concatenating the following two dictionaries:
a={1:10,2:20}
b={3:30,4:40}
Expected Result: {1:10,2:20,3:30,4:40}
'''
a = {1:10,2:20}
b = {3:30,4:40}
a.update(b)
print(a)


#task 3.9
'''
Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
Sample data (n=5)
Expected Output: {1:1,2:4,3:9,4:16,5:25}

'''
sample = dict()
n = 10
for i in range(1,n+1):
    sample[i] = i*i
print(sample)



#task 3.10
'''
Write a program which accepts a sequence of comma-separated numbers from the console 
and generate a list and a tuple which contains every number. Suppose the following input
is supplied to the program:34,67,55,33,12,98
The output should be:
[‘34’,’67’,’55’,’33’,’12’,’98’]
(‘34’,’67’,’55’,’33’,’12’,’98’)
'''
list1 = input()
n = list1.split(",")
newList = list(n)
print(newList)
newTuple = tuple(n)
print(newTuple)

