from collections import defaultdict

from app.domain.models.follow import Follow
from app.domain.repositories.follow import FollowRepository


class InMemoryFollowRepository(FollowRepository):

    def __init__(self) -> None:
        self.follows: dict[str, dict[str, Follow]] = defaultdict(dict)

    def create(self, follow: Follow) -> Follow:
        """Creates a follow relationship between two users.

        Args:
            follow (Follow): The follow relationship to create.

        Returns:
            Follow: The created follow relationship.
        """
        self.follows[follow.followee_id][follow.follower_id] = follow

        return follow

    def get_followers_ids(self, user_id: str) -> list[str]:
        """Gets the IDs of the users that are following the given user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list[str]: A list of user IDs.
        """
        if user_id not in self.follows:
            return []

        return list(self.follows[user_id].keys())
