import pathlib
import os
from dotenv import load_dotenv


load_dotenv()
# Make sure to create .env file for the discord token 
#     - create a .env variable and name it DISCORD_API_TOKEN
DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")

BASE_DIR = pathlib.Path(__file__).parent





