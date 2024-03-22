from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from urllib.parse import parse_qs, urlparse
from tqdm import tqdm
import os


class PapersWithCode:

    @staticmethod
    def _extract_description(task):

        # Extract query string task=
        query_parser = parse_qs(urlparse(task.get("href")).query)
        task = query_parser.get("task")[0]

        # Construct URL
        url = f"https://paperswithcode.com/task/{task}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Obtain div with class description-content
        description = soup.find(
            "div", class_="description-content").get_text(strip=True)

        return url, description

    @staticmethod
    def extract_tasks(filepath=None):
        url = "https://paperswithcode.com/datasets?mod=texts&page=1"

        response = requests.get(url)

        df_tasks = pd.DataFrame(columns=[
            "id",
            "task_name",
            "description",
            "papers_with_code_url"
        ])

        if response.status_code != 200:
            raise Exception("Failed to fetch tasks from PapersWithCode")

        soup = BeautifulSoup(
            response.content,
            "html.parser"
        )

        # First div is modality, second is task, third is dataset
        task_div = soup.find_all("div", class_="datasets-filter")[1]

        for task in tqdm(task_div.find_all("a", class_="filter-item")):

            task_value = " ".join(task.text.split())

            task_name = re.search(r'\D+', task_value).group().strip()
            id = re.search(r'\d+', task_value).group()

            papers_with_code_url, description = PapersWithCode._extract_description(
                task)

            df_tasks = pd.concat([df_tasks, pd.DataFrame({
                "id": [int(id)],
                "task_name": [task_name],
                "description": [description],
                "papers_with_code_url": [papers_with_code_url]
            })])

        if filepath:
            df_tasks.to_json(filepath, orient="records",
                             lines=False, force_ascii=False)

        return df_tasks
