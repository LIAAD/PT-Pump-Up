from quart import Quart
from init_server import init_orm
import os
import json
from pt_pump_up.orm.Dataset import Dataset

app = Quart(__name__)

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


@app.before_serving
async def init():
    await init_orm(CURRENT_PATH)

# Your routes here


@app.route('/')
async def hello():
    return 'hello'


@app.route('/api/datasets', methods=['GET'])
async def get_datasets():
    datasets = await Dataset.find_all().to_list()
    return json.dumps(datasets, default=str)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
