from flask import Flask
import asyncio
import os
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from pt_pump_up.orm.Author import Author
from pt_pump_up.orm.Language import Language
from pt_pump_up.orm.Dataset import Dataset
from pt_pump_up.orm.Conference import Conference
from pt_pump_up.orm.DatasetStats import DatasetStats
from pt_pump_up.orm.License import License


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


async def init_orm():
    client = AsyncIOMotorClient(
        "mongodb+srv://pt-pump-up.8fhov50.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority",
        tls=True,
        tlsCertificateKeyFile=os.path.join(
            CURRENT_PATH, "cert", "mongo.pem"),
    )

    # Initialize beanie with the Sample document class and a database
    await init_beanie(database=client.db_name, document_models=[Author, Language, Dataset, Conference, DatasetStats, License])


with app.app_context():
    asyncio.get_event_loop().run_until_complete(init_orm())


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/languages")
def languages():
    return [
        {'id': '1', 'name': 'European Portuguese', 'iso_code': 'pt-PT'},
        {'id': '2', 'name': 'Brazilian Portuguese', 'iso_code': 'pt-BR'},
        {'id': '3', 'name': 'American English', 'iso_code': 'en-US'},
    ]
