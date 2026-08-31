#DAY :4 (input(), Fstrings, string formatting)
#1. input()
#The input() function in python allows the python program to take information or inputs from the user 

x=input()
print(x)

#point to  remember is that input() function always stores the value entered in string format as default.
#to check
print(type(x))

#we can use type conversionn on it in 2 comman and efficient ways ,lets  go one by one 
#method 1.
#lets do with addition two positive integer value
x = input("enter the value of 1st number:")
y = input('enter the value of 2nd number:')

result = x + y

print(f"result before the type conversion:{result}")
#the + operator will treat the value of x and y as string value so it will perform addition of two strings

x = int(x)
y = int(y)

result = x + y
print(f"result after the type conversion:{result}")

#method 2. ,and it is  the most efficient and easy to use 
x = int(input("enter the value of 1st number:"))
y = int(input('enter the value of 2nd number:'))

result = x + y

print(f"resul by using type conversion along with the input() function itself:{result}")

#converting input type to float()
x=float(input("enter the float value to check the conversion:"))
print(x)
print('data type of value of x:',type(x))

#2. f-strings 
#this topic has been learned in the day2 and been in practicing fron that on.


#3.string formatting
name = "Farhan"

print("Hello, " + name)

#String Concatenation Using +
first_name = "Farhan"
last_name = "Baji"

full_name = first_name + " " + last_name

print(full_name)

#lets learn use of format()
name='farhan'
age=23
print('My name is {}, and i\'m {} years old'.format(name,age))

#Formatting Decimal Numbers With F-Strings
price = 99.9999

print(f"Price: {price:.2f}")  

#another example
pi = 3.1415926535

print(f"Pi: {pi:.2f}")
