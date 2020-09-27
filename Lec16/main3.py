import pickle

class User:
    def __init__(self, name):
        self.__name = name 

    def __str__(self):
        return "User <name : {}>".format(self.__name)

with open('class.pickle', 'wb') as fhand:
    pickle.dump(User, fhand)

NewUser = None
with open('class.pickle', 'rb') as fhand:
    NewUser = pickle.load(fhand)

nu = NewUser('Bob')
print(nu, type(nu))