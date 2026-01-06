from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.dependencies import get_current_user
from app.models.users import UserModel
from app.schemas.users import UserCreate, UserUpdate

user_router = APIRouter(prefix="/users", tags=["users"])


# 유저 생성
@user_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate):
    new_user = UserModel.create(username=user_in.username, age=user_in.age, gender=user_in.gender)
    return {"id": new_user.id}


# 전체 유저 목록 조회 API (endpoint)
@user_router.get("/")
async def get_all_users():
    user = UserModel.all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


# 특정 유저 상세 조회 API (endpoint)
@user_router.get("/{user_id}")
async def get_user(user=Depends(get_current_user)):
    return user


# 유저 삭제 API (endpoint)
@user_router.delete("/{user_id}")
async def delete_user(user=Depends(get_current_user)):
    user.delete()  # 유저 인스턴스의 delete() 메서드 호출
    return {"message": f"User : {user.id} ({user.username})  deleted successfully"}


# 유저 업데이트 API (endpoint)
@user_router.patch("/{user_id}")  # put : 전체 교체, patch 일부만 수정할때
async def update_user(user_in: UserUpdate, user=Depends(get_current_user)):
    update_data = user_in.model_dump(exclude_unset=True)
    user.update(**update_data)  # 모델에 정의된 update메서드 실행
    # user.update(**user_update.dict(exclude_unset=True))    # pydantic v1 기준, 결과는 같음.  # exclude_unset=True 입력하지 않은 값은 제외

    return {"message": f"User : {user.id} ({user.username})  updated successfully"}
