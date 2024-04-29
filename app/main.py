from fastapi import FastAPI
from . import models
from .database import engine
from .router import user,auth,post

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(post.router)


@app.get("/")
def test_route():
    return {"status":"Success","message":"Server running"}