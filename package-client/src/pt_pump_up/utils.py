import requests
import logging
import pandas as pd

# TODO: Reduce the size of the function, by creating a function to fetch the data and another to filter it

def fetch_resources(url, endpoint, element, nlp_task="all", use_cache=True):
    if element is not None and use_cache:
        logging.info(f"Using cached")
        return element

    response = requests.get(f"{url}/api/{endpoint}/", headers={
        "Accept": "application/json",
    })

    if response.status_code != 200:
        raise Exception(
            f"Error while fetching status code {response.status_code}")

    data = response.json()

    if nlp_task != "all":
        data = [elem for elem in data if any(
            task["short_name"] == nlp_task or task["full_name"] == nlp_task for task in elem["nlp_tasks"])]

    element = pd.DataFrame(data=data)

    return element
