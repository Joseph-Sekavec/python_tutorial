phrase = "Giraffe was named \" George \" \n"
print(phrase + "is cool \n") #Note + is a concatonation operator. Here we concatonated "George" to phrase.
print(phrase.lower() + "\n") #sting_name.lower() makes all lowercase
print(phrase.upper() + "\n") #string_name.upper() makes all uppercase...

print(phrase.isupper())
print(phrase.islower())

print("\n")


print(phrase.lower().islower())
print(phrase.upper().isupper()) #We can use these operators one after antoher...

print("\n")
print(len(phrase)) #len(string) gives string length. This is equal to strlen in c++

#We can get an element of a string...



print(phrase[0]) #This gives us the character at index 0, which is now G

#If we want to know where a particular character or string is, we use the index function:
print(phrase.index("G"))

#This is how to use the replace function (Basically the copy function in c++).
print(phrase.replace("GIRAFFE", "Elephant"))