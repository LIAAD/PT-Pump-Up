from quart import Quart, Response, request, send_file
from init_server import init_orm
import os
import json
from pt_pump_up.orm.Dataset import Dataset, DatasetStats
from pt_pump_up.orm.Dataset import Hrefs as DatasetHrefs
from pt_pump_up.orm.Hrefs import Hrefs as ModelHrefs
from pt_pump_up.orm.Conference import Conference
from pt_pump_up.orm.Language import Language
from pt_pump_up.orm.Author import Author
from pt_pump_up.orm.Author import Hrefs as AuthorHrefs
from pt_pump_up.orm.Status import Status
from pt_pump_up.orm.NLPTask import NLPTask
from pt_pump_up.orm.Architecture import Architecture
from pt_pump_up.orm.Model import Model, ModelStats, MetricResult, Benchmark
from pt_pump_up.orm.Metric import Metric
from pt_pump_up.orm.Publication import Publication
from beanie import WriteRules
from beanie.operators import In
from quart_cors import cors


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

app = Quart(__name__, static_folder=os.path.join(
    CURRENT_PATH, 'build'), static_url_path='/')

app = cors(app, allow_origin="*")


def findall_to_json(documents):
    new_documents = [document.model_dump_json() for document in documents]
    json_string = ','.join(new_documents)
    json_string = '[' + json_string + ']'
    return json_string


@app.before_serving
async def init():
    await init_orm(CURRENT_PATH)


@app.route('/', defaults={'path': ''})
@app.route('/<path>', methods=['GET'])
async def index(path):
    return await send_file(os.path.join(CURRENT_PATH, 'build', 'index.html'))


@app.route('/api/homepage/', methods=['GET'])
async def get_homepage():

    datasets = findall_to_json(await Dataset.find_all(fetch_links=True).to_list())
    models = findall_to_json(await Model.find_all(fetch_links=True).to_list())
    authors = findall_to_json(await Author.find_all(fetch_links=True).to_list())
    publications = findall_to_json(await Publication.find_all(fetch_links=True).to_list())

    response = {
        'datasets': datasets,
        'models': models,
        'authors': authors,
        'publications': publications
    }
    return Response(status=200, response=json.dumps(response), content_type='application/json')


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

        nlp_tasks = await NLPTask.find(In(NLPTask.acronym, elem['nlp_tasks'])).to_list()

        if len(languages) != len(elem['languages']) or len(authors) != len(elem['authors']) or nlp_tasks is None:
            return Response(status=400)

        await Dataset(
            english_name=elem['english_name'],
            description=elem['description'],
            language_stats=[DatasetStats(language=language.id)
                            for language in languages],
            hrefs=DatasetHrefs(link_source=elem['link_source']),
            introduction_date=elem['introduction_data'],

            status=Status(broken_link=elem['status']['broken_link'], author_response=elem['status']['author_response'], standard_format=elem['status']
                          ['standard_format'], backup=elem['status']['backup'], preservation_rating=elem['status']['preservation_rating'], off_the_shelf=elem['status']['off_the_shelf']),

            authors=[author.id for author in authors],
            nlp_tasks=[nlp_tasks.id for nlp_tasks in nlp_tasks]
        ).insert(link_rule=WriteRules.WRITE)

    # Return 200 OK
    return Response(status=200)


@app.route('/api/languages/', methods=['POST'])
async def post_language():
    request_body = await request.get_json()

    for elem in request_body:
        await Language(
            name=elem['name'],
            iso_code=elem['iso_code'],
            papers_with_code_id=elem['papers_with_code_id']
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
            acronym=elem['acronym'],
            papers_with_code_ids=elem['papers_with_code_ids']
        ).insert(link_rule=WriteRules.WRITE)

    return Response(status=200)


@app.route('/api/architectures/', methods=['POST'])
async def post_architecture():
    request_body = await request.get_json()

    for elem in request_body:
        await Architecture(
            name=elem['name'],
        ).insert(link_rule=WriteRules.WRITE)

    return Response(status=200)


@app.route('/api/metrics/', methods=['POST'])
async def post_metric():
    request_body = await request.get_json()

    for elem in request_body:
        await Metric(
            name=elem['name'],
        ).insert(link_rule=WriteRules.WRITE)

    return Response(status=200)


@app.route('/api/models/', methods=['POST'])
async def post_model():

    async def parse_benchmarks(request_body):
        benchmarks = []

        for benchmark in request_body['benchmarks']:
            train_dataset = await Dataset.find_one(Dataset.english_name == benchmark['train_dataset'])
            test_dataset = await Dataset.find_one(Dataset.english_name == benchmark['test_dataset'])
            scores = [MetricResult(metric=(await Metric.find_one(Metric.name == score['metric'])).id, value=score['value']) for score in benchmark['scores']]
            benchmarks.append(Benchmark(
                train_dataset=train_dataset.id, test_dataset=test_dataset.id, scores=scores))

        return benchmarks

    request_body = await request.get_json()

    for elem in request_body:

        languages = await Language.find(In(Language.iso_code, elem['languages'])).to_list()
        authors = await Author.find(In(Author.hrefs.email, elem['authors'])).to_list()
        nlp_tasks = await NLPTask.find(In(NLPTask.acronym, elem['nlp_tasks'])).to_list()

        await Model(
            name=elem['name'],
            model_stats=ModelStats(
                architecture=(await Architecture.find_one(Architecture.name == elem['architecture'])).id,
                languages=[language.id for language in languages],
            ),
            hrefs=ModelHrefs(
                link_source=elem['link_source'],
            ),
            year=elem['year'],
            status=Status(broken_link=elem['status']['broken_link'], author_response=elem['status']['author_response'], standard_format=elem['status']
                          ['standard_format'], backup=elem['status']['backup'], preservation_rating=elem['status']['preservation_rating'], off_the_shelf=elem['status']['off_the_shelf']),
            authors=[author.id for author in authors],
            benchmarks=await parse_benchmarks(elem),
            nlp_tasks=[nlp_task.id for nlp_task in nlp_tasks]
        ).insert(link_rule=WriteRules.WRITE)

    return Response(status=200)


@app.route('/api/models/', methods=['GET'])
async def get_models():
    models = await Model.find_all(fetch_links=True).to_list()
    return Response(status=200, response=findall_to_json(models), content_type='application/json')


@app.route('/api/publications/', methods=['POST'])
async def post_publication():
    request_body = await request.get_json()

    for elem in request_body:

        authors = await Author.find(In(Author.hrefs.email, elem['authors'])).to_list()

        await Publication(
            title=elem['title'],
            abstract=elem['abstract'],
            authors=[author.id for author in authors],
            url_abstract=elem['url_abstract'],
            url_pdf=elem['url_pdf'],
            published_date=elem['published_date'],
            github_url=elem['github_url'],
            bibtex=elem['bibtex'],

        ).insert(link_rule=WriteRules.WRITE)

    return Response(status=200)
