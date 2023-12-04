import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    # Retrieve the database name from an environment variable
    database_name = os.environ.get("habit-tracker-app")

    # Replace "your_database_name" with the actual name of your MongoDB database
    client = MongoClient(f"mongodb+srv://datlagu:<pw>@microblog-app.cdegwje.mongodb.net/{'db_name'}?retryWrites=true&w=majority")
    
    # Explicitly specify the database name
    app.db = client.get_database(database_name)

    app.register_blueprint(pages)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()

