from abc import ABC, abstractmethod

from app.domain.models.publication import Publication


class PublicationRepository(ABC):
    @abstractmethod
    def create(self, publication: Publication) -> Publication:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: str) -> list[Publication]:
        pass

    @abstractmethod
    def get_by_user_ids(
        self, user_ids: list[str], limit: int = 100
    ) -> list[Publication]:
        pass
