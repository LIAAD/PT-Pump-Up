from pt_pump_up_admin.integration.papers_with_code import Element
from pt_pump_up_admin.integration.papers_with_code.utils import bypass_select
from pt_pump_up_orms import Dataset


class Dataset(Element):
    def __init__(self, dataset: Dataset, modalities=[6], languages=[22], br=None):
        super().__init__(post_url="https://paperswithcode.com/contribute/dataset/new", br=br)
        self.name = dataset.json['short_name']
        self.full_name = dataset.json['full_name']
        self.url = dataset.json['link']['website']
        self.introduced_data = dataset.json['year']

        # TODO: Add support for license
        self.license_name = ""
        self.license_url = ""

        # TODO: Add support for multiple modalities and languages
        # Text Modality is 6
        self.modalities = modalities
        # Portuguese language id is 22
        self.languages = languages

        for nlp_task in dataset.json['nlp_tasks']:
            if self.tasks_ids is None:
                self.tasks_ids = nlp_task.json['papers_with_code_ids']
            else:
                self.tasks_ids.extend(nlp_task.json['papers_with_code_ids'])

    def insert(self):
        self.br.open(self.post_url)
        self.br.select_form(nr=2)

        self.br.form['name'] = self.name
        self.br.form['full_name'] = self.full_name
        self.br.form['description'] = self.description
        self.br.form['url'] = self.url
        self.br.form['introduced_date'] = self.introduced_data
        self.br.form['license_name'] = self.license_name
        self.br.form['license_url'] = self.license_url

        # Selects must be bypassed
        for modality_id in self.modalities_ids:
            bypass_select(form=self.br.form, select_name='modalities',
                          value=modality_id)

        for language_id in self.languages_ids:
            bypass_select(form=self.br.form, select_name='languages',
                          value=language_id)

        for task_id in self.tasks_ids:
            bypass_select(form=self.br.form,
                          select_name='tasks', value=task_id)

        # Bypasse done. Now we can assign the values
        self.br.form['modalities'] = self.modalities
        self.br.form['languages'] = self.languages
        self.br.form['tasks'] = self.tasks

        req = self.br.submit()

        if req.code != 200:
            raise Exception('Insert failed')

        return req
