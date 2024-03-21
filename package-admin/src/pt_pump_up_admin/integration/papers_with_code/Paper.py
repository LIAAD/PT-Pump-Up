from pt_pump_up_admin.integration.papers_with_code import Element


class Paper(Element):
    def __init__(self, title, abstract, authors, url_abstract, url_pdf, published_date, journal, github_url, br=None):
        super().__init__(post_url="https://paperswithcode.com/submit-paper", br=br)
        self.title = title
        self.abstract = abstract
        self.authors = authors
        self.url_abstract = url_abstract
        self.url_pdf = url_pdf
        self.published_date = published_date
        self.journal = journal
        self.github_url = github_url

    def insert(self):
        self.br.open(self.post_url)
        self.br.select_form(nr=2)

        self.br.form['title'] = self.title
        self.br.form['abstract'] = self.abstract
        self.br.form['authors'] = ",".join(self.authors)
        self.br.form['url_abs'] = self.url_abstract
        self.br.form['url_pdf'] = self.url_pdf
        self.br.form['published'] = self.published_date
        self.br.form['journal_or_conference'] = self.journal
        self.br.form['github_url'] = self.github_url

        req = self.br.submit()

        if req.code != 200:
            raise Exception('Insert failed')
