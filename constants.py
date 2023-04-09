import os
import logging

# LOGGER
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

# Base URLs
COINGECKO_BASE_URL = os.environ.get("COINGECKO_BASE_URL")
POLYGOIN_IO_BASE_URL = os.environ.get("POLYGON_IO_BASE_URL")
COINMARKETCAP_BASE_URL = os.environ.get("COINMARKETCAP_BASE_URL")

#API Keys
COINMARKETCAP_API_KEY = os.environ.get("COINMARKETCAP_API_KEY")
POLYGON_IO_AUTH_KEY = os.environ.get("POLYGON_IO_AUTHORIZATION_KEY")