#NOTES
# VARIABLES

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