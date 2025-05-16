from collections import defaultdict
from uuid import uuid4

from app.domain.models.publication import Publication
from app.domain.repositories.publication import PublicationRepository


class InMemoryPublicationRepository(PublicationRepository):

    def __init__(self) -> None:
        self.publications: dict[str, Publication] = {}
        self.user_publications: dict[str, list[str]] = defaultdict(list)

    def create(self, publication: Publication) -> Publication:
        """Creates a new publication.

        Args:
            publication (Publication): The publication to create.

        Returns:
            Publication: The created publication.
        """
        publication.id = str(uuid4())

        self.publications[publication.id] = publication

        self.user_publications[publication.user_id].append(
            publication.id
        )

        return publication

    def get_by_id(self, publication_id: str) -> Publication:
        """Gets a publication by its ID.

        Args:
            publication_id (str): The ID of the publication.

        Returns:
            Publication: The publication.
        """
        return self.publications.get(publication_id)

    def get_by_user_id(
        self, user_id: str, limit: int = 100
    ) -> list[Publication]:
        """Gets the publications of a user.

        Args:
            user_id (str): The ID of the user.
            limit (int, optional): The maximum number of publications to
                return. Defaults to 100.

        Returns:
            list[Publication]: A list of publications.
        """
        result = [
            self.publications[pub_id]
            for pub_id in self.user_publications.get(user_id, [])
        ]

        return sorted(result, key=lambda t: t.timestamp, reverse=True)[
            :limit
        ]
