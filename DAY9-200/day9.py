#DAY 9 :String Deep Dive: indexing,slicing ,methods

#strings : string is the sequence of character
name = "farhan"
print(f"The varible name contains data {name} in it and it is of type {type(name)}")
print()
#if the sentence to be printed has inverted commmas in sentence there are ways to perform it :
print("heyy it's me ,hows going on!")
print()
print("i was in a jungle when i saw a man eating lion who was so scared by village people ,he was named as the \"kaali\"")
print()
#for the multi line text we use the format :
msg = """hello good evening to everyone,
my name is mohammed farhan i'm from gunjimutt.
currently i'm persuing my bachelors in engineering inthe field of data science."""

print(msg)
print()

#string indexing:a string is a sequence of characters and each character has its indexand indexing means accessing the specified element of index in the string
#there's two type in indexing :
#1.positive indexing
#2.negative indexing

name = "Mohammed Farhan"

print(name[0])
print(name[8])
print()
#accessing every character
for character in name :
    print(character)

print()

#len
print(len(name))
print()
c = 'far'
print(len(c))
print()

#negative indexing:

print(name[-1])
print()
print(name[-2])
print()
print(name[-4]) 
print()
#stings are immutable,that means once a string is created it can can be replaced but not be changed by index

#to change the string we use :
new_name = name.replace("Farhan","Faizan")
print(new_name)
print()

#srting slicing means accessing a part of the string unlike the indexing where it can access only the individual elemnt  
print(name[0:8])
print()

print(name[9:15])
print()

print(name[2:])
print()

print(name[:2])
print()

#slicin with stpe

print(name[0:9:2])
print()
print(name[9:15:3])
print()
print(name[::2])

#reversing the string using the reverse indexing
print(name[::-1])
print()
print(name[-1:-5:-2])
print()

#string concatenation
last_name = 'Sirajbaji'
full_name = name+' '+ last_name
print(full_name)
print()

#repeatation:
print("ayoo"*10)
print('*'*5)
print()

#use of membership operator(in,not in):

print("farhan" in name)
print("Farhan" in name)

#upper():

print(name.upper())
print(name)
print()

#lower():
print(name.lower())
print()

#capitalize():
c = 'horse'
print(c.capitalize())
print()

#title()

b = 'data structure and analysis'
print(b.title())
print()

#find:
print(name.find('Farhan'))
print(name.find('farhan'))
print()
#index():
print(name.index('Farhan'))
#print(name.index('farhan'))
print()

#count()
print(name.count('a'))
print(name.count('z'))
print(name.count("Farhan"))

#split():

c = "there will be always a debate abt the goat between messi and ronaldo"
print(c.split())
print()

#join():
a = ['messi','is','one','of','the','best','footballer']
b = ' '.join(a)
print(b)
b = '-'.join(a)
print(b)

#isalpha()	Checks alphabetic characters
#isdigit()	Checks digits
#isalnum()	Checks letters/numbers
#isspace()	Checks whitespace
#startswith()	Checks beginning
#endswith()	Checks ending

