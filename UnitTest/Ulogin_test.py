# Author: The Vinh Ly
# Unit test for login

import sys

sys.path.insert(0,'..')

from loginModel import loginModel

new_login = loginModel(filename="../users.json")
new_login.loaddata()

def test_user_exist():
    print('this is from feature-z')
    assert new_login.checkUserAvailable(email="abc@gmail.com") == True