from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
import os

from pt_pump_up.orm.Author import Author
from pt_pump_up.orm.Language import Language
from pt_pump_up.orm.Dataset import Dataset
from pt_pump_up.orm.Conference import Conference
from pt_pump_up.orm.DatasetStats import DatasetStats
from pt_pump_up.orm.License import License
from pt_pump_up.orm.NLPTask import NLPTask


async def init_orm(CURRENT_PATH):
    client = AsyncIOMotorClient(
        "mongodb+srv://pt-pump-up.8fhov50.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority",
        tls=True,
        tlsCertificateKeyFile=os.path.join(
            CURRENT_PATH, "cert", "mongo.pem"),
    )

    # Initialize beanie with the Sample document class and a database
    await init_beanie(database=client.db_name, document_models=[
        Author, Language, Dataset, Conference, DatasetStats, License, NLPTask])
