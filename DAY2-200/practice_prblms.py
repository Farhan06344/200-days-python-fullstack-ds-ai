#this fille contains the practice problems for day 2 of 200 days
#PROBLEM:1 Create variables,print the variables and check the data types of the variables
#creation of variables
name = "mohammed Farhan"
age = 21
gender = "male"
student = True
cgpa = 8.4

#printing the variables
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Gender: {gender}")
print(f"Student: {student}")
print(f"CGPA: {cgpa}")

#checking the data types of the variables
print(f"Data type of name: {type(name)}")
print(f"Data type of age: {type(age)}")
print(f"Data type of gender: {type(gender)}")
print(f"Data type of student: {type(student)}")
print(f"Data type of cgpa: {type(cgpa)}")

#PROBLEM:2 CONVERTING THE DATA TYPES OF VARIABLES
#converting the data types of variables
age = "20" #string
print(f"Data type of age before conversion: {type(age)}")
age = int(age) #convert to integer
print(f"Data type of age after conversion: {type(age)}")

marks = 85.5 #float
print(f"Data type of marks before conversion: {type(marks)}")
marks = int(marks) #convert to integer
print(f"Data type of marks after conversion: {type(marks)}")

#PROBLEM:3 CONVERSION AND CALCULATION
daily_hours = "3"
total_days = "200"
print(f"Daily hours: {daily_hours}")
print(f"Total days: {total_days}")
daily_hours = int(daily_hours)
total_days = int(total_days)
print(f"Daily hours (converted): {daily_hours}")
print(f"Total days (converted): {total_days}")
#calculation of total hours
total_hours = daily_hours * total_days
print(f"Total hours spent in 200 days: {total_hours}")  
print(f"Data type of total_hours: {type(total_hours)}")

#problem:4 string vs integer
a = 20
b = "20"
print(a+a)#this prints 40 as a is an integer
print(b+b)#this prints 2020 as the value of b is within "" it is considered a string and the + operator concatenates the strings

print(f"Data type of a: {type(a)}")
print(f"Data type of b: {type(b)}")

#problem:5 student profile
#converting the data types of variables
name = "Farhan"
age = "20"
height = "5.8"
print(f"Name: {name}")
age = int (age)
print(f"Age: {age}")
height = float(height)
print(f"Height: {height}")


#problem:6 200 day tracker

current_day = 2
total_days = 200
daily_hours = "3"

remaining_days = total_days - current_day
total_hours = remaining_days * int(daily_hours) 

print(f"current_day: {current_day}")
print(f"total_days: {total_days}")      
print(f"daily_hours: {daily_hours}")
print(f"remaining_days: {remaining_days}")  
print(f"total_hours: {total_hours}")