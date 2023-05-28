import re
from os import environ,sys
from sys import executable
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(message)s",
    handlers = [logging.FileHandler('bot.log'), logging.StreamHandler()]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

try:
    API_ID = int(environ['API_ID'])
    API_HASH = environ['API_HASH']
    BOT_TOKEN = environ['BOT_TOKEN']
    DB_URL = environ['DB_URL']
    DB_NAME = environ['DB_NAME']
    OWNER_ID = int(environ['OWNER_ID'])
except KeyError:
    LOGGER.debug("One or More ENV variable not found.")
    sys.exit(1)
# Optional Variable
SUDO_USERS = environ.get("SUDO_USERS",str(OWNER_ID)).split()
SUDO_USERS = [int(_x) for _x in SUDO_USERS]
if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)
ADMIN = int(environ['ADMIN'])
AUTH_CHATS = environ.get('AUTH_CHATS', None).split()
AUTH_CHATS = [int(_x) for _x in AUTH_CHATS]
START_PIC = environ['START_PIC']
LOG_GROUP = environ.get("LOG_GROUP", None)
if LOG_GROUP:
    LOG_GROUP = int(LOG_GROUP)
BUG = environ.get("BUG", None)
if BUG:
    BUG = int(BUG)
GENIUS_API = environ.get("GENIUS_API", None)
if GENIUS_API:
    GENIUS_API = GENIUS_API
