# number = int(input("Enter a number: "))
# print(number)
# but if they don't enter a number?
# Use a try except block.
# It is similar to if(!cin>>number) else
# Or a simple switch with a default.

try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:  # ZeroDivisionError is as it sounds.
    print(err)
except ValueError:  # ValueError means our input value is invalid.
    print("Invalid input.")

# ZeroDivisionError as err stores our error to
# a variable err. Here our built in error is
# ZeroDivisionError in Python...


# Our syntax is this:

# try:
# what we want to do
# except type of error to look for:
# What do do if we have the error so it doesn't crash.
