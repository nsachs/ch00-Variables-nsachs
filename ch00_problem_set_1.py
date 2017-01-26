#SECTION 1 - MATH OPERATORS AND VARIABLES (20PTS TOTAL)

#PROBLEM 1 (From Math Class to Code - 2pts)

# Print the answer to the math question:
# 3(60x^2 + 3x/9) + 2x - 4/3(x) - sqrt(x)
# where x = 12.83
x = 12.83
your_answer = 3 * 60 * (x ** 2) + ((3 * x)/9) + (2 * x) - 4/(3 * x) - (x ** 0.5)
print("Problem #1:", your_answer)
print()

#PROBLEM 2 (Set your alarm - 3pts)

#You look at the clock and see that it is currently 1:00PM.
# You set an alarm to go off 728 hours later.
# At what time will the alarm go off? Write a program that prints the answer.
# Hint: for the best solution, you will need the modulo operator.
current_time = 13
elapsed_time = 728
time = 13 + 728 % 24

print("Problem #2: ", time)
print()


#PROBLEM 3 (Wholesale Books - 3pts)
#The cover price of a book is $27.95, but bookstores get a 50 percent discount.
#Shipping costs $4 for the first copy and 75 cents for each additional copy.
# Calculate the total wholesale costs for 68 copies to the nearest penny.
number_of_books = 68
total_wholesale_cost = float((number_of_books * (27.95/2)) + 4 + (0.75 * (number_of_books-1)))
print("Problem #3:", total_wholesale_cost, "dollars.")
print()

#PROBLEM 4 (Dining Room Chairs - 3pts)
# You purchase eight chairs for your dining room.
# You pay for the chairs plus sales tax at 9.5%
# Make a program that prints the amount to the nearest penny using the variables below
# Use the round(float, digits) function to get to nearest penny
chair_price = float(189.99)
tax_percent = float(0.095)
units = 8

total_cost = (chair_price * tax_percent) * units
print("Problem #4:", total_cost, "dollars.")
print()

#PROBLEM 5 (Area of Circle - 3pts)
# Write code that can compute the area of circle.
# Create variables for radius and pi (3.14159)
# The formula, in case you do not know, is radius times radius times pi.
# Print the outcome of your program as follows:
# “The surface area of a circle with radius ... is ...”
radius = float(input("Problem #5: Enter a positive value:  "))
pi = 3.1415926535

area = (pi * (radius ** 2))

print("The surface area of a cirlce with a radius", radius, "has an area of", area, ".")
print()

#PROBLEM 6 (Coin counter - 4pts)
# Write code that classifies a given amount of money (which you store in a variable named count),
# as greater monetary units. Your code lists the monetary equivalent in dollars, quarters,
# dimes, nickels, and pennies.
# Your program should report the maximum number of dollars that fit in the amount,
# then the maximum number of quarters that fit in the remainder after you subtract the dollars,
# then the maximum number of dimes that fit in the remainder after you subtract the dollars and quarters,
# and so on for nickels and pennies.
# The result is that you express the amount as the minimum number of coins needed.
count = 12.66
dollars = round(count // 1)
quarters = round(count-dollars // 0.25)
dimes = round(count-dollars-quarters) // 0.1
nickels = round(count-dollars-quarters-dimes)//0.05
pennies = round(count-dollars-quarters-dimes-nickels) // 0.01
print("Problem #6: You have", dollars,"dollars,", quarters, "quarters,", dimes, "dimes,", nickels, "nickels, and", pennies, "pennies.")

#the first part of this runs correctly, but I'm not sure why the quarters, dimes, nickels, and, pennies are all wrong.

#PROBLEM 7 (Variable Swap - 2pts)
# Can you think of a way to swap the values of two variables that does not
# need a third variable as a temporary storage?
# In the code below, try to implement the swapping of the values of 'a' and 'b' without using a third variable.
# To help you out, the first step to do this is already given.
# You just need to add two more lines of code.

a = 17
b = 23
print( "a =", a, "and b =", b)
a += b # this is the first line to help you out
# add two more lines of code here to cause swapping of a and b
b = a -b
a -= b
print( "a =", a, "and b =", b)