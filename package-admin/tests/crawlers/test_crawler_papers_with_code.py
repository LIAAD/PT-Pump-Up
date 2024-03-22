from pt_pump_up_admin.crawlers import PapersWithCode


def test_crawler_nlp_tasks():
    df_tasks = PapersWithCode.extract_tasks()

    df_tasks.to_json(
        "tests/data/papers_with_code_tasks.json",
        orient="records"
    )

    assert len(df_tasks) > 0
