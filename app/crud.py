# app/crud.py
from sqlmodel import Session, select
from typing import Optional, List

from .models import Picture, User
from .schemas import PictureCreate


def add_picture(db: Session, new_picture: PictureCreate) -> Picture:
    """
    Insert a new Picture row into the DB using the data from PictureCreate.
    """
    new_pic = Picture(
            image_url=new_picture.image_url,
            user_id=new_picture.user_id,
            description=new_picture.description,
        )
    db.add(new_pic)
    db.commit()
    db.refresh(new_pic)
    return new_pic


def get_picture(db: Session, picture_id: int) -> Optional[Picture]:
    """
    Fetch a Picture by its primary key.
    Returns None if not found.
    """
    return db.get(Picture, picture_id)

def list_pictures_by_user(db: Session, user_id: int) -> List[Picture]:
    """
    Return all Picture rows for a given user_id.
    """
    statement = select(Picture).where(Picture.user_id == user_id)
    results = db.exec(statement).all()
    return results
