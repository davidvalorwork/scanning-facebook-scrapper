import uuid
from typing import Optional, Dict, List
from pydantic import BaseModel, Field
import copy

class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    Friend_count: str = Field(...)
    Follower_count: str = Field(...)
    Following_count: str = Field(...)
    cover_photo_text: str = Field(...)
    cover_photo: str = Field(...)
    profile_picture: str = Field(...)
    facebook_id: str = Field(...)
    Name: str = Field(...)
    Work: str = Field(...)
    Education: str = Field(...)
    Places_lived: str = Field(...)
    Contact_info: str = Field(...) 
    Basic_info: str = Field(...) 
    Other_names: str = Field(...) 
    Relationship: str = Field(...)
    Family_members: str = Field(...) 
    About: str = Field(...)
    Life_events: str = Field(...)
    Favorite_quotes: str = Field(...)
    Friends: List[Dict] = Field(...)

    def serialization(user):
        new_user = copy.copy(user)

        new_user['facebook_id'] = user['id']
        if('Places lived' in user): new_user['Places_lived'] = user['Places lived']
        if('Contact info\nEdit' in user): new_user['Contact_info'] = user['Contact info\nEdit']
        if('Basic info\nEdit' in user): new_user['Basic_info'] = user['Basic info\nEdit']
        if('Other names' in user): new_user['Other_names'] = user['Other names']
        if('Family members' in user): new_user['Family_members'] =user['Family members']
        if('Life events' in user): new_user['Life_events'] = user['Life events']
        if('Favorite quotes' in user): new_user['Favorite_quotes'] = user['Favorite quotes']

        del new_user['id']
        if('Places lived' in user): del new_user['Places lived']
        if('Contact info\nEdit' in user): del new_user['Contact info\nEdit']
        if('Basic info\nEdit' in user): del new_user['Basic info\nEdit']
        if('Other names' in user): del new_user['Other names']
        if('Family members' in user): del new_user['Family members']
        if('Life events' in user): del new_user['Life events']
        if('Favorite quotes' in user): del new_user['Favorite quotes']

        return new_user


    class Config:
        allow_population_by_field_name = True
