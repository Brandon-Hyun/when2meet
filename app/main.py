from fastapi import FastAPI
from app.models.users import UserModel
from app.models.movies import MovieModel
from app.routers.users import user_router
from app.routers.movies import movie_router

import uvicorn

app = FastAPI()

UserModel.create_dummy()  # API 테스트를 위한 더미를 생성하는 메서드 입니다.
MovieModel.create_dummy()   # API 테스트를 위한 더미를 생성하는 메서드 입니다.

app.include_router(user_router)
app.include_router(movie_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# dict, set, list, tuple -> collection
# int, str, bool 같은 자료형의 자료를 담기위한 collection
