from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def open_manage_project_page(self):
        wd = self.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def select_project(self, project):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_link_text(project.name[0]).click()

    def delete_project(self):
        wd = self.wd
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

    def create_project(self):
        wd = self.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form()
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def fill_project_form(self):
        wd = self.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("New_project")
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text("stable")
        wd.find_element_by_xpath("//option[@value='50']").click()
        wd.find_element_by_name("inherit_global").click()
        wd.find_element_by_name("inherit_global").click()
        wd.find_element_by_name("view_state").click()
        Select(wd.find_element_by_name("view_state")).select_by_visible_text("private")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='View Status'])[1]/following::option[2]").click()
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys("desc")

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_project_page()
            self.project_cache = []
            for row in wd.find_elements_by_xpath(
                    "//table[3]/tbody/tr[contains(@class,'row-1') or contains(@class,'row-2')]"):
                cells = row.find_elements_by_tag_name("td")
                name = cells[0].text
                description = cells[4].text
                self.project_cache.append(
                    Project(name=name, description=description))
        return list(self.project_cache)
