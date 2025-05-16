from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock, patch

from app.application.use_cases.timeline import TimelineUseCase
from app.domain.models.publication import Publication
from app.domain.models.timeline import Timeline


class TestTimelineUseCase(TestCase):
    def setUp(self):
        self.mock_timeline_repo = Mock()
        self.mock_follow_repo = Mock()
        self.mock_publication_repo = Mock()
        self.use_case = TimelineUseCase(
            self.mock_timeline_repo,
            self.mock_follow_repo,
            self.mock_publication_repo,
        )

    def test_get_user_timeline(self):
        user_id = "user-456"
        publication_ids = ["pub-1", "pub-2"]
        publications = [
            Publication(id=pub_id, user_id="user", content="Content")
            for pub_id in publication_ids
        ]

        self.mock_timeline_repo.get_by_user_id.return_value = [
            Timeline(
                user_id=user_id,
                publication_id=pub_id,
                timestamp=datetime.now().timestamp(),
            )
            for pub_id in publication_ids
        ]
        self.mock_publication_repo.get_by_id.side_effect = (
            lambda pub_id: next(
                pub for pub in publications if pub.id == pub_id
            )
        )

        result = self.use_case.get_user_timeline(user_id)

        self.mock_timeline_repo.get_by_user_id.assert_called_once_with(
            user_id
        )
        self.assertEqual(result, publications)

    @patch('app.application.use_cases.timeline.datetime')
    def test_add_to_user_timeline(self, mock_datetime):
        mock_datetime.now.return_value = datetime.now()
        user_id = "user-123"
        publication_id = "pub-456"

        timeline_entry = Timeline(
            user_id=user_id,
            publication_id=publication_id,
            timestamp=mock_datetime.now().timestamp(),
        )
        self.mock_timeline_repo.add_to_user_timeline.return_value = (
            timeline_entry
        )

        result = self.use_case.add_to_user_timeline(
            user_id, publication_id
        )

        self.mock_timeline_repo.add_to_user_timeline.assert_called_once_with(
            timeline_entry
        )
        self.assertEqual(result, timeline_entry)

    def test_update_followers_timelines(self):
        user_id = "user-123"
        publication_id = "pub-456"
        followers_ids = ["follower-1", "follower-2"]

        self.mock_follow_repo.get_followers_ids.return_value = (
            followers_ids
        )
        self.use_case.add_to_user_timeline = Mock()

        self.use_case.update_followers_timelines(
            user_id, publication_id
        )

        self.mock_follow_repo.get_followers_ids.assert_called_once_with(
            user_id
        )

        for follower_id in followers_ids:
            self.use_case.add_to_user_timeline.assert_any_call(
                follower_id, publication_id
            )
