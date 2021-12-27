# We create a list similarly to how we create a Python variable...
# Our syntax is variable_name = [value_1, value_2, ..., value_n]. Lists are basically arrays.
friends = ["Kevin", "Karen", "Jen"]  # We can also make values that are not strings...

# If we just say print(list_name), we get the whole list.

print(friends)


# We can access list elements in the same way we do with arrays.

print(friends[1])  # This prints the element in the list called "friends" at index 1.

print(friends[-1])  # using negative indexes lets us access elements from end to beginning instead starting at
# -1 = end position, whereas 0 is start position if we don't do negative numbers...

print(friends[1:])  # This accesses each element greater than or equal to 1.

print(friends[1:3])  # This includes all elements from 1 up to but not including 3.

friends[1] = "Mike"  # We can update our values at any index in our lists.

lucky_numbers = [4, 8, 15, 16, 23, 42]

friends.extend(lucky_numbers)  # Extend function allows us to take a list, and append another list onto the end of it.
# syntax is: list_name_1.extend(list_name_2)

print(friends)

# We also have the append function which allows you to add another element to the back of the list.

friends.append("Creed")  # Similar to vector_name.push_back(input_element) in C++
print(friends)
# The difference between extend and append is that extend adds on a list, append adds an element to your list.

# There is another list function called insert
# The syntax is list_name.insert(index_number, element) and it will shift the elements after by 1 to the right.
friends.insert(1, "kelly")

print(friends)

friends.remove("Mike")  # Removes specified element from your list.

print(friends)
friends.pop()  # pops last element out of our list. pop() is just the opposite of append().
print(friends)


print(friends.index("Kevin"))  # Prints the index number where "Kevin" is located.
# The syntax for index is list_name.index(name_of_element_to_check_for).

print(friends.count("Jim"))  # Prints number of times "Jim" appears.
# The syntax for count is list_name.count(name_of_element).

# variable_name.sort() will put your list in alphabetical or ascending order depending on if you have strings or
# numbers. For example:

# friends.sort()  # If there were not integers, this would sort alphabetically
lucky_numbers.sort()
# Syntax is list_name.sort()

print(friends)
print(friends)
print(lucky_numbers)

lucky_numbers.reverse()  # will reverse order.
# Syntax is list_name.reverse.

friends_2 = friends.copy()  # similar to strcpy(destination, source) in C++

friends.clear()  # Clears all elements in your list.
# Syntax for clear is list_name.clear()

friends_3 = []

for k in range(3):
    friends_3.append(" ")
print(friends_3)

print(friends)
print(friends_2.index("Kevin"))

# print(range(2))
# for k in range(3):
#    friends_3[k] = friends_2[k]

# print(friends_3)

# for k in range(3):
#    print(k)
