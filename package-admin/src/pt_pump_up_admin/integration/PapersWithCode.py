from mechanize import Browser
from environs import Env

env = Env()
env.read_env()


class PapersWithCode:
    @staticmethod
    def create(username: str = None, password: str = None):
        br = Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        br.open('https://paperswithcode.com/accounts/login?next=/')
        br.select_form(nr=2)

        br.form['username'] = username if username else env.str(
            "PAPERS_WITH_CODE_USERNAME")
        br.form['password'] = password if password else env.str(
            "PAPERS_WITH_CODE_PASSWORD")

        req = br.submit()

        if req.code != 200:
            raise Exception('Login failed')

        return br
