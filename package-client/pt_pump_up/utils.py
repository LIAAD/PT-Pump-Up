import requests
import logging
import pandas as pd


def fetch_resources(url, endpoint, element, nlp_task="all", use_cache=True):
    if element is not None and use_cache:
        logging.info(f"Using cached")
        return element

    response = requests.get(f"{url}/api/{endpoint}/", headers={
        "Accept": "application/json",
    })

    if response.status_code != 200:
        raise Exception(f"Error while fetching status code {response.status_code}")

    data = response.json()

    if nlp_task != "all":
        data = [elem for elem in data if any(
            task["name"] == nlp_task or task["acronym"] == nlp_task for task in elem["nlp_tasks"])]

    element = pd.DataFrame(data=data)
    element.set_index("english_name", inplace=True)

    return element
