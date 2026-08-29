#DAY3 begins with learning of operators in python.
#today we will learn about arithmetic operators, comparison operators, logical operators, assignment operators, and bitwise operators,identity operators, membership operators.


#operater:it is symbol or a keyword that performs specific operations on the values
#1.ARITHMATIC OPERATOR

#addition operation  +

a = 20
b = 30
print(a + b)

result = 12 + 39
print(result)

result = a + b
print(result)

a+=a
print(a)

#print(a+=a)  #this is invalid and it will throw an error

#subtraction - 

a = 20
b = 15
result = a - b
print(result)

print(a - b)

print(b - a)

#division /
a=5
b=2
result=a/b
print(result)

print(a/b)

#floor division // :it gives the output in the integer format

a=5
b=2
print(a//b)#this will print 2 instead of the 2.5 as the floor division is used to print only the int value and it excludes the float value

#modulus %: it returns the remainder value 
a=5
b=2

print(a % b)
print(b % a)

#Exponentiation **
a=5
b=2
print(a ** b)

#2. comparison operator
#comprison operator performs comparison operation of two values

#equal ==
a=5
b=2
print(a == b)

print(a == 5)

#not equal !=
a=5
b=2
print(a != b)
print(a != 5)

#greater than >
a=5
b=2
print(a>b)
print(b>5)

#less than <
a=5
b=2
print(a<b)
print(a<100)

#greater than or equal to >=
a=5
b=2
print(a>=b)
print(a >= 5)

#less than or equal to 
a=5
b=2
print(a <= b)

#3.logical operator
#Logical operators allow you to combine Boolean values or conditions.
#and
age = 20
print(age >= 18 and age <= 25)

a = True
b = False
print(a and b)

#or
age = 20
print(age >= 18 or age <= 5)

a = True
b = False
print(a or b)

#not
a = True
print(not(a)) 

#4.Assignment operator 
#basically assignment operator (=) performs a arithmatic operation and assigns the value to the defined variable in syntax
#for example
#add
a=2
a+=a
print(a)
#sub
a=2
a-=a
print(a)
#mul
a=2
a*=a
print(a)
#div
a=2
a/=a
print(a)
#floor divsion
a=2
a//=a
print(a)
#modulus
a=2
a%=a
print(a)
#exponentiation
a=2
a**=a
print(a)
