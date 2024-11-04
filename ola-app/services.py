from repositories import UserRepository , LanguRepository , DatabaseRepository
from models import Language , User


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        
    def create_user(self, user: User):
        return self.user_repository.create_user(user)
    
    def get_all_user(self):
        return self.user_repository.get_users()
    
    def get_one_user(self , user_id):
        return self.user_repository.get_one_user(user_id)
    def remove_user(self, user_id):
        return 
    
    
class LanguageService:
    def __init__(self , language_repository: LanguRepository):
        self.language_repository = language_repository
        
        
    def create_language(self , languages: Language):
        return self.language_repository.create_language(languages)
        
        
class DatabaseService:
    def __init__(self , database_repository: DatabaseRepository):
        self.database_repository = database_repository
        
    def read_database(self):
        return self.database_repository.read_database()
    
    def write_database(self , data):
        return self.database_repository.write_database(data)
    
    