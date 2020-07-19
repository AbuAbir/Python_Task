# TASK SIX: FILE HANDLING AND EXCEPTION HANDLING
# 1.	Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError

try:
    eval("hee =")
except SyntaxError:
    print("Hey! Who's using eval() anyway??")

# 2. 	
# Write a program in Python to allow user to open a file by using argv module. If the entered name is
#  incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode. 


from sys import argv
NameOfProgram, NameOfFile = argv
print(f"The name of the program is {NameOfProgram} and file is {NameOfFile}")
while True:
    try:
        fh = open(NameOfFile, 'r')
        fh.read()
        print(content)
        #fh.close()
        break
    except:
        print("You have entered the filename wrong. Try Again. ")
        NameOfFile = input()

# 3. 	
# Write a program to handle an error if the user entered the number more than four digits it 
# should return “Please length is too short/long !!! Please provide only four digits” 

value = input("Enter the number : ")
if len(value)>4:
    raise Exception('Please length is too short/long !!! Please provide only four digits')
  

# 4. 	
# Create a login page backend to ask user to enter the UserEmail and password.
# Make sure to ask Re-Type Password and if the password is incorrect give chance to enter it again but 
# it should not be more than 3 times.


i = 1
UserEmail = input("Please enter your email :")
password = input("please enter your password :")
Repassword = input("please enter your password once again :")
while True:
    try:
        if password != Repassword:
            raise Exception
        print("password matched")
        break
    except:
        print("your password didn't match, please insert again twice ")
        password = input("please enter your password :")
        Repassword = input("please enter your password once again :")   
    i+=1
    if(i==3):
        print("You have tried 3 times, sorry I need to break the program")
        break


# 5. 	https://www.programiz.com/python-programming/exception-handling Go through this link to
#  understand Finally and Raise concept.

Did it


# 6. 	Read any file using Python File handling concept and return only the even length string
#  from the doc.txt file.
# Consider the content as: 
	# Hello I am a file 
	# Where you need to return the data string 
	# Which is of even length 
	# Make sure you return the content in 
	# The same link as it is present.

with open("doc.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    if len(stripped_line)%2 ==0:
        print(stripped_line)