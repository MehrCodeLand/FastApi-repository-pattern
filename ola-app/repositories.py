from typing import List
from models import User , Language
from schemas import UserCreate
import json



# database         
DATABASE_PATH = 'db.json'
         
class DatabaseRepository:
    def __init__(self):
        pass
        
    # updated database method
    def write_database(self , data):
        with open(DATABASE_PATH , 'w') as file_json:
            json.dump(data , file_json)
            
    def read_database(self):
        with open(DATABASE_PATH , 'r') as file_json:
            return json.load(file_json)
        
    def add_user(self,user:User):
        data = self.read_database()
        data["Users"][user.id] = {"username": user.username , "password":user.password}
        self.write_database(data)
    
    def get_all_user(self):
        data = self.read_database()
        return data["Users"]
    
    


# implement database repository here 


class UserRepository:
    def __init__(self):
        self.users = [] # in memory data-base
        
    def create_user(self , user:User ):
        new_user = User(
        id=user.id,
        username=user.username,
        password=user.password
    ) 
           
        db = DatabaseRepository()  
        data = db.get_all_user()
        data["Users"][user.id] = {"username":user.username , "password":user.password , "language_id" : None}         
        
        db.add_user(new_user)
        return new_user        
        
    def get_users(self) -> List[User]:
        db = DatabaseRepository()
        return db.get_all_user()
        
        
        
class LanguRepository:
    def __init__(self):
        self.languages = [] # in memory data-base
        
    def create_language(self , languages: Language ):
        new_language = Language(
            id=languages.id ,
            name= languages.name ,
            hola = languages.hola
            )
        database_here = DatabaseRepository()
        database_here.write_database_User()
        self.languages.append(new_language)
        
        return new_language
  
  
