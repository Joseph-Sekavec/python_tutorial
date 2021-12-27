# To write a function in Python you start with "def" and end the function call definition with ":".

def say_hi(name, number):  # Like with for loops, we have to indent our functions.
    print("Hello there " + name)  # MUST call this function for it to execute (just like c++).
    print("Your number is: " + str(number))


# Need to have two lines after a function or the compiler will yell at you...
print("Top.")
say_hi("Dumbass", 9)  # Here we call the function.
print("Bottom.")

say_hi("Brutus", 69)

# ###################################Return Statements


def cube(num):
    return num*num*num  # We need to return a value before it will print.
    # We cannot put any code in the function after the return statement.


result = cube(3)
print(result)

result = cube(4)
print(result)


