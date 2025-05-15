from fastapi import APIRouter, FastAPI

from app.api.routers.publication import publication_router
from app.api.routers.user import user_router


def setup_routers(app: FastAPI) -> None:
    main_router = APIRouter(prefix="/api/v1")

    main_router.include_router(publication_router)
    main_router.include_router(user_router)

    app.include_router(main_router)
