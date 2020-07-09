#Weekend Activity on data structure
#1 #2 same as before
#3
'''
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
Access list [1, 2, 3, 4]
Access list [600,  700]
Access list [100, 300, 500, 600, 800]
Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 
500, 400, 300, 200, 100]]
Access list [10]
'''
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][:4])
print(x[6:8])
print(x[::2])
print(x[::-1])
print(x[5][5][:1])
print(x[5][5][:0])


#4
'''
Create a list of thousand numbers using range and xrange and see the difference 
between each other.


python 2.7, xrange and range are different, range returns the whole
list with all the numbers whereas xrange returns only the object which
can be used later as needed. In python 3, xranges is not supported and
is already implemented with range function.
'''
print(xrange(1000)) #for python 2
print(range(1000))


#5
''' 
How Tuple is beneficial as compared to the list?


Tuple is beneficial in a way compared to listwhen we need some i
mplementation where we need immutable property of data structure, unlike
list, in other words some kinds of data structure where change of 
the values is not desired or expected. In this case, tuple gives us 
the benefit over list
'''

#6
'''
Write a program in Python to iterate through the list of numbers in the range of 
1,100 and print the number which is divisible by 3 and a multiple of 2.
'''
print([i for i in range(1101) if i%3==0 and i%2 == 0])

#7
'''
Write a program in Python to reverse a string and print only the vowel alphabet 
if it exists in the string with their index.
'''
alphabets = "Consultadd is in Texas"
alphabets.lower()
new = alphabets[::-1]
print("Reversed string is: ", new)
for x in range(len(new)):
    if new[x] =='a'  or new[x] =='e' or new[x]=='i' or new[x]=='o' or new[x] == 'u':
        print("index of the vowels in the reversed string", x)


#8
'''
Write a program in Python to iterate through the string “hello my name is Abcde” and 
print the string which has even length of the word.
'''
test_string = "hello my name is Abcde"
without_space = test_string.split(" ")
for i in without_space:
    if len(i)%2==0:
        print(i)

#9
'''
Write a program in python to print the pair of numbers whose sum is equal to result 
number that is let's say 8. x=[1,2,3,4,5,6,7,8,9,-1]
'''
x=[1,2,3,4,5,6,7,8,9,-1]
target = 8
nums = {}
for i in x:
    if i>=0:
        potentialMatch = target-i 
    else:
        potentialMatch = abs(i-target)
    if potentialMatch in nums:
        print([i, potentialMatch])
    else:
        nums[i] = potentialMatch



#10
'''
Write a program in Python to complete the following task:
Create two different lists as in even_list and odd_list
Ask the user to enter the number in the range of 1,50 and make sure if the entered 
number is even appended it to the even_list and if the entered number is odd append it 
to the odd list.Keep that in mind you can only add 5 items in each list
Make sure once you entered the total 5 elements calculate the sum of the list and return
 the maximum out of the list.
'''
even_list = []
odd_list = []
odd_count  = 0
even_count = 0
while True:
    if odd_count == 5 and even_count == 5:
        break
    value = int(input("Please enter any number in the range of 1-50: "))
    if value<1 or value>50:
        print("Check again the input range insertion condition")
        continue
    if value%2 == 0 and odd_count <=5:
        even_list.append(value)
        odd_count+=1
    elif even_count <=5:
        odd_list.append(value)
        even_count+=1

def sum_result(list1):
    summation = 0
    for i in list1:
        summation += i
    return summation

def maximum(list2):
    largest = list2[0]
    for i in range(len(list2)):
        if largest < list2[i]:
            largest = list2[i]
    return largest

print("Sum of odd list ", sum_result(odd_list))
print("Maximum of odd list ",maximum(odd_list))
print("SUm of even list ", sum_result(even_list))
print("Maximum of even list ", maximum(even_list))


#11
'''
Write a program to find out the occurrence of a specific word from an alphanumeric statement. 
Example: 12abcbacbaba344ab  
Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic
'''
alphanumeric = "12abcbacbaba344ab"
def removeDigits(s):
    answer = []
    for char in s:
        if not char.isdigit():
            answer.append(char)
    return ''.join(answer)

a = removeDigits(alphanumeric)

count = {}
for i in a:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)


#12
'''
Generate and print another tuple whose values are even numbers in the
 given tuple (1,2,3,4,5,6,7,8,9,10).
 '''
t1 = (1,2,3,4,5,6,7,8,9,10)
t2 = ()
for x in t1:
    if x%2 == 0:
        t2 = t2 + (x,)
print(t2)
