# We desire to make an improved calculator

num1 = float(input("Enter first number: "))
op = input("Enter your operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator!")

# character = ["bob", "bill", "Raymond"]

# print(character.index("Raymond"))
# character.append("Fucktard")
# print(character)
# char = "Hello there my friend"
# print(char.replace("Hello", "Goodbye"))
# print(char.replace("Hello", "\n"))

