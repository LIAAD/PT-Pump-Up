from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
import os

from pt_pump_up.orm.Author import Author
from pt_pump_up.orm.Language import Language
from pt_pump_up.orm.Dataset import Dataset
from pt_pump_up.orm.Conference import Conference
from pt_pump_up.orm.License import License
from pt_pump_up.orm.NLPTask import NLPTask
from pt_pump_up.orm.Architecture import Architecture
from pt_pump_up.orm.Metric import Metric
from pt_pump_up.orm.Model import Model
from pt_pump_up.orm.Publication import Publication



async def init_orm(CURRENT_PATH):
    client = AsyncIOMotorClient(
        "mongodb+srv://pt-pump-up.8fhov50.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority",
        tls=True,
        tlsCertificateKeyFile=os.path.join(
            CURRENT_PATH, "cert", "mongo.pem"),
    )

    # Initialize beanie with the Sample document class and a database
    await init_beanie(database=client[os.getenv('mongo_database')], document_models=[
        Author, Language, Dataset, Conference, License, NLPTask, Architecture, Metric, Model, Publication])
