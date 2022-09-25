year = int(input("Which year do you want to check?\n"))

if year % 4 == 0:
    print("Leap year.")
elif year % 1 == 0:
    print("Not leap year.")
