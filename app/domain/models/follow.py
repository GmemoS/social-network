from pydantic import BaseModel, ValidationInfo, field_validator


class Follow(BaseModel):
    follower_id: str
    followee_id: str

    @field_validator("followee_id")
    def followee_id_not_self(cls, v: str, info: ValidationInfo):
        if v == info.data["follower_id"]:
            raise ValueError("Users cannot follow themselves")
        return v
