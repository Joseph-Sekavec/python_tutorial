# We are going to learn to write and append to files.

employee_file = open("employee.txt", "a")
# a is to append to end of the file.

# employee_file.write("\nToby - Human Resources")

# employee_file.write("\nKelly - Customer Service")
employee_file.close()  # Just like in c++, we close to save.

open_employee_file = open("employee.txt", "r")

print(open_employee_file.read())


employee_file.close()

# Now we create and write a new file akin to ofstream by saying "w".
#
#

employee_file_1 = open("employee_1.txt", "w")

number = int(input("Enter the number of lines that you want: "))

for k in range(number):
    employee_file_1.write(input("Write some stuff: ")+"\n")

employee_file_1.close()

open_employee_file_1 = open("employee_1.txt", "r")
print(open_employee_file_1.read())
employee_file_1.close()


# We could also create and write to an html file:
html_file = open("file.html", "w")
html_file.write("<p> This is HTML</p>")
# To create and write an html file.

