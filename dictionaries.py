# We can convert 3 digit month name to full name
# ex: Jan -> January
# When we create dictionaries in Python, we make it in syntax
# dictionary_name = { }

monthConversions = {
    "Jan": "January",  # We create a key : value,
    # That is, we put a #key : value it represents,#
    "Feb": "February",
    "Mar": "March",  # Notice we put our 3 letter month then
    # a colon then the thing it means then a comma.
    "Apr": "April",  # The thing on the left of the colon
    # is called the key, the thing on the right is called
    # the value...
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}  # Almost similar to structs and classes.

# To access a key we say dictionary_name[key_name]:
print(monthConversions["Nov"])
# or dictionary_name.get(key_name)
print(monthConversions.get("Dec"))
# Or... we can use the .get function to get a default val.
print(monthConversions.get("Luv", "Invalid"))
# Our second parameter is our default statement for if we
# don't enter a valid key.
print(monthConversions.get("Mar", "Invalid"))