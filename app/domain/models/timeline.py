from datetime import datetime

from pydantic import BaseModel


class Timeline(BaseModel):
    user_id: str
    publication_id: str
    timestamp: datetime
