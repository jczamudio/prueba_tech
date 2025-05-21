import requests
import os
from app.interfaces.scanner_interface import FileScanner

class VirusTotalScanner(FileScanner):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://www.virustotal.com/vtapi/v2/file/scan"

    def scan(self, file_bytes: bytes, filename: str) -> dict:
        files = {"file": (filename, file_bytes)}
        params = {"apikey": self.api_key}
        response = requests.post(self.api_url, files=files, params=params)
        if response.status_code != 200:
            raise Exception(f"VirusTotal error: {response.status_code}, {response.text}")
        return response.json()
