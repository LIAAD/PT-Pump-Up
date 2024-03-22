import os
from pt_pump_up_admin.crawlers import PapersWithCode

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def test_crawler_nlp_tasks():
    df_tasks = PapersWithCode.extract_tasks(filepath=os.path.join(
        CURRENT_DIR, "data", "papers_with_code_tasks.json"))

    assert len(df_tasks) > 0
