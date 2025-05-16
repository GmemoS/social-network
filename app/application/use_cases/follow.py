from app.domain.models.follow import Follow
from app.domain.repositories.follow import FollowRepository


class FollowUseCase:

    def __init__(self, follow_repo: FollowRepository) -> None:
        self.repository = follow_repo

    def follow_user(self, follower_id: str, followee_id: str) -> Follow:
        """Creates a follow relationship between two users.

        Args:
            follower_id (str): The ID of the user who is following.
            followee_id (str): The ID of the user being followed.

        Returns:
            Follow: The created follow relationship.
        """
        follow = Follow(
            follower_id=follower_id,
            followee_id=followee_id,
        )

        return self.repository.create(follow)

    def get_followers_ids(self, user_id: str) -> list[str]:
        """Gets the IDs of the users that are following the given user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list[str]: A list of user IDs.
        """
        return self.repository.get_followers_ids(user_id)
