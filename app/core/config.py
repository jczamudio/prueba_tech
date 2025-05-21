import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    VT_API_KEY: str = os.getenv("VT_API_KEY")

settings = Settings()
