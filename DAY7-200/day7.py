#Day : 7 ; while loops ,continue,breakand pass statements
#while loops: A while loop repeatedly executes a block of code as long as a condition is True.

#while loop syntax:
#while condition:
#  #code block to be executed
i = 1
while i<=5:
    print(i)
    i+=1  
 #this will print numbers from 1 - 5
#if we dont use i+=1 to increment then the value will always be 1 and loop will run infinitely
# while loop to ask the user to enter the password untill user enters the correct password 
password = input("Enter the password:")
while password != "farhan123456789":
    print("Incorrect password ,please enter the password again:")
    password = input("Enter the password:")
print("password is correct, access Granted!...")       

#lets learn abt the break statement

i = 1
while i<10:
    if i == 3:
        break
    print(i)
    i+=1

#this will print 1 and 2 and then break the loop when i is equal to 3


#using break with user input 
#for ex, this code will ask the user for a number and will print the number untill the user enters 0, then it will break the loop

num = int(input("Enter a number except 0(0 to exit): "))
while True:
    if num == 0:
        print("as you entered 0,the loop ends and the program exits...") 
        break
    print("you entered:", num)
    break


#continue statement: The continue statement is used to skip the current iteration of a loop and move on to the next iteration.

count = 0

while count < 10:
    count += 1

    if count == 5:
        continue

    print(count)


#pass statement: The pass statement is a null operation; it does nothing when executed. It is used as a placeholder in situations where code is syntactically required but you don't want to execute any code. 
while True:
    pass  # This loop will run indefinitely and do nothing                 

#combining break, continue and pass statements in a while loop
num = 0 
while num < 10:
    num += 1
    if num == 3:
        continue  # Skip the rest of the loop when num is 3
    if num == 5:
        pass 
    if num == 8:
        break  # Exit   the loop when num is 8
    print(num)
#this code will print numbers from 1 to 10 except 3 and will break the loop when num is equal to 8    


