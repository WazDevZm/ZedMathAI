from dotenv import load_dotenv
from os import getenv

load_dotenv()

class ENVs:
    API_KEY = getenv("API_KEY")


settings = ENVs()