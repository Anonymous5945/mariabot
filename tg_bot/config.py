from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 395357593  # my telegram ID
    OWNER_USERNAME = "inferno59"  # my telegram username
    API_KEY = "1166885639:AAFDYnzxSi9D4m9qefNncAM0NPN6WuYiuKI"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = False
    SUDO_USERS = [395357593]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
