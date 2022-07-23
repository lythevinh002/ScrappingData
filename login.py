import json

# Load the data from database
def loaddata(filename):
    f = open(filename)
    data = json.load(f)
    f.close()
    return data

users = loaddata('users.json')

for i in users["users"]:
    print(i)

