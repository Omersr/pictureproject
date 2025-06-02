# app/routers.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from .database import get_session
from .crud import *
from .schemas import PictureCreate
from .models import Picture

pictures_router = APIRouter(
    prefix="/pictures",
    tags=["pictures"],
)


@pictures_router.post(
    "/",
    response_model=Picture,
    status_code=status.HTTP_201_CREATED,
)
def create_picture_endpoint(
    payload: PictureCreate,
    session: Session = Depends(get_session),
):
    """
    POST /pictures/
    - Expects JSON { image_url: str, user_id: int, description?: str }
    - Returns the newly created Picture (including id + created_at).
    """
    # Example of extra HTTP‐layer validation:
    if not (payload.image_url.startswith("http://") or payload.image_url.startswith("https://")):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="image_url must start with http:// or https://"
        )

    new_pic = add_picture(session, payload)
    return new_pic


@pictures_router.get(
    "/{picture_id}",
    response_model=Picture,
)
def read_picture(picture_id: int, session: Session = Depends(get_session)):
    """
    GET /pictures/{picture_id}
    - Returns a single Picture by its primary key, or 404 if not found.
    """
    pic = get_picture(session, picture_id)
    if not pic:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Picture not found")
    return pic


@pictures_router.get(
    "/user/{user_id}",
    response_model=list[Picture],
)
def read_pictures_by_user(user_id: int, session: Session = Depends(get_session)):
    """
    GET /pictures/user/{user_id}
    - Returns all pictures belonging to that user.
    """
    return list_pictures_by_user(session, user_id)

@pictures_router.get("/test/ping")
def ping():
    return {"status": "ok"}

