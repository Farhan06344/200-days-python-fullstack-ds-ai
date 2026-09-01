#DAY:5,Todays topics are if, elif, else & Nested Conditionals statements
#these are the conditional statements allows the program to take decisions based on conditions provided,turns out to be true or false
#simple if statement




a = 21
if a == 21:
   print("the 'a' holds the value 21")

#in python, boolean values are represented as True and False, they are case sensitive.
print(a >= 20)
print(a <= 20)

#if-statements

age = 18
if age >= 18:
    print("you are eligible for having a driving license")

#intendation is very important in python, it is used to define the blocks of code, if the indentation is not proper then the program will throw an error. 

#if age < 18:
#print("you are not eligible for having a driving license")   
##this will throw an error because the print statement is not indented properly, it should be indented to the right by 4 spaces or 1 tab space.

#if else statement with user input
age = int(input("enter your  age :"))
if age >= 18:
    print("you are eligible for having a driving licence and you can also vote in the elections")
else:
    print(f"you are not eligible for having a driving licence and you cannot vote in the elections,wait for {18 - age} years to get your driving licence and vote in the elections") 

#checking whether a number is even or odd using if else statement
number = int(input("enter the number which you wnt to check whether it is even or odd :")) 
if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"the number {number} is odd") 

#now lets do practice with elif statement
#going to make a simple grading system using elif statemets
#criteria is marks above 90 is distinction,89-80 is first class,79-60 is second class,59-40 is third class,and below 39 is to be considered to be fail

marks = int(input("Enter the marks obtained by the student:"))

if marks >= 90:
    print('congrats you have secured distinction!')
elif marks >= 80:
    print('you have secured first class')
elif marks >= 60:
    print('you have secured second class')
elif marks >= 40:
    print('you have secoured third class')
elif marks < 40:
    print('unfornatately you have failed,don tbe upset do well in upcoming exams!')            

#simple practice on if else elif and nested if

#lets make  a program that grants access if and only if email and password is correct.

email = input("\nEnter your email: ")
password = input("Enter the password:")
if '@' in email:
    if email == "farhan11@gmail.com" and password == "farhan123":
        print('ACCESS GRANTED!, Welcome farhan' )
    elif email != "farhan11@gmail.com" and password == "farhan123":
        print("email is incorrect")
    elif email == 'farhan11@gmail.com' and password != "farhan123" :
        print("entered password is incorrect!")     
    else :
        print("invalid credentials")    
else:
    print("enterd email format is incorrect, please try agein later!")
