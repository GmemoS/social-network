from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock, patch

from app.application.use_cases.publication import (
    PUBLICATION_DEFAULT_MAX_LENGTH,
    PublicationUseCase,
)
from app.domain.models.publication import Publication


class TestPublicationUseCase(TestCase):
    def setUp(self):
        self.mock_repo = Mock()
        self.use_case = PublicationUseCase(self.mock_repo)

    @patch("app.domain.models.publication.datetime")
    def test_create_publication_success(self, mock_datetime):
        user_id = "user-123"
        content = "This is a valid publication content"

        with patch.object(
            mock_datetime, "now", return_value=datetime.now()
        ):
            publication = Publication(user_id=user_id, content=content)
            self.mock_repo.create.return_value = publication

            result = self.use_case.create_publication(user_id, content)

        self.mock_repo.create.assert_called_once_with(publication)
        self.assertEqual(result, publication)

    def test_create_publication_exceeds_max_length(self):
        user_id = "user-123"
        content = "x" * (PUBLICATION_DEFAULT_MAX_LENGTH + 1)

        with self.assertRaises(ValueError) as context:
            self.use_case.create_publication(user_id, content)

        self.assertIn(
            "Publication content cannot be longer than "
            f"{PUBLICATION_DEFAULT_MAX_LENGTH} characters",
            str(context.exception),
        )

    def test_get_publications_by_user_id(self):
        user_id = "user-123"
        publications = [
            Publication(user_id=user_id, content="Content 1"),
            Publication(user_id=user_id, content="Content 2"),
        ]

        self.mock_repo.get_by_user_id.return_value = publications

        result = self.use_case.get_publications_by_user_id(user_id)

        self.mock_repo.get_by_user_id.assert_called_once_with(user_id)
        self.assertEqual(result, publications)
