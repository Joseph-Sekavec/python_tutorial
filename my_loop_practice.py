phrase = input("Input a phrase: ")
length = len(phrase)
number = 1

for k in range(length):
    print(k)

while number <= 5:

    print("Your number is now: " + str(number))
    number = number + 1

    # print("You are a dumbass.")
print("You are a dumbass")  # White space actually matters...

print(range(6))

for k in range(2):  # This will print 0,1 so if we say range(n) we execute from 0 to n-1 times.
    print(k)

character_string = "Hello, my name is Joseph"

for letter in character_string:
    print(letter)

character = ["Hello", "my", "name", "is", "Joseph"]

for word in character:
    print(word)

