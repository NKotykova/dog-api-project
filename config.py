from dotenv import load_dotenv
import os

load_dotenv()  # зчитує .env

API_KEY = os.getenv("DOG_API_KEY")