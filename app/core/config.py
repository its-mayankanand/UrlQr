import logging

# Configure logging for the entire project
logging.basicConfig(
    level=logging.INFO,  # Default logging level (use DEBUG for more details in dev)
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Save logs to file: app.log
        logging.StreamHandler(),  # Also show logs in console
    ],
)

# Create a reusable project-wide logger
logger = logging.getLogger("urlqr")


# For future configs (DB URL, env vars etc.)
PROJECT_NAME = "QR Generator"
VERSION = "1.0.0"
