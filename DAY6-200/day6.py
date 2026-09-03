#DAY 6:Todays topics are for loops, range(), enumerate().
#for loops:
#for loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string). This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

#basic for loop syntax:
#for variable in sequence:

for i in range(5):
    print("hello world!")
#hello world will be  printed 5 times.

for i in range(5):
    print(i)    
#this block of code will print numbers from 0 to 4.


#now we will practice for loops with strings:
name = "Farhan"
for i in name :
    print(i)
print("\n")   

#also can be written as 
name = "raid"
for character in name:
    print(character)
print("\n")    

#for loops can be used to iterate over a list, tuple ,dictionary, set, or string.
list = ['neymar', 'Mbappe', 'ronaldo']
for i in list:
    print(i,"\n")


tuple = ('neymar', 'Mbappe', 'ronaldo')
for i in tuple:
    print(i,"\n")

set = {'neymar', 'Mbappe', 'ronaldo'}
for i in set:
    print(i,"\n")

dictionary = {'neymar': 10, 'Mbappe': 7, 'ronaldo': 10}    
for i in dictionary:
    print(i,"\n")

#use of range() function:

#range() function is used to generate a sequence of numbers. It has three parameters: start, stop, and step.

#use of range(stop):

for i in range(5):
    print(i)
print("\n")     
#this will print numbers from 0 to 4. as range function generates numbers from 0 to stop-1.
#use of range(start, stop):
#to print numbers from 1 to 5 we can use range(1,6) as it will generate numbers from start to stop-1.
for i in range(1,6):
    print(i)
print("\n") 


#use of range(start, stop, step):
#step parameter is used to specify the increment between each number in the sequence. 
# For example, to print even numbers from 2 to 10, we can use range(2, 11, 2).
for i in range(2, 11, 2):
    print(i)
print("\n")    

#range() function can also be used to geanerate a sequence of numbers in reverse order by using a negative step value. 
# #For example, to print numbers from 10 to 1, we can use range(10, 0, -1).
for i in range(10, 0, -1):
    print(i)
print("\n")   


#now lets learn about enumerate() function:
name = "Sirajbaji"
for index, character in enumerate(name):
    print(index, character)

#more structed example of enumerate() function:
name = "Sirajbaji"
for index, character in enumerate(name):
     print(f"{index}. {character}")
print("\n")        

#as we can see in output index starts from 0, but we can change the starting index by passing a second argument to the enumerate() function. 
# For example, to start the index from 1, we can use enumerate(name, start=1).
name = "Sirajbaji"
for index, character in enumerate(name, start=1):
    print(f"{index}. {character}")
print("\n")

#numbered subjects ex:
sub = ["Math", "Science", "English", "History"]
for number, i in enumerate(sub,1):
    print(f"{number}. {i}")
print("\n")
