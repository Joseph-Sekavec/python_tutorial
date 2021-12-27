# We are going to learn how to read from files.
# We will use something called the python read command

# To open a file we have some syntax:
# open("filename", "mode to open in")
# Ex:

# open("employee.txt, "r") r is read.
# open("employee.txt, "w") w is write.
# open("employee.txt, "a") a is append.
# open("employee.txt, "r+") r is read and write.

employee_file = open("employee.txt", "r")
# This is okay since our txt file is in the same directory.

# print(employee_file.readable())

# file_variable_name.readable() is a boolean function that
# checks if a file is indeed readable.

print(employee_file.read())  # read() actually spits out info.

# print(employee_file.readline())
# prints first line, moves cursor, just like ifs.getline().
# print(employee_file.readline())

# print(employee_file.readlines())  # reads/prints all lines

# for k in employee_file:
#    print(employee_file.readlines()[k])  # prints lines at index k.


# Without a for loop, print(employee_file.readlines()[0]) would give us our first line.
# print(employee_file.readlines()[1]) would give us our second line.
# print(employee_file.readlines()[2]) would give us our third line, etc.

employee_file.close()

# just like ifstream ifs
# ifs.open("name")
# ifs.close()
