from pydantic import Annotated, BaseModel

from app.dtos.frozen_config import FROZEN_CONFIG

class CreateMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG

    url_code: Annotated[str, Field(description="미팅 url 코드, Unique합니다.")]
