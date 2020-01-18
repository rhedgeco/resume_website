from pathlib import Path

from backend.general_manager.databases import SqliteDatabase
from general_falcon_webserver import WebApp

from api.database_manager import DatabaseManager

app = application = WebApp('frontend', 'page404.html')

with open(Path('api') / 'database_config.sql') as file:
    db_config = file.read()
db = SqliteDatabase('resume_website', db_config)
manager = DatabaseManager(db)

app.launch_webserver()
