import string
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash

users_dict = {}

class Users():
    
    def __init__(self):
        self.oneuser_dict = {}

    def put(self,username, name, email, password,role):
        
        if username in users_dict:
            return {"message":"Username already exists"}
        
        self.oneuser_dict["name"] = name
        self.oneuser_dict["email"] = email
        self.oneuser_dict["username"] = username
        self.oneuser_dict["role"] = role
        pw_hash = generate_password_hash(password)
        self.oneuser_dict["password"] = pw_hash

        users_dict[email] = self.oneuser_dict
        return {"message":"{} registered successfully".format(email)}

    def verify_password(self,password,email):
       
        if email in users_dict:
            # result = check_password_hash(users_dict[email]["password"], password)
            # if result is True:
            return "True"
            
        return {"message": "email does not exist "}
    def get_user_by_email(self,email):
        if email in users_dict:
            return users_dict[email]
        return {"message":"User not found"}