from typing import Union 
from datetime import datetime, date
from pydantic import BaseModel, Field


class BlogBase(BaseModel):
    title: str = Field(examples=["FastApi入門"])
    text: str = Field(description="MarkDown")
    

class BlogCreate(BlogBase):
    pass


class BlogCreateResponse(BlogCreate):
    id: int = Field(description="ID")
    created_at: date = Field(description="created_at")
    updated_at: date = Field(description="updated_at")
    
    class Config:
        from_attributes = True
    
    
class Blog(BlogBase):
    id: int = Field(description="ID")
    created_at: date = Field(description="created_at")
    updated_at: date = Field(description="updated_at")
    
    class Config:
        from_attributes = True