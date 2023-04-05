class Friend:
    def __init__(self):
        self.friends = []
        self.friendsNumber = 0

    def addFriend(self, user):
        self.friends.append(user)
        self.friendsNumber +=1
        print(f"A new friend was added: {user.firstName} {user.lastName}")
        return self
