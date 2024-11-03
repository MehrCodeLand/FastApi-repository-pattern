from models import User , Language
import json


class Database:
    def __init__(self):
        self.load_database()
        self.find_index()
        
    def find_index():
        index_users = len(database["Users"])
        index_languages = len(database["Languages"])
        
    def load_database():
        with open('database_file.json') as json_file:
            
            database = json.load(json_file)
            print(database)

    def write_database_User(user:User):
        with open('database_file.json' , 'w') as json_file:
            user.id = index_users + 1  
            json.dump(user , json_file , )
            
    # updated database method
    def write_database(data):
        with open(DATABASE_PATH , 'w') as file_json:
            json.dump(data , file_json , 4)
            
    def read_database():
        with open(DATABASE_PATH , 'r') as file_json:
            return json.load(file_json)



# language = Language(
#     id="1",
#     name="farsi",
#     hola="salam"
# )


# database["Users"]["2"] = {
#     "name": "mehrshad",
#     "hola": "salam"
# }

# database["Users"]["3"] = {
#     "name": "mehrshad",
#     "hola": "salam"
# }
# print(database)

