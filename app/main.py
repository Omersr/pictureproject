from fastapi import *
from .database import *
from .models import *
from .schemas import *
from .crud import *
from .routers import *
app = FastAPI(on_startup=[create_tables])

app.include_router(pictures_router)
