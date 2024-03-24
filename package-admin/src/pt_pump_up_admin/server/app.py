from flask import Flask, request, jsonify
from flask_cors import CORS
from pt_pump_up_orms.orms import Dataset
import requests
from pt_pump_up_admin.integration import P
from datasets import load_dataset
from transformers import pipeline

app = Flask(__name__)
CORS(app)


def _extract_varieties_stats(varieties):
    raise NotImplementedError
    model = pipeline('text-classification', model="")
    dataset_dict = load_dataset(dataset.link.hugging_face_url.split('/')[-1])

    for split in ['train', 'validation', test]:
        for text in dataset_dict[split]:
            model(text)


@app.route('/papers_with_code/insert_dataset', methods=['POST'])
def event_insert_dataset():
    raise NotImplementedError

    dataset = Dataset(**request.json)

    if dataset.link.papers_with_code_url:
        # Push Dataset to PapersWithCode
        raise NotImplementedError

    if dataset.link.hugging_face_url:
        varieties = _extract_varieties_stats(dataset.link.hugging_face_url)

    # Extract Language Variety Stats
    varieties = None


# Parse Json request for crawl websites
@app.route('/fetch_resources', methods=['POST'])
def event_fetch_resources():
    raise NotImplementedError
