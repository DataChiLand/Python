class User:
    def __init__(self, user_id,username):
        self.id = user_id
        self.undername = username
        self.followers = 0
    
    def follow(self, user):
        user.followers += 1
        self.followers += 1
        print(f"{self.undername} is now following {user.undername}.")
        print(f"{user.undername} now has {user.followers} followers.")
        print(f"{self.undername} now has {self.followers} followers.")


user_1 = User("001", "John")
user_2 = User("002", "Michelle")
        
    
user_1.follow(user_2)
print(user_1.followers)
print(user_2.followering)
print(user_1.following)
print(user_2.followers)
