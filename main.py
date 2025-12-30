from typing import Annotated
from fastapi import FastAPI, HTTPException, Path, Depends
from app.models.users import UserModel
from app.models.movies import MovieModel
from app.schemas.users import UserCreate, UserUpdate
from app.schemas.movies import MovieCreate, MovieUpdate

app = FastAPI()

 # 유저 검증 공통함수
def get_current_user(user_id : int = Path(gt=0)):
    user = UserModel.get(id = user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

 # 영화 검증 공통 함수
def get_current_movie(movie_id : int = Path(gt=0)):
    movie = MovieModel.get(id = movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

# 유저 생성 API
@app.post("/users/")
def create_user(user_in: UserCreate):  # user_in = parameter, typehint 가 UserCreate 클래스임, UserCreate 양식에 맞는지 검증(data validation),JSON(텍스트잖아?)을 객체로 변환 UserModel 로.== Deserialization 역직렬화
    new_user = UserModel.create(username=user_in.username, age=user_in.age, gender=user_in.gender)
    return {"id": new_user.id}

# 전체 유저 목록 조회 API (endpoint)
@app.get("/users/")
def get_all_users():
    users = UserModel.all()
    return users


# 특정 유저 상세 조회 API (endpoint)
@app.get("/users/{user_id}")
def get_user(user = Depends(get_current_user)):
    return user


# 유저 삭제 API (endpoint)
@app.delete("/users/{user_id}")
def delete_user(user = Depends(get_current_user)):
    user.delete()  # 유저 인스턴스의 delete() 메서드 호출
    return {"message": f"User : {user.id} ({user.username})  deleted successfully"}


# 유저 업데이트 API (endpoint)
@app.put("/users/{user_id}")  # put : 전체 교체, patch 일부만 수정할때
def update_user(user_in: UserUpdate, user = Depends(get_current_user)):
    update_data = user_in.model_dump(exclude_unset=True)
    user.update(**update_data)  # 모델에 정의된 update메서드 실행
# user.update(**user_update.dict(exclude_unset=True))    # pydantic v1 기준, 결과는 같음.  # exclude_unset=True 입력하지 않은 값은 제외

    return {"message": f"User : {user.id} ({user.username})  updated successfully"}



""""""
# 영화 생성 API
@app.post("/movies/")
def create_movie(movie_in: MovieCreate):
    new_movie = MovieModel.create(title = movie_in.title, playtime = movie_in.playtime, genre=movie_in.genre)
    return {"id": new_movie.id}

# 전체 영화 목록 조회 API (endpoint)
@app.get("/movies/")
def get_all_movies():
    movies = MovieModel.all()
    return movies


# 특정 영화 상세 조회 API (endpoint)
@app.get("/movies/{movie_id}")
def get_movie(movie = Depends(get_current_movie)):
    return movie


# 영화 삭제 API (endpoint)
@app.delete("/movies/{movie_id}")
def delete_movie(movie = Depends(get_current_movie)):
    movie.delete()  # 영화 인스턴스의 delete() 메서드 호출
    return {"message": f"Movie : {movie.id} ({movie.title})  deleted successfully"}


# 영화 업데이트 API (endpoint)
@app.put("/movies/{movie_id}")  # put : 전체 교체, patch 일부만 수정할때
def update_movie(movie_in: MovieUpdate, movie = Depends(get_current_movie)):
    update_data = movie_in.model_dump(exclude_unset=True)
    movie.update(**update_data)  # 모델에 정의된 update메서드 실행

    return {"message": f"Movie : {movie.id} ({movie.title})  updated successfully"}


UserModel.create_dummy()  # API 테스트를 위한 더미를 생성하는 메서드 입니다.
MovieModel.create_dummy()   # API 테스트를 위한 더미를 생성하는 메서드 입니다.


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

# dict, set, list, tuple -> collection
# int, str, bool 같은 자료형의 자료를 담기위한 collection
