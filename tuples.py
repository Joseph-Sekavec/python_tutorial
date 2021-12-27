# Tuples are structures where we can store different pieces of information...
# Unlike lists which use [], we make tuples by saying var_name = (stuff).

# And example of tuples is (x,y) coordinates. Tuples are immutable (cannot be changed after declaration similar to
# array).

coordinates = (4, 5)

print(coordinates[0])  # This prints 4. THus our indexing is similar to lists and arrays.
print(coordinates[1])  # This prints 5.

# coordinates[1] = 10 gives us an error because we cannot change a tuple at runtime.
# We can make a list of tuples...

coord_list = [(4, 5), (6, 7), (12, 19)]  # The tuples cannot be changed however.

print(coord_list[0])  # We can access an entire tuple in our list
print(coord_list[0][0])  # Or we can access an individual element in a tuple in our list...

print(coord_list[-1][-2])




