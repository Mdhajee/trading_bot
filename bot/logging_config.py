import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

LOG_FILE = "logs/trading.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)