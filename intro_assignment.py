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
# print(today_is)
# print(calendar.today_is)
# print(today_is.weekday())
# print(calendar.day_name[week_index])


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