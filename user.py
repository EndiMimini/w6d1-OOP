from friend import Friend

class User:
    type = "Human"
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.friends = Friend()

    #methods == functions
    #class methods  cls
    #instance methods self
    #static methods 

    def introduceYourself(self):
        print(f"My name is {self.firstName} {self.lastName} and my age is {self.age}  and I have {self.friends.friendsNumber}!")
        return self
    
    @classmethod
    def myType(cls):
        print(cls.type)
        return cls
    
    def addFriend(self, user):
        self.friends.addFriend(user)
        print(f"Total number of friends of {self.firstName} {self.lastName} is {self.friends.friendsNumber} ")
        return self


    # @staticmethod
    # def validateUser(cls, data):
    #     isValid = True
    #     if len(cls.name)< 2:
    #         print("The type should be more than 2 character")
    #         isValid = False
    #     return isValid



endi = User("Endi", "Mimini", 24)
klea = User("Klea", "Manushi", 21)
enxhi = User("Enxhi", "Abazi", 21)

klea.addFriend(enxhi).addFriend(endi).introduceYourself()



