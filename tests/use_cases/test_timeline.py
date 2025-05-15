from unittest import TestCase
from unittest.mock import Mock

from app.application.use_cases.timeline import TimelineUseCase
from app.domain.models.publication import Publication


class TestTimelineUseCase(TestCase):
    def setUp(self):
        self.mock_follow_repo = Mock()
        self.mock_publication_repo = Mock()
        self.use_case = TimelineUseCase(
            self.mock_follow_repo, self.mock_publication_repo
        )

    def test_get_user_timeline(self):
        user_id = "user-456"
        followee_ids = ["followee-1", "followee-2"]

        publications = [
            Publication(
                user_id="followee-1", content="Content from followee 1"
            ),
            Publication(
                user_id="followee-2", content="Content from followee 2"
            ),
        ]

        self.mock_follow_repo.get_followee_ids.return_value = (
            followee_ids
        )
        self.mock_publication_repo.get_by_user_ids.return_value = (
            publications
        )

        result = self.use_case.get_user_timeline(user_id)

        self.mock_follow_repo.get_followee_ids.assert_called_once_with(
            user_id
        )
        self.mock_publication_repo.get_by_user_ids.assert_called_once_with(
            followee_ids
        )
        self.assertEqual(result, publications)
