from app.domain.models.publication import Publication
from app.domain.repositories.follow import FollowRepository
from app.domain.repositories.publication import PublicationRepository


class TimelineUseCase:
    def __init__(
        self,
        follow_repo: FollowRepository,
        publication_repo: PublicationRepository,
    ):
        self.follow_repo = follow_repo
        self.publication_repo = publication_repo

    def get_user_timeline(self, user_id: str) -> list[Publication]:
        followee_ids = self.follow_repo.get_followee_ids(user_id)

        return self.publication_repo.get_by_user_ids(followee_ids)
