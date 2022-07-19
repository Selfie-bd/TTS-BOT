import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5006643023:AAFuiTBrxHQWRNAO6i-XKCe0mQ4zlg6RtDM")

    APP_ID = int(os.environ.get("APP_ID", 2791256))

    API_HASH = os.environ.get("API_HASH", "cd2fb4cdc795334aee3fbbc83da463ce")
