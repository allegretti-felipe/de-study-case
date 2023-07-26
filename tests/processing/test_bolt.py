from unittest.mock import MagicMock, patch

import pytest

from processing._base import BaseProcessing
from processing.bolt import Bolt


@pytest.fixture
def mock_base_processing():
    with patch.object(BaseProcessing, "__init__", return_value=None):
        yield


@pytest.fixture
def mock_bolt(mock_base_processing):
    with patch.object(Bolt, "__post_init__"):
        yield Bolt(company="Bolt", full_load=False, debug=False)


def test_run(mock_bolt):
    mock_bolt.s3 = MagicMock()
    mock_bolt.s3.list_files_from_path = MagicMock(return_value=["test1.json"])
    mock_bolt.s3.read_json = MagicMock(
        return_value={"content": "<div><p>Test content</p></div>", "url": "http://test.url"},
    )
    mock_bolt.extract_text_by_xpath = MagicMock(return_value="Test content")
    mock_bolt.extract_next_data = MagicMock(return_value="Test next data")

    mock_collection = MagicMock()
    mock_bolt.collection = mock_collection

    mock_bolt.run()
    assert mock_collection.replace_one.called
