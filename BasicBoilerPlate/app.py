from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def root():
    return {"message": "Hello World"}

@app.patch("/")
async def root():
    return {"message": "Hello World"}

@app.delete("/")
async def root():
    return {"message": "Hello World"}
