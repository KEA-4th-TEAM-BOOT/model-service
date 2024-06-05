import os
import uvicorn
import config
from fastapi import FastAPI
from api import main
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

port = int(os.environ.get("MODEL_PORT", 8002))

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메소드 허용
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)

app.include_router(main.api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}