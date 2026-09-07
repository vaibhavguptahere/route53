from fastapi import FastAPI

from .database import engine
from .models import Base
from .routers import hosted_zones, records

app = FastAPI(title="Route53 Clone API")

Base.metadata.create_all(bind=engine)

app.include_router(hosted_zones.router)
app.include_router(records.router)


@app.get("/")
def root():
    return {"message": "Route53 Clone API"}