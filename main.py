import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

port = int(os.environ.get("VOICE_PORT", 8002))

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}