from pydantic import ConfigDict

FROZEN_CONFIG = ConfigDict(frozen=True)
 # frozen => 얼어있다. 얼어있는 객체 -> 생성 이후 변경 불가 == immutable

# my_set = frozenset()
# my_set.add(1)
