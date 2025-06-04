
from typing     import Optional
from sqlmodel    import SQLModel
     
class PictureCreate(SQLModel):
    image_url:   str
    user_id:     int
    description: Optional[str] = None

class UserCreate(SQLModel):
    user_name:   str

