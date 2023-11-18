from flask import jsonify, make_response
from pt_pump_up.orm.Dataset import Dataset


async def index(app, request):
    datasets = await Dataset.find_all().to_list()

    return make_response(datasets, 200)


async def create(app, request):
    pass

# TODO: Implement this


async def update(app, request):
    return make_response(jsonify({"message": "Not implemented"}), 501)

# TODO: Implement this


async def delete(app, request):
    return make_response(jsonify({"message": "Not implemented"}), 501)

# TODO: Implement this


async def get(app, request):
    return make_response(jsonify({"message": "Not implemented"}), 501)
