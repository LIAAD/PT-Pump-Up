from abc import abstractmethod, ABC
from mechanize import Item, Browser
import logging


class PaperWithCodeElement(ABC):
    @abstractmethod
    def insert(self, br: Browser) -> list:
        pass

    def bypass_select(self, form, select_name, value):
        select_control = form.find_control(name=select_name)

        select_control.items.append(
            Item(select_control, {"name": value, "value": value})
        )


class PapersWithCodeDataset(PaperWithCodeElement):
    def __init__(self, name, full_name, description, url, introduced_data, license_name, license_url, modalities: list, languages: list, tasks: list) -> None:
        self.post_url = "https://paperswithcode.com/contribute/dataset/new"
        self.name = name
        self.full_name = full_name
        self.description = description
        self.url = url
        self.introduced_data = introduced_data
        self.license_name = license_name
        self.license_url = license_url
        self.modalities = modalities
        self.languages = languages
        self.tasks = tasks

    def insert(self, br: Browser) -> list:
        logging.info("Inserting dataset: " + self.name)

        br.open(self.post_url)
        br.select_form(nr=2)

        br.form['name'] = self.name
        br.form['full_name'] = self.full_name
        br.form['description'] = self.description
        br.form['url'] = self.url
        br.form['introduced_date'] = self.introduced_data
        br.form['license_name'] = self.license_name
        br.form['license_url'] = self.license_url

        # Selects must be bypassed
        for modality in self.modalities:
            self.bypass_select(form=br.form, select_name='modalities',
                               value=modality)

        for language in self.languages:
            self.bypass_select(form=br.form, select_name='languages',
                               value=language)

        for task in self.tasks:
            self.bypass_select(form=br.form, select_name='tasks', value=task)

        # Bypasse done. Now we can assign the values
        br.form['modalities'] = self.modalities
        br.form['languages'] = self.languages
        br.form['tasks'] = self.tasks

        logging.info("Inserting Dataset: " + self.name)
        return br.submit().code


class PaperWithCodePaper(PaperWithCodeElement):
    def __init__(self, title, abstract, authors: list, url_abstract, url_pdf, published_date, journal, github_url="") -> None:
        self.post_url = "https://paperswithcode.com/submit-paper"
        self.title = title
        self.abstract = abstract
        self.authors = authors
        self.url_abstract = url_abstract
        self.url_pdf = url_pdf
        self.published_date = published_date
        self.journal = journal
        self.github_url = github_url

    def insert(self, br: Browser) -> list:
        logging.info("Inserting paper")
        br.open(self.post_url)
        br.select_form(nr=2)

        br.form['title'] = self.title
        br.form['abstract'] = self.abstract
        br.form['authors'] = ",".join(self.authors)
        br.form['url_abs'] = self.url_abstract
        br.form['url_pdf'] = self.url_pdf
        br.form['published'] = self.published_date
        br.form['journal_or_conference'] = self.journal
        br.form['github_url'] = self.github_url

        logging.info("Inserting paper: " + self.title)

        return br.submit().code


class PapersWithCode:
    def __init__(self, username, password) -> None:
        self.br = Browser()
        self.br.set_handle_robots(False)
        self.br.addheaders = [
            ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        self.login(username, password)

    def login(self, username, password) -> int:

        self.br.open("https://paperswithcode.com/accounts/login?next=/")
        self.br.select_form(nr=2)
        self.br.form['username'] = username
        self.br.form['password'] = password
        req = self.br.submit()
        return req.code

    def insert(self, element: PaperWithCodeElement) -> int:

        code = element.insert(self.br)

        if code == 200:
            logging.info("Element inserted successfully")
        else:
            logging.error("Error inserting element")

        return code
