from pydantic import BaseModel
from typing import Optional

class LanguageBase(BaseModel):
    name: str
    hola: str

class LanguageCreate(LanguageBase):
    pass

class Language(LanguageBase):
    id: str

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    password: str

class UserCreate(UserBase):
    language_id: Optional[str] = None

class User(UserBase):
    id: str
    language_id: Optional[str] = None
