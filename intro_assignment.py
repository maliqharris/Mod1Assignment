# -----------------------------------------------------------------------------------------Assignment 1----------------------------------------------------------------------------------------------
# Create a program that asks the user for their name and then prints a personalized greeting. The program should also show them the length of their name and display their name in uppercase letters.


import calendar
# calander.day_name returns a list of the days of the week so we dont have to make one ourselves so we import calander
import datetime
#We use datetime to get the date

# from datetime import date

today_is = datetime.date.today() 
#Gives us the date of today 
# YYYY-MM-DD

week_index = today_is.weekday()
# Gives is a number corosponding to the day of the week - 0 is Monday, 1 is tuesday and so on

# -------------------Tests-------------------------
# print(today_is)                                 |
# print(calendar.today_is)                        |
# print(today_is.weekday())                       |
# print(calendar.day_name[week_index])            |
# -------------------------------------------------

first_name = input("What is your first name?")
# set variable for first name
last_name = input("What is your last name?")
# set variable for last name

first_name_length = len(first_name)
#  set variable for length of first name
last_name_length = len(last_name)
# set variable for length of last name

print(f"Hello {first_name[0].upper() + first_name[1:]} {last_name[0].upper() + last_name[1:]}, I hope you are having a good {calendar.day_name[week_index]}!")
# first character of name made uppercase + the rest of the name or 2nd character of name onwards  - using slice [start:end:steps iteratiing on] -- calander.day_name is a list of weeks at index [week_index]

print(f"The length of your first name is {first_name_length}!")
print(f"The length of your last name is {last_name_length}!")
print("Wow!")
print(f"Your name in uppercase would look like {first_name.upper()} {last_name.upper()}!")


# -----------------------------------------------------------------------------------------Assignment 2----------------------------------------------------------------------------------------------
# Create a program that asks the user for a positive number `n` and then prints the sum of all the numbers from 1 up to `n`. For example, if `n` = 5, the program should print the sum 1+2+3+4+5 = 15.


input_number = int(input("Enter any number!"))
# int catches the edgecase of not being a number 

current = 1
# Start at 1
final = 0
# Initialize sum value 

while current <= input_number:
# while current value is less than or equal to our inputed value
    final += current
    # current is added to sum 
    current += 1
    # we increment by 1 and continue the loop
    # loop stops when the current number we are on is equal to the inputed value
    
# print(final)
print(f"The sum of all the numbers leading up to {input_number} is {final}!")


# -----------------------------------------------------------------------------------------Assignment 3----------------------------------------------------------------------------------------------
# Create a program that asks the user for a sentence (or any string of text) and then counts how many vowels (a, e, i, o, u) are in that sentence. Print the total number of vowels found.

string = input("Say anything!")

string_converted = string.lower()
# converted to lowercase , alternativly we could check for uppercase as well



vowels = 0
#  init vowel count

for char in string_converted:
    if char in "aeiou":
        vowels += 1

print(f"The amount of vowels in what you said is {vowels}!")





# Edgecase for first_name
space = 0
for char in first_name:
    if char in " ":
        space += 1

real_length = first_name_length - space 

print(f"Your first name without and spaces would be {real_length}")

# reusable 
def real_length2(name):
    space2 = 0
    for char in name:
        if char == " ":
            space2 += 1
    return len(name) - space2
print(f"The amount of letters in your first name would be {real_length2(first_name)} without spaces. "
      f"Your last name would have {real_length2(last_name)} letters without spaces.")
