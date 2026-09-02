#multiplication table using for loop,range()
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
print('\n')

#using for ,range ,enumerate to print multiplication table

num = int(input("Enter a number to print its multiplication table: "))
number = range(1, 11)
for index,i in enumerate(number,1):
    print(f"{index}. {num} x {i} = {num*i}")
print('\n')


#printing all the even numbers from 1 to 100 using for loop and range() function
print("All the even numbers between 1-100 are:")
for i in range(2,101,2):

    print(i)
print("\n")


#character with index
name = input("Enter your name:")

for index,character in  enumerate(name,1):
    print(f"{index} -> {character}")      
print('\n')    
