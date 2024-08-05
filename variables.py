# https://github.com/Infamous-Hydra/YaeMikos
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 28243586  # Get this value from my.telegram.org/apps
    API_HASH = "4022d5686b9b7a7cf8891205921a0ab3"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgresql://postgres:OMmMozXruEulVmeqrGqDmzCpMquwDOoU@postgres.railway.internal:5432/railway"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = --1002235766670
    MESSAGE_DUMP = --1002249319477

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://madarazbotz:uAcFszAkr5zoiyuv@cluster0.hep1w7t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Support chat and support ID
    SUPPORT_CHAT = "unreal_x_support"
    SUPPORT_ID = -1002211086274

    # Database name
    DB_NAME = "Cluster0"

    # Bot token
    TOKEN = "7202673383:AAE_LuVDJyfD41EQGx6bJCr5Dk97vMKpPV4"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 5340652544
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = []  # Sudo users
    DEV_USERS = []  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
