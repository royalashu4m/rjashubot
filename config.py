# yooo guiz Herox 
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "LittelStar_org")
API_ID = int(getenv("API_ID", "8945070"))
API_HASH = getenv("API_HASH", "")
OWNER_NAME = getenv("OWNER_NAME", "Herox_xd")
ALIVE_NAME = getenv("ALIVE_NAME", "RJAshu")
BOT_USERNAME = getenv("BOT_USERNAME", "Rjashu_robot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "LittelStar_org")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "LittelStar_org")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LittelStar_org")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5124507794").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ? + - *").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/2c1035f056f495a59e1c6.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "70"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/royalashu4m/rjashubot")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/2c1035f056f495a59e1c6.jpg")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/596f75a52ea9bf0109644.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")

