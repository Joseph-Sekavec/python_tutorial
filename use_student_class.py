from intro_classes_and_objects import student
# from our file, import the student class

student1 = student("Jim", "Business", 3.1, False)

# We don't use self during instantiation, that is just a keyword like __init__

print(student1.name +" " + student1.major)