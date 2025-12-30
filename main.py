from typing import Annotated
from fastapi import FastAPI, HTTPException, Path
from app.models.users import UserModel
from app.schemas.users import UserCreate
from app.schemas.users import UserUpdate


app = FastAPI()


@app.post("/users/")
def create_user(
    user_in: UserCreate,
):  # user_in = parameter, typehint 가 UserCreate 클래스임, UserCreate 양식에 맞는지 검증(data validation),JSON(텍스트잖아?)을 객체로 변환 UserModel 로.== Deserialization 역직렬화
    new_user = UserModel.create(username=user_in.username, age=user_in.age, gender=user_in.gender)
    return {"id": new_user.id}


# 전체 유저 목록 조회 API (endpoint)
@app.get("/users/")
def get_all_users():
    users = UserModel.all()
    return users


# 특정 유저 상세 조회 API (endpoint)
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = UserModel.get(id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# 유저 삭제 API (endpoint)
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    user = UserModel.get(id=user_id)  # 삭제할 유저가 있나 유저 객체(instance) 가져와

    if user is None:  # 유저가 없으면 처리
        return {"error": "User not found"}

    user.delete()  # 유저 인스턴스의 delete() 메서드 호출
    return {"message": f"User : {user_id} ({user.username})  deleted successfully"}


# 유저 업데이트 API (endpoint)
@app.put("/users/{user_id}")  # put : 전체 교체, patch 일부만 수정할때
def update_user(data: UserUpdate, user_id: int = Path(gt=0)):

    user = UserModel.get(id=user_id)

    if not user:
        return {"error": "user not found"}

    update_data = user_in.model_dump(exclude_unset=True)
    user.update(**update_data)  # 모델에 정의된 update메서드 실행
    # user.update(**user_update.dict(exclude_unset=True))    # pydantic v1 기준, 결과는 같음.  # exclude_unset=True 입력하지 않은 값은 제외

    return {"message": f"User : {user_id} ({user.username})  updated successfully"}


UserModel.create_dummy()  # API 테스트를 위한 더미를 생성하는 메서드 입니다.


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

# dict, set, list, tuple -> collection
# int, str, bool 같은 자료형의 자료를 담기위한 collection
