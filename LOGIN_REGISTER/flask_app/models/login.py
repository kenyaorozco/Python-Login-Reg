print("model file running")

# from types import ClassMethodDescriptorType
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# bcrypt = Bcrypt(app) 
# from flask_bcrypt import Bcrypt        

class Login:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL('login_register_schema').query_db(query,data)
        # Didn't find a matching user
        if len(results) < 1:
            # print (len(results))
        #     return True
        # else:
            return False 
        #     print(result)  
        return cls(results[0])

    @classmethod
    def save(cls,data):
        query = "INSERT INTO user (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"

        new_user = connectToMySQL('login_register_schema').query_db(query,data)
        return new_user

    @staticmethod
    def validate_user(data):
        is_valid = True

        if len(data["first_name"]) < 1:
            is_valid = False
            flash("Invalid Name")
        
        if len(data["last_name"]) < 1:
            is_valid = False
            flash("Invalid last name")

        if len(data["email"]) < 1:
            is_valid = False
            flash("BOO TOMATO TOMATO")

        if len(data["password"]) < 1:
            is_valid = False
            flash("input password")

        return is_valid
    # @staticmethod
    # def validate_login(data):
    #     is_valid = True

    #     if data["email"] == Login["email"]:
    #         is_valid = False
    #         flash("invalid email")

    #     if data["password"]:
    #         is_valid = False
    #         flash("invalid password")

    #     return is_valid
# create a regular expression object that we'll use later   
    @staticmethod
    def validate_login( login ):
        is_valid = True
# test whether a field matches the pattern
        if not EMAIL_REGEX.match(login['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid





