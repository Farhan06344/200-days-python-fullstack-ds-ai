#DAY : 8  Nested loops and Patterns problems

#as we know the normal loop
#now i'll learn abt the nested loops in for and while
#simple nested loop for printing
# 0 1 2
# 0 1 2
# 0 1 2
for i in range(3):
    for j in range(3):
        print(j,end=" ")
    print()    
print("\n")
#now lets print sqaure of pattern:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

for i in range(5):
    for i in range(5):
        print("*",end=" ")
    print()    
print("\n")    

#lets print rectangle 
#* * * * * * * * * *
#* * * * * * * * * *
#* * * * * * * * * *
#* * * * * * * * * *

for i in range(1,5):
    for j in range(1,11):
        print("*",end=" ")
    print()
print()        

#now lets print a right angle triangle
#*
#* *
#* * *
#* * * *
#* * * * *

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()        

#now lets print inverted triangle 
#* * * * *
#* * * *
#* * * 
#* * 
#* 

for i in range(5,0,-1):
    for  j in range(i):
        print("*",end=' ')
    print()
print()    

#print pattern:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')

    print()
print()        


#print pattern:
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

for i in range(1,6):
    for j in range(i):
        print(i,end=' ')
    print()
print()

#print the pattern 
#1 2 3 4 5
#1 2 3 4
#1 2 3
#1 2
#1

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print()

#print pyarmid
#     *         
#   * * *
#  * * * *
# * * * * *
#* * * * * *
n=5 #n=rows

for i in range(1,6):
    for j in range(i,5):
        print(" ",end=' ')
    for k in range(1,(i*2)):
        print("*",end=' ')   
    print() 
print()


for i in range(1,6):
    for j in range(i,5):
        print(" ",end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    print()
print()    

#to print a diamond
for i in range(1,6):
    for j in range(i,5):
        print(" ",end=' ')
    for k in range(1,(i*2)):
        print('*',end=' ')
    print()
     
for i in range(4,0,-1):
    for j in range(5,i,-1):
        print(" ",end=' ')
    for k in range(1,(i*2)):
        print("*",end=' ')
    print()
print()    