from fastapi import APIRouter, Body, Depends, HTTPException
from pydantic import ValidationError

from app.api.dependencies import get_publication_use_case
from app.application.use_cases.publication import PublicationUseCase
from app.domain.models.publication import Publication
from app.domain.models.publication_dto import PublicationDTO

publication_router = APIRouter(
    prefix="/publication", tags=["Publication"]
)


@publication_router.post("", response_model=Publication)
async def create_publication(
    publication: PublicationDTO = Body(...),
    use_case: PublicationUseCase = Depends(get_publication_use_case),
) -> Publication:
    try:
        return use_case.create_publication(
            publication.user_id, publication.content
        )
    except ValidationError as e:
        raise e
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
