from pt_pump_up_admin.integration.papers_with_code import Element
from pt_pump_up_admin.integration.papers_with_code.utils import bypass_select


class Dataset(Element):
    def __init__(self, name, full_name, url, introduced_data, license_name, license_url, modalities, languages, tasks, br=None):
        super().__init__(post_url="https://paperswithcode.com/contribute/dataset/new", br=br)
        self.name = name
        self.full_name = full_name
        self.url = url
        self.introduced_data = introduced_data
        self.license_name = license_name
        self.license_url = license_url
        self.modalities = modalities
        self.languages = languages
        self.tasks = tasks

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
        for modality in self.modalities:
            bypass_select(form=self.br.form, select_name='modalities',
                          value=modality)

        for language in self.languages:
            bypass_select(form=self.br.form, select_name='languages',
                          value=language)

        for task in self.tasks:
            bypass_select(form=self.br.form,
                          select_name='tasks', value=task)

        # Bypasse done. Now we can assign the values
        self.br.form['modalities'] = self.modalities
        self.br.form['languages'] = self.languages
        self.br.form['tasks'] = self.tasks

        req = self.br.submit()

        if req.code != 200:
            raise Exception('Insert failed')

        return req
