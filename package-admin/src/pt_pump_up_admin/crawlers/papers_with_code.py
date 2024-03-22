from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


class PapersWithCode:
    @staticmethod
    def extract_tasks():
        url = "https://paperswithcode.com/datasets?mod=texts&page=1"

        response = requests.get(url)

        df_tasks = pd.DataFrame(columns=[
            "id",
            "task_name",
        ])

        if response.status_code != 200:
            raise Exception("Failed to fetch tasks from PapersWithCode")

        soup = BeautifulSoup(
            response.content,
            "html.parser"
        )

        # First div is modality, second is task, third is dataset
        task_div = soup.find_all("div", class_="datasets-filter")[1]

        for task in task_div.find_all("a", class_="filter-item"):
            task = " ".join(task.text.split())
            task_name = re.search(r'\D+', task).group().strip()
            id = re.search(r'\d+', task).group()

            df_tasks = pd.concat([df_tasks, pd.DataFrame({
                "id": [int(id)],
                "task_name": [task_name]
            })])

        return df_tasks
