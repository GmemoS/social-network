from collections import defaultdict

from app.domain.models.timeline import Timeline
from app.domain.repositories.timeline import TimelineRepository


class InMemoryTimelineRepository(TimelineRepository):
    def __init__(self) -> None:
        self.timelines: dict[str, list[tuple[str, float]]] = (
            defaultdict(list)
        )

    def add_to_user_timeline(self, timeline: Timeline) -> Timeline:
        """Adds a timeline to a user's timeline.

        Args:
            timeline (Timeline): The timeline to add.

        Returns:
            Timeline: The added timeline.
        """
        self.timelines[timeline.user_id].append(
            (timeline.publication_id, timeline.timestamp)
        )
        return timeline

    def get_by_user_id(
        self, user_id: str, limit: int = 100
    ) -> list[Timeline]:
        """Gets the timelines of a user.

        Args:
            user_id (str): The ID of the user.
            limit (int, optional): The maximum number of timelines to
                return. Defaults to 100.

        Returns:
            list[Timeline]: A list of timelines.
        """
        result = []

        user_timelines = reversed(
            self.timelines.get(user_id, [])[:limit]
        )

        for pub_id, timestamp in user_timelines:
            result.append(
                Timeline(
                    user_id=user_id,
                    publication_id=pub_id,
                    timestamp=timestamp,
                )
            )

        return result
