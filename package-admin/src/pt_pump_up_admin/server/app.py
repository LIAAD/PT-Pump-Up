from flask import Flask, request, jsonify
from flask_cors import CORS
from pt_pump_up_orms.orms import Dataset
import requests
from pt_pump_up_admin.integration import P

app = Flask(__name__)
CORS(app)

# Parse Json request for train decision tree

# Parse Json request for inference decision tree

# Parse Json request for papers with code insert paper

# Parse Json request for papers with code insert dataset

@app.route('/papers_with_code/insert_dataset', methods=['POST'])
def event_insert_dataset():
    dataset = Dataset(**request.json)

    # Push Dataset to PapersWithCode
    
    


# Parse Json request for crawl websites
