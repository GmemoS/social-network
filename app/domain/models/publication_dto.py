from pydantic import BaseModel, Field


class PublicationDTO(BaseModel):
    user_id: str = Field(min_length=1)
    content: str = Field(min_length=1)
