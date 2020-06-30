#2.1

value = eval(input("Please enter the number: "))
if value%3==0:
    print("Consultadd")
elif value%5 == 0:
    print("c")
elif value%3 == 0 and value%5 == 0:
    print("Consultadd Python Training")



#2.2
value = eval(input("Please enter the number to detect the type of operation: 1 for addition, 2 for subtraction, 3 for divison, 4 for multiplication, 5 for average "))
first, second = [int(x) for x in input("Please enter two numbers: ").split()] 
if value == 1:
    answer = first + second
elif value == 2:
    answer = first - second
elif value == 3:
    if second != 0:
        answer = first / second
    else:
        print("The dividor is zero")
elif value == 4:
    answer = first * second
elif value == 5:
    first1, second2 = [int(x) for x in input("Two more numbers please").split()]
    answer = first + first1 + second + second2)/4

if float(answer) < 0:
    print("Zsa")
else:
    print(answer)




#task 2.3
age = eval(input("Enter your age: "))
if age >= 11:
    print("You are eligible to see the Football match")
    if age <= 20 or age >= 60:
        print("Ticket price is $12")
    else:
        print("Ticket price is $20")
else:
    print("You're not eligible to buy a ticket")



#task 2.4

value = eval(input("Enter a number: "))
while True:
    if value < 0:
        print("It's over")
        break
    else:
        print("Good Going") 


#task 2.5
print([x for x in range(2000, 3201) if x%7 == 0 and x%5 !=0])

#task 2.6
#1
# TypeError: 'int' object is not iterable, we need to deal with some iterable such as range()

#2
# this program prints 0, 1, 2

#3
# This program prints 0, 1, 2, 3, 4


#task 2.7
for i in range(6): # 6 would be exclusive already in the range function
    if i == 3:
        continue
    print(i)



#task 2.8
value = input("Enter the alphanumeric string: ")
digitCount = 0
letterCount = 0
for i in value:
    if i.isdigit():
        digitCount +=1
    else:
        letterCount += 1

print(f"letters {letterCount} digits {digitCount}")


#task 2.9
#1st part
lucky_number = 7
correct_number = eval(input("Guess the lucky number: "))
while True:
    if correct_number == lucky_number:
        break

#modified one
answer = ""
while True:
    correct_number = eval(input("Guess the lucky number: "))
    
    if (correct_number == lucky_number): 
        break
    answer = input("Do you want to guess again? Please type 'no' to stop the program. " )
    if answer == "no":
        break


#task 2.10
counter = 1
while counter <= 5:
    number = eval(input("Guess the number "))
    if number == lucky_number:
        print("Good guess")
    else:
        print("try again!")
    counter += 1



#task 2.11
counter = 1
while counter <= 5:
    number = eval(input("Guess the number "))
    if number == lucky_number:
        print("Good guess")
        break
    else:
        print("Sorry but that was not very successful")
    counter += 1
