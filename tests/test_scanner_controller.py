import pytest
from unittest.mock import AsyncMock, patch
from fastapi import UploadFile
from app.controllers.scanner_controller import ScannerController

@pytest.fixture
def mock_file():
    return UploadFile(filename="test.txt", file=AsyncMock(read=AsyncMock(return_value=b"test file content")))

@patch("app.controllers.scanner_controller.scanner.scan")
@pytest.mark.asyncio
async def test_scan_file_success(mock_scan, mock_file):
    mock_scan.return_value = {"scan_id": "12345", "status": "completed"}

    result = await ScannerController.scan_file(mock_file)

    assert result["scan_id"] == "12345"
    assert result["status"] == "completed"

@patch("app.controllers.scanner_controller.scanner.scan")
@pytest.mark.asyncio
async def test_scan_file_failure(mock_scan, mock_file):
    mock_scan.side_effect = Exception("Scan failed")

    with pytest.raises(Exception) as excinfo:
        await ScannerController.scan_file(mock_file)
    assert "Scan failed" in str(excinfo.value)