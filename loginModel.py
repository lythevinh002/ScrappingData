import json

class loginModel:
    def __init__(self, filename, data = []) -> None:
        self.filename = filename
        self.data = data

    # Load the data from database
    def loaddata(self):
        f = open(self.filename)
        self.data = json.load(f)
        f.close()

    def checkAvailable(self, typechecking, arg):
        for i in self.data["users"]:
            print(i)
            if i[typechecking] == arg:
                return True
        return False

    # test the existing user
    def checkUserAvailable(self, email):
        for i in self.data["users"]:
            print(i)
            if i["email"] == email:
                return True
        return False

# users = loaddata('users.json')

# print(checkUserAvailable(users["users"], "abc@gmail.com"))