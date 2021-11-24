import os


class Dependencies:
    """Server Required Dependencies"""
    pass


class Config:
    DB_VERSION = 1
    
    APP_NAME = "RTCS"

    MONGODB_URI = os.environ[APP_NAME + "_MONGODB_URI"]
    MONGODB_NAME = os.environ[APP_NAME + "_MONGODB_NAME"]
    API_SECRET_KEY = os.environ[APP_NAME + "_SEOUL_DATA_CENTER_SECRET_KEY"]
