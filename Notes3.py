# --------- February 23 --------

#Insertion Sort
#iterate through the list starting at 1 through the end of list
# we are splitting our list into two parts, sorted items on the left, unsorted on the right.
#1 We iterate to the next number to sort
#2 we store the value and pos
#3 we compare val to val of pos to the immediate left.
#4 If it is bigger, we found the place for this item.  If it is smaller, we swap out the scanning position with the one to its immediate left and move
#the scan position down one to check the next item.  This repeats until we find the place it belongs.
#5 Then we put the original value in that place, and start over with the next pos.
#import random
'''
my_list = []
for i in range(5000000):
    my_list.append(random.randrange(100000))

for pos in range(1,len(my_list)):
    key_pos = pos
    scan_pos = key_pos - 1
    key_val = my_list[key_pos]

    while my_list[scan_pos] > key_val and key_pos >= 0:
        my_list[scan_pos + 1] = my_list[scan_pos]
        scan_pos -= 1

    my_list[scan_pos + 1] = key_val
print(my_list)


import turtle

my_turtle = turtle.Turtle()
my_turtle.isvisible()
my_screen = turtle.Screen()

#Draw Here
my_turtle.fillcolor("red")

my_turtle.begin_fill()
my_turtle.goto(200, 0)
my_turtle.goto(200, 200)
my_turtle.goto(0, 200)
my_turtle.goto(0,0)
my_screen.bgcolor("blue")
my_turtle.end_fill()

my_turtle.width(10)
my_turtle.up()
my_turtle.goto(-100, -100)
my_turtle.down()

my_turtle.setheading(135)
my_turtle.forward(100)

#my_turtle.begin_fill()
curl = 0.1
heading = 0

for i in range(50):
    my_turtle.setheading(heading)
    curl += 0.1
    heading += curl
    my_turtle.forward(5)
#my_turtle.end_fill()

my_screen.exitonclick()
'''

#EXCEPTIONS (use me sparingly please)

#Exception = condition that resuls in abnormal program flow
#Exception handling = what we actively do to for exceptions
#Catch = code that handles abnormal conditions
#Throw/raise = adnormal conditions THROW or RAISE Exceptions
#Unhandled exceptions = Thrown, but not caught. Program killers

#Common exception handling we might do:
#Divide by zeri error (ZeroDivisionError)
'''
x = 0
y = 2

try:
    print(y/x)
except:
    print("Invalid Operation")

#Conversion Error (ValueError)

done = False

while not done:
    try:
        user_input = int(input("Enter a valid number: "))
        done = True
    except:
        print("Number entered was not valid.")

#File opening (IOError, FileNotFoundError)
try:
    file = open("AliceInWonderland.txt")
except:
    print("Couldn't open files")

#Use the built in error types

try:
    my_file = open("myfile.txt")
    int("Hello")
    print(1/0)
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Invalid integer conversion")
except:
    print("Unknown Error")


#Exception object (grabbing the caight exception object)

try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)
'''

#RECURSION NOTES

#functions can call functions
def f():
    g()
    print("f")
def g():
    print("g")


f()


#functions can call themselves
def hello():
    print("Hello")
    #hello()

hello()

#control the level of recursion (depth)
def controlled(level, end_level):
    print("Recursion level", level)
    if level < end_level:
        controlled(level + 1, end_level)

controlled(4,20)

#make a function to calculate a factorial
def factorial(n):
    total = 1
    for i in range(2, n +1):
        total *= i
    return total

print(factorial(10))

def recursive_factorial(n):
    if(n == 1):
        return n
    else:
        return n * recursive_factorial(n-1)

print(recursive_factorial(10))


 #Zombie Apocalypse Problem

def zombie_apocalypse(zombies, humans, attacks_per_day, defense_rate, day, end_day):
    print("DAY: ", day)
    print("Humans = ", humans)
    print("Zombies = ", zombies)

    new_zombies = zombies + zombies * attacks_per_day * (1-defense_rate) - zombies * attacks_per_day * defense_rate

    humans = humans - new_zombies
    day += 1


    if humans > 0 and zombies > 0 and day < end_day:
        zombie_apocalypse(new_zombies, humans, attacks_per_day, defense_rate, day, end_day)


zombie_apocalypse(100, 6e9, 1, 0.1, 0, 100)

