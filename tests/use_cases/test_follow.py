from unittest import TestCase
from unittest.mock import Mock

from app.application.use_cases.follow import FollowUseCase
from app.domain.models.follow import Follow


class TestFollowUseCase(TestCase):
    def setUp(self):
        self.mock_repository = Mock()
        self.use_case = FollowUseCase(self.mock_repository)

    def test_follow_user(self):
        follower_id = "user1"
        followee_id = "user2"
        follow_instance = Follow(
            follower_id=follower_id, followee_id=followee_id
        )

        self.mock_repository.create.return_value = follow_instance

        follow_result = self.use_case.follow_user(
            follower_id, followee_id
        )

        self.mock_repository.create.assert_called_once_with(
            follow_instance
        )

        self.assertEqual(follow_result, follow_instance)

    def test_get_followee_ids(self):
        follower_id = "user1"
        followee_ids = ["user2", "user3"]

        self.mock_repository.get_followee_ids.return_value = (
            followee_ids
        )

        result = self.use_case.get_followee_ids(follower_id)

        self.mock_repository.get_followee_ids.assert_called_once_with(
            follower_id
        )

        self.assertEqual(result, followee_ids)
