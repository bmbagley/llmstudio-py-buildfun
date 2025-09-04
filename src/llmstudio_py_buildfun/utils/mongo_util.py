"""Setup of mongodb initialization, import, and storage."""

import json
import logging
from pathlib import Path

from pymongo import MongoClient

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

package_root_pth = Path(__file__).parent.parent
logging.debug(f"Package Root: {package_root_pth}")

if package_root_pth.joinpath('config').is_dir():
    with open(package_root_pth.joinpath('config', 'settings.json')) as f:
        config = json.load(f)
        logging.debug(f"Opened file at {package_root_pth.joinpath('config', 'settings.json')}\n{config}")
else:
    logging.error(f"Error identifying package root path at {package_root_pth}")


def get_mongo_client():
    """Returns a MongoDB client with default URI."""
    return MongoClient(config["mongodb"]["uri"])

# def db_name(client, db_name):
#     return str(config['mongodb']['db_name'])
