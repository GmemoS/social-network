from collections import defaultdict
from uuid import uuid4

from app.domain.models.publication import Publication
from app.domain.repositories.publication import PublicationRepository


class InMemoryPublicationRepository(PublicationRepository):
    def __init__(self):
        self.publications: dict[str, Publication] = {}
        self.user_publications: dict[str, list[str]] = defaultdict(list)

    def create(self, publication: Publication) -> Publication:
        publication.id = str(uuid4())

        self.publications[publication.id] = publication

        self.user_publications[publication.user_id].append(
            publication.id
        )

        return publication

    def get_by_user_id(self, user_id: str) -> list[Publication]:
        return [
            self.publications[pub_id]
            for pub_id in self.user_publications.get(user_id, [])
        ]

    def get_by_user_ids(
        self, user_ids: list[str], limit: int = 100
    ) -> list[Publication]:
        result = []

        for user_id in user_ids:
            result.extend(self.get_by_user_id(user_id))

        return sorted(result, key=lambda t: t.timestamp, reverse=True)[
            :limit
        ]
