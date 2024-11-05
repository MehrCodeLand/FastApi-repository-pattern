from typing import List
from models import User , Language
import json



# database         
DATABASE_PATH = 'db.json'
         
class DatabaseRepository:
    def __init__(self):
        pass
        
    def write_database(self , data):
        with open(DATABASE_PATH , 'w') as file_json:
            json.dump(data , file_json)
            
    def read_database(self):
        with open(DATABASE_PATH , 'r') as file_json:
            return json.load(file_json)
        
    def get_one_user(self , user_id):
        data = self.read_database()
        user = data["Users"][user_id]  
        user["id"] = user_id      
        return user
        
     
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
        db.add_user(new_user)
        return new_user        
        
    
    
    def remove_user(self , user_id):
        user = self.get_one_user(user_id)
        db = DatabaseRepository()
        data = db.read_database()
        # time to removing obj 
        if user["id"] in data["Users"]:
            del data["Users"][user["id"]]
            db.write_database(data)
            return "deleted"
            
    def update_user(self , user:User):
        db = DatabaseRepository()
        data = db.read_database()
                
        self.remove_user(user.id)
        self.create_user(user)
        return user
                
    def get_one_user(self , user_id):
        db = DatabaseRepository()
        user = db.get_one_user(user_id) 
        return user   
        
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
        self.languages.append(new_language)
        
        return new_language
  
  
