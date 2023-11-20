from quart import Quart, Response, request
from init_server import init_orm
import os
import json
from pt_pump_up.orm.Dataset import Dataset, Status
from pt_pump_up.orm.Dataset import Hrefs as DatasetHrefs
from pt_pump_up.orm.Conference import Conference
from pt_pump_up.orm.Language import Language
from pt_pump_up.orm.Author import Author
from pt_pump_up.orm.Author import Hrefs as AuthorHrefs
from pt_pump_up.orm.DatasetStats import DatasetStats
from beanie import WriteRules
from pt_pump_up.orm.NLPTask import NLPTask
from beanie.operators import In
from quart_cors import cors
from bson.json_util import dumps


app = Quart(__name__)

app = cors(app, allow_origin="*")

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def findall_to_json(documents):
    new_documents = [document.model_dump_json() for document in documents]
    json_string = ','.join(new_documents)
    json_string = '[' + json_string + ']'
    return json_string


@app.before_serving
async def init():
    await init_orm(CURRENT_PATH)


@app.route('/')
async def hello():
    return 'hello'


@app.route('/api/datasets/', methods=['GET'])
async def get_datasets():
    datasets = await Dataset.find_all(fetch_links=True).to_list()
    return Response(status=200, response=findall_to_json(datasets), content_type='application/json')


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
        """
        await Dataset(
            name=elem['name'],
            language_stats=[DatasetStats(language=elem)
                            for elem in elem['language_stats']],
            conference=elem['conference'],
            hrefs=Hrefs(link_source=elem['link_source']),
            year=elem['year'],
            status=elem['status'],
            authors=[author for author in elem['authors']],
            nlp_task=[nlp_task for nlp_task in elem['nlp_task']
        ).insert(link_rule=WriteRules.WRITE)
        """

        # conference = await Conference.find_one({'name': elem['conference']})

        languages = await Language.find(In(Language.iso_code, elem['languages'])).to_list()

        authors = await Author.find(In(Author.hrefs.email, elem['authors'])).to_list()

        nlp_task = await NLPTask.find(In(NLPTask.acronym, elem['nlp_task'])).to_list()

        if len(languages) != len(elem['languages']) or len(authors) != len(elem['authors']) or nlp_task is None:
            return Response(status=400)

        await Dataset(
            name=elem['name'],
            language_stats=[DatasetStats(language=language.id)
                            for language in languages],
            hrefs=DatasetHrefs(link_source=elem['link_source']),
            year=elem['year'],

            status=Status(broken_link=elem['status']['broken_link'], author_response=elem['status']['author_response'], standard_format=elem['status']
                          ['standard_format'], backup=elem['status']['backup'], preservation_rating=elem['status']['preservation_rating'], off_the_shelf=elem['status']['off_the_shelf']),

            authors=[author.id for author in authors],
            nlp_task=[nlp_task.id for nlp_task in nlp_task]
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
            hrefs=AuthorHrefs(email=elem['email'])
        ).insert(link_rule=WriteRules.WRITE)

    return Response(status=200)


@app.route('/api/nlp_tasks/', methods=['POST'])
async def post_nlp_task():
    request_body = await request.get_json()

    for elem in request_body:
        await NLPTask(
            name=elem['name'],
            acronym=elem['acronym']
        ).insert(link_rule=WriteRules.WRITE)

    return Response(status=200)
