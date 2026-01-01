from typing import Annotated

from fastapi import Path, HTTPException, Query, APIRouter,Depends
from starlette import status

from app.models.movies import MovieModel
from app.schemas.movies import MovieResponse, MovieCreate, MovieSearchParams, MovieUpdate
from app.dependencies import get_current_movie


movie_router = APIRouter(prefix="/movies", tags=["movies"])

# 영화 생성 API
@movie_router.post("/", response_model=MovieResponse, status_code=status.HTTP_201_CREATED)
async def create_movie(movie_in: MovieCreate):
    movie = MovieModel.create(**movie_in.dump())
    return {"id": movie.id}

# 전체 영화 목록 조회 API (endpoint)
@movie_router.get("/", response_model=list[MovieResponse], status_code=status.HTTP_200_OK)
async def get_all_movies(query_params: Annotated[MovieSearchParams, Query()]):
    valid_query = {key: value for key, value in query_params.model_dump().items() if value is not None}

    if valid_query:
        return MovieModel.filter(**valid_query)
    return MovieModel.all()

# 특정 영화 상세 조회 API (endpoint)
@movie_router.get("/{movie_id}")
async def get_movie(movie = Depends(get_current_movie)):
    return movie

# 영화 삭제 API (endpoint)
@movie_router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(movie = Depends(get_current_movie)):
    movie.delete()  # 영화 인스턴스의 delete() 메서드 호출
    return {"message": f"Movie : {movie.id} ({movie.title})  deleted successfully"}

# 영화 업데이트 API (endpoint)
@movie_router.put("/{movie_id}", response_model=MovieResponse, status_code=200)  # put : 전체 교체, patch 일부만 수정할때
async def update_movie(movie_in: MovieUpdate, movie = Depends(get_current_movie)):
    update_data = movie_in.model_dump(exclude_unset=True)
    movie.update(**update_data)  # 모델에 정의된 update메서드 실행

    return {"message": f"Movie : {movie.id} ({movie.title})  updated successfully"}