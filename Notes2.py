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
'''
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

