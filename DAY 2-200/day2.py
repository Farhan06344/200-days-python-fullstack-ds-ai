#day 2 includes learnig about variables ,data types ,and type conversion in python
# lets start with learning the variables in python
#In python we can directly store the data in a variable without declaring the data type of the variable 
#Even a single variable in python can hold different types of data becouse python is a dynamically binded language
#practice wth variables

name = "Mohammed Farhan"
print(name) #this would print perfectly 
#print(Name)# this would throw an error as we know python is a case sensitive language and Name is not same as name
name = "Farhan" #the varible name is now holding a new value
age = 20 #the variable age is now holding an integer value

print(name)#this would print the new value of the name variable
print(age)

#now i  will be using different data types for my variables
height = 5.9 #float
is_student = False #boolean
print(height)
print(is_student)


#practice of printing different types of data using variables
name = "Mohammed Farhan"
age = 20
height = 5.11
is_student = True
gender = 'Male'

#method 1 of printing the variables
print(name)
print(age)
print(height)
print(is_student)
print(gender)

#method 2 of printing the variables
print("Name:",name) 
print("Age:",age)
print("Height:",height)
print("Is Student:",is_student)
print("Gender:",gender)


#method 3 of printing the variables using f-string
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")
print(f"Gender: {gender}")

#method 4 of printing the variables using f-string
print(f'my name is {name},my age is {age},myheight is {height},and whether i am a student:{is_student},and my gender is {gender}')


#some more practice with variables

a=10;b=20;c=30
print(a,b,c)

a,b,c = 10,20,30
print(a,b,c) #this would print 10 20 30


#DATA TYPES IN PYTHON

#lets start with the basic data types in python
#1. Integer: This data type is used to store whole numbers without any decimal point.
#2. Float: This data type is used to store numbers with decimal points.
#3. String: This data type is used to store a sequence of characters enclosed in single or double quotes.   
#4. Boolean: This data type is used to store either True or False values.   


name = "Mohammed Farhan" 
age = 15
height = 5.11

print(type(name)) #the type() function is used to check the data type of a variable
print(type(age))
print(type(height))

num = -2
print(type(num))

#the representation of the data types in python is as follows:
#1. Integer: int
#2. Float: float
#3. String: str
#4. Boolean: bool


age = 20 #is an integer
age1 = 20.5 #is a float
age2 = "20" #is a string

print(type(age),type(age1),type(age2)) #this would print the data types of the variables age, age1 and age2

is_student = True #is a boolean
print(type(is_student)) #this would print the data type of the variable is_student

result = None #is a special data type in python which represents the absence of a value or a null value
print(type(result)) #this would print the data type of the variable result

#the string concatenation can also be done using the + operator in python
first_name = "Mohammed" 
middle_name = "Farhan"
last_name = "SirajBaji"

full_name = first_name + " " + middle_name + " " + last_name #this would concatenate the three strings and store it in the variable full_name
print(full_name) #this would print the full name
print(type(full_name))


#TYPE CONVERSION IN PYTHON
#Type conversion is the process of converting one data type to another data type in python.

#convert to integer
num = "10"
print(type(num)) #this would print the data type of the variable num
num = int(num) #this would convert the variable num to an integer data type
print(type(num)) #this would print the data type of the variable num


#convert to float
price = "99.99"

price = float(price)

print(price)
print(type(price))

#convert to string
age = 20
print(type(age)) #this would print the data type of the variable age as integer
age = str(age)
print(type(age)) #this would print the data type of the variable age as string

#convert float to integer
price = 99.99
price = int(price) #this would convert the variable price to an integer data type
print(price)#this would print the value of the variable price as 99
#convert integer to float
age = 20
age = float(age)
print(type(age)) #this would print the data type of the variable age as float
print(age) #this would print the value of the variable age as 20.0

#conversion of boolean
print(bool(1)) #this would print True
print(bool(0)) #this would print False

#conversion 
age = int('38')
print(age) #this would print 38
print(type(age)) #this would print <class 'int'>

