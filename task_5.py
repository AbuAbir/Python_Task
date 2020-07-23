# TASK FIVE: HIGHER ORDER FUNCTIONS, GENERATORS, LIST COMPREHENSION AND DECORATOR	

# 1.
# Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. 
# Make sure to use only higher order function.

numbers = filter(lambda x: x%3 != 0 and x%7 == 0, range(10000))
print(next(numbers))

# 2. 	
# Write a program in Python to  multiply the element of list by itself using a traditional function 
# and pass the function to map to complete the operation.

def multiply(x):
    return x*x

result = map(multiply, range(1,10))
print(next(result))


# 3.
# Write a program to Python find out the character in a string which is uppercase using list comprehension.
string="abUaBiR"
print([i for i in string if i.isupper() is True])

# 4. 	
# Write a program to construct a dictionary from the two lists containing the names of students and their
# corresponding subjects. The dictionary should maps the students with their respective subjects. 
# Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also
# Student = ['Smit', 'Jaya', 'Rayyan']
# Capital = ['CSE', 'Networking', 'Operating System']

print({name:subject for name, subject in zip(Student, Capital)})


# 5. 	
# Learn More about Yield, next and Generators
# Learned

# 6. 	
# Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”

def gen(n):
    for i in n:
        yield i

res = gen('Consultadd Training') 
reverse=""
while True: 
    try:
        reverse = next(res) + reverse
    except StopIteration:
        break
print(reverse)


# 7. 	
# Write any example on decorators.

# The following example would modify the functionality if divisor is a zero

def checkIfZero(original_func):
    def inside(a,b):
        if b == 0:
            print("can't divide by zero")
            exit()
        return original_func(a,b)
    return inside

@checkIfZero
def division(a,b):
    return a/b

print(division(2,3))
print(division(2,0))


# 8. 	
# Learn about What is FRONT END and its Technologies and Tools
# Make sure to mention at least 5 top notch technologies of Frontend.
# Also mention the name of companies using those 5 technologies individually

React.js - Airbnb, Dropbox, BBC, Facebook, New York Times, and Reddit are some of the prominent 
websites and web apps built with React.

Angular.js - Netflix, Upwork, IBM, Goodfilms, and Freelancer are some of the renowned websites built with Angular. Gmail, Paypal, and The Guardian 
are some of the well-known applications built with Angular.

Vue.js - 9gag, Nintendo, GitLab, Behance, and Laravel

Flutter - Google ads, Alibaba, Birch Finance, Cryptograph, and Hookle are 
some of the applications powered by Flutter.

Ionic -  National Health Service, GE Transportation, Market Watch, 
and Amtrak are some of the examples of business built on Ionic.
