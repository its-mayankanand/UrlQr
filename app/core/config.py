import logging
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Read values from environment (must exist in .env or system env)
LOG_LEVEL = os.environ["LOG_LEVEL"]
LOG_FILE = os.environ["LOG_FILE"]
LOGGER_NAME = os.environ["LOGGER_NAME"]

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(),
    ],
)

# Create a reusable project-wide logger
logger = logging.getLogger(LOGGER_NAME)
