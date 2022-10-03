class User:
    # every time a user_1 or user_2 is created this is run! (REMEMBER FOR SCHOOL SIP)
    def __init__(self):
        print("new user being created")


user_1 = User()
user_1.id = "001"
user_1.username = input("What's the first persons name?: ")

print(f"Username: {user_1.username}.\nUser ID number: {user_1.id}")

user_2 = User()
user_2.id = "002"
user_2.username = input("What's the second persons name?: ")

print(f"Username: {user_2.username}.\nUser ID number: {user_2.id}")
