from abc import ABC, abstractmethod

from app.domain.models.publication import Publication


class PublicationRepository(ABC):
    @abstractmethod
    def create(self, publication: Publication) -> Publication:
        pass

    @abstractmethod
    def get_by_id(self, publication_id: str) -> Publication:
        pass

    @abstractmethod
    def get_by_user_id(
        self, user_id: str, limit: int = 100
    ) -> list[Publication]:
        pass
