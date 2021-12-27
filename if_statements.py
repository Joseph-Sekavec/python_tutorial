# Let us begin by creating a sort of boolean variable.

# is_male = True
is_male = False
is_tall = True

if is_male and is_tall:  # Instead of || we just say or... well that makes sense.
    print("You are a tall male.")
elif is_male and not is_tall:  # Instead of ! or ~ we simply use not.
    print("You are a short fucker.")
elif not is_male and is_tall:
    print("You're a tall bitch!")
else:
    print("You are not a male, not tall, or not both.")

# if statements and comparisons:

# Let us take 3 parameters into a function, then print the largest number


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(12, 4, 8))


def is_equal(num1, num2):
    if num1 != num2:  # When we use == for comparison, we can say != to say not equal like C++
        print("Not equal")
    else:
        print("Is equal")

