programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected",
                          "Function": "A piece of code that you can easily call over and over again",
                          "Loop": "The action of doing something over and over again"}

# print(programming_dictionary)

# CREATE AN EMPTY DICTIONARY
empty_dictionary = {}

# WIPE AN EXISTING DICTIONARY
# programming_dictionary = {}
# print(programming_dictionary)

# EDIT AN ITEM IN A DICTIONARY
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# LOOPING THROUGH A DICTIONARY
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
