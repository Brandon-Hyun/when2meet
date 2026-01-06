from fastapi import HTTPException, Path

from app.models.movies import MovieModel
from app.models.users import UserModel


# 유저 검증 공통함수
def get_current_user(user_id: int = Path(gt=0)):
    user = UserModel.get(id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# 영화 검증 공통 함수
def get_current_movie(movie_id: int = Path(gt=0)):
    movie = MovieModel.get(id=movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie
