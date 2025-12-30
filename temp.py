# my_int: int = "1"
my_int: int = 123  # Literal : 값, inference (Literal 기반으로 추론한다.)  // 근데 왜

# dict, set, list, tuple -> collection
# int, str, bool 같은 자료형의 자료를 담기위한 collection

my_list: list[str] = ["abc", "def"]
my_list2 = ["abc", "def"]  # mypy 가 추론할 수 있으면 넘어감

# immutable (생성 후 길이 변경할 수 없다.)
# my_tuple: tuple[str,str] = ("str", "str", "str")  #튜플의 길이 명시함,
# 길이를 모르는 경우는?
my_tuple: tuple[str, ...] = ("str", "str", "str")  # ...

# pipeline | 은 or 의미함       // bool 은 int의 서브클래스


from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
