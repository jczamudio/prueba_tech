import pytest
from unittest.mock import patch, Mock
from app.services.virus_scanner import VirusTotalScanner


@pytest.fixture
def scanner():
    return VirusTotalScanner(api_key="test_api_key")

@patch("app.services.virus_scanner.requests.post")
def test_scan_success(mock_post, scanner):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"scan_id": "12345", "status": "completed"}
    mock_post.return_value = mock_response

    file_bytes = b"test file content"
    filename = "test.txt"
    result = scanner.scan(file_bytes, filename)

    assert result["scan_id"] == "12345"
    assert result["status"] == "completed"

@patch("app.services.virus_scanner.requests.post")
def test_scan_failure(mock_post, scanner):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"
    mock_post.return_value = mock_response

    file_bytes = b"test file content"
    filename = "test.txt"

    with pytest.raises(Exception) as excinfo:
        scanner.scan(file_bytes, filename)
    assert "VirusTotal error" in str(excinfo.value)