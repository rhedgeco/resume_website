import json

from general_falcon_webserver.backend.general_manager.databases import SqliteDatabase
from datetime import datetime

TIME_FORMAT = '%d/%m/%Y %H:%M:%S'


class DatabaseManager:

    def __init__(self, database: SqliteDatabase):
        self.db = database

    def get_user(self, username: str):
        return self.db.fetchone_query(f"SELECT * FROM users WHERE username='{username}'")