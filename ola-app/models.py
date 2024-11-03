from pydantic import BaseModel, Field
from typing import List, Optional

class Language(BaseModel):
    id: str
    name: str
    hola: str

class User(BaseModel):
    id: str
    username: str
    password: str
    language_id: Optional[str] = None  # Foreign key-like reference
