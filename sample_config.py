from telethon.tl.types import ChatBannedRights

#Edit all values here. If there's a value None, replace it with "" and set your data into it.

class Config(object):
    LOGGER = True
    # Default .alive name
    ALIVE_NAME = ""
    # For customizing there alive message
    CUSTOM_ALIVE_TEXT = "My Telethon is online!"
    CUSTOM_ALIVE_EMOJI = None
    # for profile default name
    AUTONAME = None
    # Get this value from my.telegram.org! Please do not steal
    APP_ID = int("")
    API_HASH = ""
    STRING_SESSION = ""
    # For Databases, get from elephantsql.com
    DB_URI = ""
    SCREEN_SHOT_LAYER_ACCESS_KEY = None
    # string session for running on Heroku
    # some people upload their session files on GitHub or other third party hosting
    # websites, this might prevent the un-authorized use of the
    # confidential session files
    # Get your own APPID from https://api.openweathermap.org/data/2.5/weather
    OPEN_WEATHER_MAP_APPID = None
    # Send .get_id in any group to fill this value.
    PRIVATE_GROUP_BOT_API_ID = ""
    if PRIVATE_GROUP_BOT_API_ID:
        PRIVATE_GROUP_BOT_API_ID = int(PRIVATE_GROUP_BOT_API_ID)
    # same as  PRIVATE_GROUP_BOT_API_ID but set only if you need pmpermit
    PRIVATE_GROUP_ID = None
    if PRIVATE_GROUP_ID:
        PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
    PLUGIN_CHANNEL = ""
    if PLUGIN_CHANNEL:
        PLUGIN_CHANNEL = int(PLUGIN_CHANNEL)
    # Send .get_id in any channel to fill this value. ReQuired for @Manuel15
    # inspiration to work!
    PRIVATE_CHANNEL_BOT_API_ID = ""
    if PRIVATE_CHANNEL_BOT_API_ID:
        PRIVATE_CHANNEL_BOT_API_ID = int(PRIVATE_CHANNEL_BOT_API_ID)
    # This is required for the speech to text plugin. Get your USERNAME from
    # https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
    IBM_WATSON_CRED_URL = None
    IBM_WATSON_CRED_PASSWORD = None
    # This is required for the @telegraph functionality.
    TELEGRAPH_SHORT_NAME = "caty"
    # Set False to stop deleting old welcome messages
    CLEAN_WELCOME = True
    # github vars
    GITHUB_ACCESS_TOKEN = None
    GIT_REPO_NAME = None
    # Get a Free API Key from OCR.Space
    OCR_SPACE_API_KEY = ""
    # TG API limit. An album can have atmost 10 media!
    TG_GLOBAL_ALBUM_LIMIT = int(9)
    # Telegram BOT Token from @BotFather
    TG_BOT_TOKEN_BF_HER = ""
    TG_BOT_USER_NAME_BF_HER = ""
    THUMB_IMAGE = ""
    # Genius lyrics get this value from https://genius.com/developers both has
    # same values
    GENIUS_API_TOKEN = ""
    # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
    # TG API limit. A message can have maximum 4096 characters!
    MAX_MESSAGE_SIZE_LIMIT = 4095
    # set blacklist_chats where you do not want userbot's features
    UB_BLACK_LIST_CHAT = {
        int(x) for x in "".split()
    }

    # specify LOAD and NO_LOAD
    LOAD = []
    # foloowing plugins won't work on Heroku,
    # because of their ephemeral file system
    MAX_ANTI_FLOOD_MESSAGES = 10
    # warn mode for anti flood
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None, view_messages=None, send_messages=True
    )
    CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
    # specify LOAD and NO_LOAD
    NO_LOAD = [x for x in "".split()]
    # in alive message pic
    ALIVE_PIC = None
    # in pm permit pic
    PMPERMIT_PIC = None
    DIGITAL_PIC = None
    DEFAULT_PIC = None
    CUSTOM_PMPERMIT_TEXT = None
    # Get your own API key from https://www.remove.bg/ or
    # feel free to use http://telegram.dog/Remove_BGBot
    REM_BG_API_KEY = ""
    # number of rows of buttons to be displayed in .help command
    NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = int(7)
    # number of rows of buttons to be displayed in .helpme command
    NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD = int(3)
    # emoji to be displayed in .help
    EMOJI_TO_DISPLAY_IN_HELP = " "
    # specify command handler that should be used for the plugins
    # this should be a valid "regex" pattern
    COMMAND_HAND_LER = r"\."
    SUDO_COMMAND_HAND_LER = r"\!"
    # specify list of users allowed to use bot
    # WARNING: be careful who you grant access to your bot.
    # malicious users could do ".exec rm -rf /*"
    SUDO_USERS = {int(x) for x in "".split()}
    # Leave this stuff
    CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
    CHROME_DRIVER = "/app/.chromedriver/bin/chromedriver"
    # Google Drive plugin
    G_DRIVE_CLIENT_ID = None
    G_DRIVE_CLIENT_SECRET = None
    G_DRIVE_FOLDER_ID = None
    G_DRIVE_AUTH_TOKEN_DATA = None
    G_DRIVE_DATA = None
    G_DRIVE_INDEX_LINK = None
    TMP_DOWNLOAD_DIRECTORY = "./downloads"
    # for heroku plugin
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    # For transfer channel
    TELE_GRAM_2FA_CODE = ""
    # for sed plugin
    GROUP_REG_SED_EX_BOT_S = r"(regex|moku|BananaButler_|rgx|l4mR)bot"
    # rapidleech plugins
    # Google Chrome Selenium Stuff
    # taken from
    # https://github.com/jaskaranSM/UniBorg/blob/9072e3580cc6c98d46f30e41edbe73ffc9d850d3/sample_config.py#L104-L106
    TEMP_DIR = "./temp/"
    # spotify stuff
    DEFAULT_BIO = None
    SPOTIFY_BIO_PREFIX = None
    SPOTIFY_PASS = None
    SPOTIFY_USERNAME = None
    LYDIA_API = None
    DEFAULT_NAME = ""
    # define "spam" in PMs
    MAX_FLOOD_IN_P_M_s = int(5)
    # leave this blank, should be automatically filled for Heroku.com users
    PM_LOGGR_BOT_API_ID = None
    if PM_LOGGR_BOT_API_ID:
        PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)
    # to work manager.py
    DUAL_LOG = False
    # MONGOCLIENT = pymongo.MongoClient(MONGO_DB_URI)
    # MONGO = MONGOCLIENT.userbot
    # JustWatch Country
    WATCH_COUNTRY = "IN"
    TZ = "europe/berlin"
    RSS_POST_MSG_GROUP_ID = None
    if RSS_POST_MSG_GROUP_ID:
        RSS_POST_MSG_GROUP_ID = int(RSS_POST_MSG_GROUP_ID)
    # SpamWatch API you can get it from get api from http://t.me/SpamWatchBot?start=token
    SPAMWATCH_API = None
    # SpamWatch, CAS, SpamProtection ban Needed or not
    ANTISPAMBOT_BAN = False
    # Deepai value can get from https://deepai.org/
    DEEP_AI = ""
    # For custom stickerpack names
    CUSTOM_STICKER_PACKNAME = None
    # Owner id to show profile link of given id as owner
    OWNER_ID = ""
    if OWNER_ID:
        OWNER_ID = int(OWNER_ID)
    # Last.fm plugin
    BIO_PREFIX = None
    DEFAULT_BIO = None
    LASTFM_API = None
    LASTFM_SECRET = None
    LASTFM_USERNAME = None
    LASTFM_PASSWORD_PLAIN = None
    # time.py
    COUNTRY = str("")
    TZ_NUMBER = int(1)
    #  for updater plugin
    UPSTREAM_REPO_URL = "https://github.com/tinybotstg/catuserbot.git"
    UPSTREAM_REPO_BRANCH = "main"
    # can get from https://coffeehouse.intellivoid.net/
    LYDIA_API_KEY = None
    CHANGE_TIME = int(60)


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
