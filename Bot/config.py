from distutils.util import strtobool
import os
from dotenv import load_dotenv
from pyrogram.types import BotCommand


# Load environment variables from .env file
load_dotenv()


class Config(object):

    # Your API HASH
    API_HASH = os.environ.get('21866171')

    # Your API ID
    APP_ID = int(os.environ.get('5788dba8f23fade5edda55948e985f06'))

    # Your Bot Token
    BOT_TOKEN = os.environ.get('8147399877:AAEk1DTB1Hvy52wsjM96d2xzID83_0C5s1g')

    # Your Telegram ID (optional)
    OWNER_ID = os.environ.get('8082516546')

    # Upload method (default to False)
    AS_ZIP = bool(strtobool(os.environ.get('AS_ZIP', 'False')))

    # Channel/Group ID where you dump all the downloaded files.
    DUMP_ID = int(os.environ.get('DUMP_ID')
                  ) if os.environ.get('DUMP_ID') else None

    PLUGINS = {'root': 'Bot.plugins'}

    DOWNLOAD_DIR = "./downloads/"

    BOT_COMMANDS = [
        BotCommand('start', 'start bot'),
        BotCommand('help', 'help messages'),
        BotCommand('thumbnail', 'custom thumbnail'),
        BotCommand('caption', 'custom caption')
    ]
