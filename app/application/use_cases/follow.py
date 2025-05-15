from app.domain.models.follow import Follow
from app.domain.repositories.follow import FollowRepository


class FollowUseCase:
    def __init__(self, follow_repo: FollowRepository):
        self.repository = follow_repo

    def follow_user(self, follower_id: str, followee_id: str) -> Follow:
        follow = Follow(
            follower_id=follower_id,
            followee_id=followee_id,
        )

        return self.repository.create(follow)

    def get_followee_ids(self, follower_id: str) -> list[str]:
        return self.repository.get_followee_ids(follower_id)
