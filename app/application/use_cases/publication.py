from concurrent.futures import ThreadPoolExecutor

from app.application.use_cases.timeline import TimelineUseCase
from app.domain.models.publication import Publication
from app.domain.repositories.follow import FollowRepository
from app.domain.repositories.publication import PublicationRepository
from app.domain.repositories.timeline import TimelineRepository

PUBLICATION_DEFAULT_MAX_LENGTH = 280


class PublicationUseCase:

    def __init__(
        self,
        publication_repo: PublicationRepository,
        follow_repo: FollowRepository,
        timeline_repo: TimelineRepository,
    ) -> None:
        self.repository = publication_repo

        # NOTE: These objects are just injected for fake queue
        # implementation
        self.follow_repo = follow_repo
        self.timeline_repo = timeline_repo
        self.executor = ThreadPoolExecutor(max_workers=1)

    def create_publication(
        self, user_id: str, content: str
    ) -> Publication:
        """Creates a new publication.

        Args:
            user_id (str): The ID of the user who is creating the publication.
            content (str): The content of the publication.

        Returns:
            Publication: The created publication.

        Raises:
            ValueError: If the content is longer than the maximum length.
        """
        if len(content) > PUBLICATION_DEFAULT_MAX_LENGTH:
            raise ValueError(
                "Publication content cannot be longer than "
                f"{PUBLICATION_DEFAULT_MAX_LENGTH} characters"
            )

        publication = self.repository.create(
            Publication(user_id=user_id, content=content)
        )

        # Propagate the publication to the followers of the user
        self._propagate_to_followers(publication.id, user_id)

        return publication

    def get_publications_by_user_id(
        self, user_id: str
    ) -> list[Publication]:
        """Gets the publications of a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list[Publication]: A list of publications.
        """
        return self.repository.get_by_user_id(user_id)

    def _propagate_to_followers(
        self, publication_id: str, user_id: str
    ) -> None:
        """
        Propagate the publication to the followers of the user.

        NOTE: This method is just a fake queue implementation. In the
        real application, you would use a message queue.

        Args:
            publication_id (str): The ID of the publication.
            user_id (str): The ID of the user.
        """
        timeline_use_case = TimelineUseCase(
            self.timeline_repo, self.follow_repo, self.repository
        )

        self.executor.submit(
            timeline_use_case.update_followers_timelines,
            user_id,
            publication_id,
        )
