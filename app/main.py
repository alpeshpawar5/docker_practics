from fastapi import FastAPI

app = FastAPI(title="FastAPI, Docker")


@app.get("/")
def read_root():
    return {"hello": "world"}