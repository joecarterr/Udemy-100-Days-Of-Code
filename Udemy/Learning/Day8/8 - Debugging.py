import random
from random import randint


# Describe Problem
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# because the range goes up to 20 however code in this case would have to go to 21 instead of 20

# Reproduce the Bug
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
if 1980 <= year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

# Fix the Errors
age = int(input("How old are you?:\n"))
if age > 18:
    print(f"You can drive at age {age}.")

# Print is Your Friend
num_of_pages = 0
num_of_words_per_page = 0
pages = int(input("Number of pages: "))
words_per_page = int(input("Number of words per page: "))
total_words = pages * words_per_page
print(total_words)


# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate(a_list=[1, 2, 3, 5, 8, 13])
