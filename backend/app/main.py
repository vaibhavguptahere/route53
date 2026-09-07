from fastapi import FastAPI

app = FastAPI(title="Route53 Clone API")


@app.get("/")
def root():
    return {"message": "Route53 Clone API"}