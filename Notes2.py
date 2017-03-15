
#NOTES

# VARIABLES
'''
#variables assignment and names
camelCase = "No"
snake_case = "Yes"

x = snake_case + camelCase

#multiple variable assignment

a,b = (10, 20)
print(a, b)

# math and operators
x = 5
y = 5 * x + x - x / x
print(y)

print(13 % 5) # print the remainder
print(13 // 5) #chops off remainder and gives a whole number
print(2 ** 3 ) # raising to a power (and square roots)



# Pemdas, spacing, and parentheses
x = y * 5 * (4 + 3)

# math Library
import math
x = math.pi
print(math.cos(x))

#round, absolute values
print(abs(-5))

print(round(12.8398475934857, 2))
print(round(1238.879394, -2))

x = round(3.23984, 1)
print(x)
x = x + 4.2
print(x)
#round at the very end, don't round variables


#print statements, mutples items
print(3, "yes")
print("Hello" + "World")
print("Score" + str(300))

name = "Francis Parker"
print(name.upper())


#input function
#my_input = input("Enter something: ")
#print(my_input + 5)

#str, int, float
#floats are for decimals


#escape codes
print("Escape \\")
print("Escape \nme \t me too\"")

#concatenation

#LOOPS

#While Loops

done = False
while not done:
    print("Not Done")
    done = True

count = 0
while count < 1000:
    count +=1
    print(count)
print("done")

#For Loops and ranges
for i in range(10):
    print(i)

for i in range(5,10):
    print(i)

for i in range(100,200,10):
    print(i)

for i in range(10,0,-1):
    print(i)

for i in range(10):
    for j in range(100):
        print("*", end = " ")
    print()

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                number = str(a) + str(b) + str(c) + str(d)
                number = int(number)
                print(number)


#continue, break, and else
for i in range(100):
    if i == 50:
        break
    print(i)

#breaks take you out of the loop

for i in range(-5,10):
    if i == 0:
        continue
    print(50/i)
#continue skips things

for i in range(1000):
    pass

for i in range(4):
    user_input = int(input("Enter a number between 0 and 100: "))
    if user_input < 0 or user_input > 100:
        break
else:
    print("Thank you for entering your numbers.")


import random
random.randrange(0,100, 5)
random.random()

#functions
def main():
    def hello():
        print("Hello")

        hello()

    def line(m,x,b):
        y = m*x + b
        print(y)

    line(3,8,2)

    def double(a):
        return a * 2

    print(double (10))
    num = double(20)
    print(num)


    def add_product(a,b):
        add = a + b
        product = a * b

    return add, product
        add_product(3,4)

    print(add_product(3,4))

#scope
x = 10

def fun():
    #x +=1
    #y = 10
    print(x)

fun()
print(y)

# you can access but cannot change global variables

#main function
#if __name__ == 'main'

if __name__ == "__main__":
    main()
#-----Jan 30 ---------

def fun(param):
    print(param)

fun(10)

#anonymous functions with lambda (function shortcut)
#obj_var = lambda params: function
# make a lambda function to add numbers

add_two = lambda num1,num2: num1 +num2
print(add_two(2, 3))

#iterating through a list (2 ways... now 3)

this_list = [5, 10, 15, 20, 25]

for number in this_list:
    print(number)
    number += 1
    print(number)

print(this_list)

for i in range(len(this_list)):
    print(this_list[i])
    this_list[i] += 1

print(this_list)

#python'a map function (iteration shortcut)
# map (functions, list)
print(list(map(lambda x: x**2, this_list)))
print(this_list)

#index and slicing lists
my_list = [1,2,3,4,5,6,7]
my_list2d = [[10,20], [30,40], [50,60]]

print(my_list[0])
print(my_list[3:5])
print(my_list[3:])

print(my_list2d[0])
print(my_list2d[0][0])
print(my_list2d[2][1])
print(my_list2d[1:][1][0])


#list methods
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

a[0] = 10
print(a)

#append (adds to the end of a list)
a.append(4)
print(a)

#extend (adds two lists together)
#a.append([2,3])
a.extend([2,3])
print(a)
a.extend(b)
print(a)

#insert(index,value) (place object at the index)
b.insert(2,100)
b.insert(2,5)
print(b)

#remove(index) (item you want to remove)
b.remove(5)
print(b)

#pop(index) (returns item removed)
first_in_line = c.pop(0)
print(c)
print(first_in_line)

#count (how many of these do I have in the list)
print(a.count(4))
print(a)

#reverse (performed on list)
a.reverse()
print(a)

#conditions
a = True
b = False

if not a:
    print("not")
if a:
    print("yes")
if a != b:
    print("Not equal")
# ----- February 2 ------#
# Modules and libraries have advantages.
'''
#What it does...
#When you import a file, it automatically runs the code.
#It also pulls all the def, varialbes, classes, etc. into your program for use (as long as you know how to call on them)
#Using if __name__ == "__main__" in your modules
'''
import importme
print("Hello from", __name__)

print(importme.my_var)

#general import and scope
#multiple library import s
#import name of library
import math, random

print(random.randrange(100))
print(math.pi)


#local import and scope
#wildcard imports (and why we won't generally use them)
#from name_of_library import name_of_object, object(s)
from math import pi
print(pi)

from math import *
print(e)
print(cos(pi))

#importning under alternate name (save some typing or clarity)
#import name_library as alt_name

import math as m
print(m.cos(m.pi))

# available libraries, installing libraries
# help("modules") is useful

# creating your own library/module

importme.print_stuff()

#pitfalls (circular imports and name making
random.randrange(100)

#python packages, __init__.py, and dot notation

# ------- February 6 ---------#
########
#Using files
########

#opening files
# open ("name.ext", "r, w, or a")
#writing to files
#open("name.ext", "W")
#file.write(string)
#closing files
#file.close()
import random

file = open("my_file.txt", "w")
file.write("Hello file!" + "\n")
for i in range(100):
    file.write(str(i) + "\n")
file.close()

#reading a file
#open ("name.ext", "r")
file = open("my_file.txt", "r")
for line in file:
    print(line, end = " ")
file.close()
'''
# ----- February 9 ------- #
'''
#open file to read
file = open("super_villian.txt", "r")
villain_list = [] #creat list/array to read info
#loop through file to build list
for line in file:
    villain_list.append(line.strip())# use line.strip() to take spaces off and \n

print(villain_list)

#linear search
#set a key and index
key = "The Deadly Raven"
i = 0

#cycle through index while it is not == key and check it i is less that len(list)
while villain_list[i] != key and i < len(villain_list):
    i += 1

if i <len(villain_list):
    print("Found", key, "at position", i) #that means you found it at position
else:
    print("Key is not in list") #else means you didn't find it


#linear searches are time and resource hogs
#thre must be a better way.
#number guesssing game

import random
target = random.randrange(1, 101)
guess = 0

while guess != target:
    guess = int(input("guess a number between 1 and 100: "))
    if guess > target:
        print("Too high")
    elif guess < target:
        print("Too low")
    elif guess == target:
        print("correct")


#Binary Search
print("Alligator" > "Apple")

key = "Aldric Foxe"
lower_bound = 0
upper_bound = len(villain_list) - 1

found = False

while lower_bound <= upper_bound and not found:
    middle_pos = (lower_bound + upper_bound) // 2

    if villain_list[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villain_list[middle_pos] > key:
        upper_bound = pos - 1
    else:
        found = True

if found:
    print("Found", key, "at position", middle_pos)
else:
    print(key, "not in list")


# ------- February 10 ------- #
import re

def split_line(line):
    #This function takes in a line of text
    #a list of words in the line
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

print(split_line("Hello, how are you?"))

file = open("AliceInWonderland", "r")

alice = 0

for line in file:
    #print(line.strip())
    words = split_line(line)
    #print(words)
    for word in words:
        #print(word.upper())
        if word.upper() == "ALICE" or word.upper() == "ALICE'S":
            alice += 1
print(alice)

'''
# ------- February 22 --------- #
list = ["abe", "bev", "cam", "dan", "eve", "flo"]

#Swapping
temp = list[0]
list[0] = list[1]
list[1] = temp
print(list)

list[4], list[5] = list[5], list[4]
print(list)

#Selection Sort

import random

my_list = []

for i in range(500):
    my_list.append(random.randrange(100))
print(my_list)

for pos in range(len(my_list)):
    min_pos = pos
    for scan_pos in range(min_pos, len(my_list)):
        if my_list [scan_pos] < my_list[min_pos]:
            min_pos = scan_pos
    temp = my_list[pos]
    my_list[pos] = my_list[min_pos]
    my_list[min_pos] = temp

print(my_list)



