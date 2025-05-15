from abc import ABC, abstractmethod

from app.domain.models.follow import Follow


class FollowRepository(ABC):
    @abstractmethod
    def create(self, follow: Follow) -> Follow:
        pass

    @abstractmethod
    def get_followee_ids(self, follower_id: str) -> list[str]:
        pass
