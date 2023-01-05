from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__=="__main__":
    os.system("uvicorn main:app --reload")