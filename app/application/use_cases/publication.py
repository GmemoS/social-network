from app.domain.models.publication import Publication
from app.domain.repositories.publication import PublicationRepository

PUBLICATION_DEFAULT_MAX_LENGTH = 280


class PublicationUseCase:
    def __init__(self, publication_repo: PublicationRepository):
        self.repository = publication_repo

    def create_publication(
        self, user_id: str, content: str
    ) -> Publication:
        if len(content) > PUBLICATION_DEFAULT_MAX_LENGTH:
            raise ValueError(
                "Publication content cannot be longer than "
                f"{PUBLICATION_DEFAULT_MAX_LENGTH} characters"
            )

        publication = Publication(user_id=user_id, content=content)

        return self.repository.create(publication)

    def get_publications_by_user_id(
        self, user_id: str
    ) -> list[Publication]:
        return self.repository.get_by_user_id(user_id)
