#task 1

x, y, z = 10, 20.5, "hello"
print(x)
print(y)
print(z)


#task 2
complex_variable = 1 + 2j
normal_variable = 2
print(type(complex_variable))
print(type(normal_variable))
print(f"complex_variable_before_swap: {complex_variable}, normal_variable_before_swap: {normal_variable}")
complex_variable, normal_variable = normal_variable, complex_variable
print(f"complex_variable_after_swap: {complex_variable}, normal_variable_after_swap: {normal_variable}")


#task 3
first_number = 2
second_number = 3
print(f"Before swap first number {first_number} second number {second_number}")

print("After swap without temporary variable")
first_number, second_number = second_number, first_number
print(f"first number {first_number} second number {second_number}")

first_number = 2
second_number = 3
temporary_number = first_number
first_number = second_number
second_number = temporary_number
print("After swap with temporary variable, called temporary_number")
print(f"first number {first_number} second number {second_number}")


#task 4
#Python 3
value = eval(input("Please enter the input: "))
print(f"The value you inserted is: {value}")


#Python 2
value = eval(raw_input("Please enter the input: "))
print "The value you inserted is: {} ".format(value))



#task 5
x, y = [int(x) for x in input("Enter two numbers between 1 to 10 separated by space ").split()]  
if (x <= 10 and x >=1) and (y <=10 or y >=1):
    z = x + y
    z += 30
    print(f"The final result after all desired operation is :{z}")
else:
    print(" The values you entered either don't satisfy the boundary or they can't be integers")


#task 6
value = eval(input("Please enter the input: "))
print(f"The input value data type is: {type(value)}")

#task 7
a = 2
print(a)
a = 2.5
print(a)

''' With this example, from the result it can  be seen that the values will be overwritten with the latest
assignment to that particular variable. The reason is that, when a variable is declared with a value,
a space in memory is also declared at the same time for reserving space for that particular variable.
Now, if a new value is assigned  to that particular variable once again, after evaluating the value,
that varible will be overwritten. If this is not the case, then there might be situation where
there are lot of initialized varibles stored in the memory and the memory might have been overflown. So, to 
maintain a certain lifetime of that variable, this reinitialization technique has been in practise for all
programming languages.  
 '''