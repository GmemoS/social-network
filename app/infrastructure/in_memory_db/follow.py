from collections import defaultdict

from app.domain.models.follow import Follow
from app.domain.repositories.follow import FollowRepository


class InMemoryFollowRepository(FollowRepository):
    def __init__(self):
        self.follows: dict[str, dict[str, Follow]] = defaultdict(dict)

    def create(self, follow: Follow) -> Follow:
        self.follows[follow.follower_id][follow.followee_id] = follow

        return follow

    def get_followee_ids(self, follower_id: str) -> list[str]:
        if follower_id not in self.follows:
            return []

        return list(self.follows[follower_id].keys())
