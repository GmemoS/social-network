from datetime import UTC as timezoneUTC
from datetime import datetime

from app.domain.models.publication import Publication
from app.domain.models.timeline import Timeline
from app.domain.repositories.follow import FollowRepository
from app.domain.repositories.publication import PublicationRepository
from app.domain.repositories.timeline import TimelineRepository


class TimelineUseCase:

    def __init__(
        self,
        repository: TimelineRepository,
        follow_repo: FollowRepository,
        publication_repo: PublicationRepository,
    ) -> None:
        self.repository = repository
        self.follow_repo = follow_repo
        self.publication_repo = publication_repo

    def get_user_timeline(self, user_id: str) -> list[Publication]:
        """Gets the user's timeline.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list[Publication]: A list of publications.
        """
        timeline = []

        publications_ids = [
            timeline.publication_id
            for timeline in self.repository.get_by_user_id(user_id)
        ]

        for pub_id in publications_ids:
            timeline.append(self.publication_repo.get_by_id(pub_id))

        return timeline

    def add_to_user_timeline(
        self, user_id: str, publication_id: str
    ) -> Timeline:
        """Adds a publication to the user's timeline.

        Args:
            user_id (str): The ID of the user.
            publication_id (str): The ID of the publication.

        Returns:
            Timeline: The added timeline.
        """
        return self.repository.add_to_user_timeline(
            Timeline(
                user_id=user_id,
                publication_id=publication_id,
                timestamp=datetime.now(timezoneUTC).timestamp(),
            )
        )

    def update_followers_timelines(
        self, user_id: str, publication_id: str
    ) -> None:
        """Updates the followers' timelines with the given publication.

        Args:
            user_id (str): The ID of the user.
            publication_id (str): The ID of the publication.
        """
        followers_ids = self.follow_repo.get_followers_ids(user_id)

        for follower_id in followers_ids:
            self.add_to_user_timeline(follower_id, publication_id)
