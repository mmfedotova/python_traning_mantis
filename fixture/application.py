from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from fixture.session import SessionHelper
from fixture.project_helper import ProjectHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == "chrome":
            self.wd = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == "ie":
            self.wd = webdriver.Ie(executable_path=IEDriverManager().install())
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.base_url = base_url
        self.project = ProjectHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
