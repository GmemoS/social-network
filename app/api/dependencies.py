from fastapi import FastAPI, Request

from app.application.use_cases.follow import FollowUseCase
from app.application.use_cases.publication import PublicationUseCase
from app.application.use_cases.timeline import TimelineUseCase
from app.infrastructure.in_memory_db.follow import (
    InMemoryFollowRepository,
)
from app.infrastructure.in_memory_db.publication import (
    InMemoryPublicationRepository,
)
from app.infrastructure.in_memory_db.timeline import (
    InMemoryTimelineRepository,
)


def get_publication_repository(
    request: Request,
) -> InMemoryPublicationRepository:
    return request.app.state.publication_repository


def get_follow_repository(request: Request) -> InMemoryFollowRepository:
    return request.app.state.follow_repository


def get_publication_use_case(
    request: Request,
) -> PublicationUseCase:
    return request.app.state.publication_use_case


def get_follow_use_case(request: Request) -> FollowUseCase:
    return request.app.state.follow_use_case


def get_timeline_use_case(request: Request) -> TimelineUseCase:
    return request.app.state.timeline_use_case


def setup_dependencies(app: FastAPI) -> None:
    # Repositories
    publication_repository = InMemoryPublicationRepository()
    follow_repository = InMemoryFollowRepository()
    timeline_repository = InMemoryTimelineRepository()

    app.state.publication_repository = publication_repository
    app.state.follow_repository = follow_repository

    # Use cases
    app.state.publication_use_case = PublicationUseCase(
        publication_repository,
        follow_repository,
        timeline_repository,
    )
    app.state.follow_use_case = FollowUseCase(follow_repository)
    app.state.timeline_use_case = TimelineUseCase(
        timeline_repository, follow_repository, publication_repository
    )
