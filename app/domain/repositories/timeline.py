from abc import ABC, abstractmethod

from app.domain.models.timeline import Timeline


class TimelineRepository(ABC):
    @abstractmethod
    def add_to_user_timeline(self, timeline: Timeline) -> Timeline:
        pass

    @abstractmethod
    def get_by_user_id(
        self, user_id: str, limit: int = 100
    ) -> list[Timeline]:
        pass
