from fastapi.encoders import jsonable_encoder
# from starlette.requests import Request
# from starlette.responses import JSONResponse
# from fastapi.exceptions import RequestValidationError
# import uvicorn
from routers import user,video
from fastapi.middleware.cors import CORSMiddleware
# from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_422_UNPROCESSABLE_ENTITY   
from fastapi import FastAPI
app = FastAPI()

# 加路由
app.include_router(user.router)
app.include_router(video.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World!"}