from abc import ABC, abstractmethod

class FileScanner(ABC):
    @abstractmethod
    def scan(self, file_bytes: bytes, filename: str) -> dict:
        pass