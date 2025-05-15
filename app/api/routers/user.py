from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies import (
    get_follow_use_case,
    get_publication_use_case,
    get_timeline_use_case,
)
from app.application.use_cases.follow import FollowUseCase
from app.application.use_cases.publication import PublicationUseCase
from app.application.use_cases.timeline import TimelineUseCase
from app.domain.models.publication import Publication

user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.get(
    "/{user_id}/publications", response_model=list[Publication]
)
async def get_user_publications(
    user_id: str,
    use_case: PublicationUseCase = Depends(get_publication_use_case),
) -> list[Publication]:
    return use_case.get_publications_by_user_id(user_id)


@user_router.post("/{user_id}/follow/{followee_id}")
async def follow_user(
    user_id: str,
    followee_id: str,
    use_case: FollowUseCase = Depends(get_follow_use_case),
) -> str:
    use_case.follow_user(user_id, followee_id)
    return "success"


@user_router.get("/{user_id}/timeline")
async def get_user_timeline(
    user_id: str,
    use_case: TimelineUseCase = Depends(get_timeline_use_case),
) -> list[Publication]:
    return use_case.get_user_timeline(user_id)
