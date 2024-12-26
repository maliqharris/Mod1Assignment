# -----------------------------------------------------------------------------------------Assignment 1----------------------------------------------------------------------------------------------
# Create a program that asks the user for their name and then prints a personalized greeting. The program should also show them the length of their name and display their name in uppercase letters.
import calendar
import datetime
# from datetime import date

today_is = datetime.date.today()
week_index = today_is.weekday()
# print(today_is)
# print(calendar.today_is)
# print(today_is.weekday())
# print(calendar.day_name[week_index])


first_name = input("What is your first name?")
last_name = input("What is your last name?")

first_name_length = len(first_name)
last_name_length = len(last_name)

print(f"Hello {first_name[0].upper() + first_name[1:]} {last_name[0].upper() + last_name[1:]}, I hope you are having a good {calendar.day_name[week_index]}!")

print(f"The length of your first name is {first_name_length}!")
print(f"The length of your last name is {last_name_length}!")
print("Wow!")
print(f"Your name in uppercase would look like {first_name.upper()} {last_name.upper()}!")