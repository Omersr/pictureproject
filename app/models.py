
from typing     import Optional
from datetime   import datetime, timezone
from sqlmodel    import SQLModel, Field 
class User(SQLModel, table=True):
    id:       Optional[int] = Field(default=None, primary_key=True)
    username: str



class Picture(SQLModel, table=True):
    id:          Optional[int] = Field(default=None, primary_key=True)
    image_url:   str            = Field(nullable=False)
    user_id:     int            = Field(foreign_key="user.id", nullable=False)
    description: Optional[str]  = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc)) # default_factory means use this function to fill in a default.
    
class PictureCreate(SQLModel):
    image_url:   str
    user_id:     int
    description: Optional[str] = None

