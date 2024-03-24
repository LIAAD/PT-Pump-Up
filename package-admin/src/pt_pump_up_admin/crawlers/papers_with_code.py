from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from urllib.parse import parse_qs, urlparse
from tqdm import tqdm


class PapersWithCode:

    @staticmethod
    def _extract_name(task):
        task_value = " ".join(task.text.split())

        full_name = re.search(r'\D+', task_value).group().strip()

        # If there is text inside parentheses. The short name is the text outside the parentheses
        short_name = re.search(r'\(([^)]+)', task_value)
        short_name = short_name.group(1) if short_name else None

        return full_name, short_name

    @staticmethod
    def _extract_url(task):
        query_parser = parse_qs(urlparse(task.get("href")).query)
        task = query_parser.get("task")[0]

        return f"https://paperswithcode.com/task/{task}"

    @staticmethod
    def _extract_task_information(url):

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        id = int(soup.find("input", id="id_task")["value"].strip())
        description = soup.find(
            "div", class_="description-content").get_text(strip=True)

        return id, description

    @staticmethod
    def extract_tasks(filepath=None):
        url = "https://paperswithcode.com/datasets?mod=texts&page=1"

        response = requests.get(url)

        df_tasks = pd.DataFrame(columns=['short_name', 'full_name', 'description',
                                'standard_format', 'papers_with_code_id', 'papers_with_code_url'])

        if response.status_code != 200:
            raise Exception("Failed to fetch tasks from PapersWithCode")

        soup = BeautifulSoup(
            response.content,
            "html.parser"
        )

        # First div is modality, second is task, third is dataset
        task_div = soup.find_all("div", class_="datasets-filter")[1]

        for task in tqdm(task_div.find_all("a", class_="filter-item")):

            url = PapersWithCode._extract_url(task)

            full_name, short_name = PapersWithCode._extract_name(task)

            id, description = PapersWithCode._extract_task_information(url)

            df_tasks = pd.concat([df_tasks, pd.DataFrame({
                "short_name": [short_name],
                "full_name": [full_name],
                "description": [description],
                "standard_format": None,
                "papers_with_code_id": [id],
                "papers_with_code_url": [url]
            })])

        if filepath:
            df_tasks.to_json(filepath, orient="records",
                             lines=False, force_ascii=False)

        return df_tasks
