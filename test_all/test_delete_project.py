import time
import random
from model.project import Project


def test_delete_project(app):
    time.sleep(1)
    app.session.login("administrator", "root")
    app.project.open_manage_project_page()
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    time.sleep(1)
    app.project.select_project(project)
    time.sleep(1)
    app.project.delete_project()
