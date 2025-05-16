from datetime import UTC as timezoneUTC
from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class Publication(BaseModel):
    id: str | None = Field(default=None)
    user_id: str
    content: str
    created_at: datetime | None = Field(
        default_factory=lambda: datetime.now(timezoneUTC)
    )

    @field_validator("content")
    def content_not_empty(cls, v: str) -> str:
        if not v:
            raise ValueError("Publication content cannot be empty")
        return v
