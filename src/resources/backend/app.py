from quart import Quart, Response, request
from init_server import init_orm
import os
import json
from pt_pump_up.orm.Dataset import Dataset, Hrefs
from pt_pump_up.orm.Conference import Conference
from pt_pump_up.orm.Language import Language
from pt_pump_up.orm.Author import Author
from pt_pump_up.orm.DatasetStats import DatasetStats
from beanie import WriteRules
from bson import ObjectId


app = Quart(__name__)

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


@app.before_serving
async def init():
    await init_orm(CURRENT_PATH)


@app.route('/')
async def hello():
    return 'hello'


@app.route('/api/datasets/', methods=['GET'])
async def get_datasets():
    datasets = await Dataset.find_all(fetch_links=True).to_list()
    return json.dumps(datasets, default=str)


@app.route('/api/datasets/create/', methods=['GET'])
async def create_datasets():
    conferences = await Conference.find_all(fetch_links=True).to_list()
    languages = await Language.find_all(fetch_links=True).to_list()
    authors = await Author.find_all(fetch_links=True).to_list()

    return Response(status=200, response=json.dumps({
        'conferences': conferences,
        'languages': languages,
        'authors': authors
    }, default=str))


@app.route('/api/datasets/', methods=['POST'])
async def post_datasets():
    request_body = await request.get_json()

    for elem in request_body:

        await Dataset(
            name=elem['name'],
            language_stats=[DatasetStats(language=elem)
                            for elem in elem['language_stats']],
            conference=elem['conference'],
            hrefs=Hrefs(link_source=elem['link_source']),
            year=elem['year'],
            status=elem['status'],
            authors=[author for author in elem['authors']]
        ).insert(link_rule=WriteRules.WRITE)

    # Return 200 OK
    return Response(status=200)


@app.route('/api/languages/', methods=['POST'])
async def post_language():
    request_body = await request.get_json()

    for elem in request_body:
        await Language(
            name=elem['name'],
            iso_code=elem['iso_code']
        ).insert(link_rule=WriteRules.WRITE)

    return Response(status=200)

# TODO: Create Conference


@app.route('/api/conferences/', methods=['POST'])
async def post_conference():
    request_body = await request.get_json()

    for elem in request_body:
        await Conference(
            name=elem['name'],
            year=elem['year']
        ).insert(link_rule=WriteRules.WRITE)

    return Response(status=200)


@app.route('/api/authors/', methods=['POST'])
async def post_author():
    request_body = await request.get_json()

    for elem in request_body:
        await Author(
            name=elem['name'],
            affiliation=elem['affiliation'],
            email=elem['email']
        ).insert(link_rule=WriteRules.WRITE)

    return Response(status=200)
