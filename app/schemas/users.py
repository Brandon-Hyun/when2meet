from enum import Enum

from pydantic import BaseModel


# 성별은 male | female // Enumrate 둘 중 하나여야 한다고 정의함.
class Gender(str, Enum):
    male = "male"
    female = "female"


# 유저 생성시 pydantic 검증
class UserCreate(BaseModel):
    username: str
    age: int
    gender: Gender  # 클래스 Gender  enum규칙에 따름.. 상속이 파이썬의 꽃이라는게 이런건가;


class UserUpdate(BaseModel):
    username: str | None = None
    age: int | None = None
    gender: Gender | None = None
