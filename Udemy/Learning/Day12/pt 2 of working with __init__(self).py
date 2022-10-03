class User:
    # every time a user_1 or user_2 is created this is run! (REMEMBER FOR SCHOOL SIP)
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        # if I were to type this it would set all users to a value of 0 followers to start:
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", input("What's your name?:\n"))
print(user_1.id, user_1.username)

user_2 = User("002", input("What's their name?:\n"))
print(user_2.id, user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
