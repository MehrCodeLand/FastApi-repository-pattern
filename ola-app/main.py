from fastapi import FastAPI , Depends

# inner files 
# ( schema for data validation we dont use  )
from models import  User , Language
from repositories import UserRepository , LanguRepository , DatabaseRepository
from services import UserService , LanguageService , DatabaseService

app = FastAPI() 

# repository check and constructor
def get_user_repository():
    return UserRepository()

def get_languages_repository():
    return LanguRepository()


# impliment services
def get_user_service(
    user_repository: UserRepository = Depends(get_user_repository)
    ): return UserService(user_repository)

def get_language_service(
    language_repository: LanguRepository = Depends(get_languages_repository)
): return LanguageService(language_repository)
 




# user HTTP leyer
@app.get("/users/get-all")
def get_all_user(
    user_service: UserService = Depends(get_user_service)
): return user_service.get_all_user()
    
@app.post("/users/")
def create_user(
    user: User, user_service: UserService = Depends(get_user_service)
    ): return user_service.create_user(user)

@app.post("/users/get-one-user")
def get_user_by_id(
    user_id , user_service: UserService = Depends(get_user_service)
):return user_service.get_one_user(user_id)


@app.post("/user/remove-by-id")
def remove_user(
    user_id , user_service : UserService = Depends(get_user_service)
): return user_service.remove_user(user_id)

# languages HTTP leyer
@app.post("/languages/create-languages")
def create_languages(
    language: Language , language_service: LanguageService = Depends(get_language_service)
): return language_service.create_language(language)