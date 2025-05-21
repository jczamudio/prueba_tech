import logging

from fastapi import UploadFile
from app.services.virus_scanner import VirusTotalScanner
from app.core.config import settings

scanner = VirusTotalScanner(settings.VT_API_KEY)

class ScannerController:
    @staticmethod
    async def scan_file(file: UploadFile) -> dict:
        contents = await file.read()
        result = scanner.scan(contents, file.filename)
        return result
