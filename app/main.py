from fastapi import FastAPI
from db.config import engine
from api.routes import routers
import db.models as models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(routers)

@app.get('/')
async def Home():
    return 'Welcome'