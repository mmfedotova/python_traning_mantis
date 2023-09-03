import time
import random
from model.project import Project
from operator import itemgetter


def test_delete_project(app):
    time.sleep(1)
    app.project.open_manage_project_page()
    if len(app.project.get_project_list()) == 0:
        app.project.create_project(Project(name="test", description="test"))
    old_projects = app.soap.get_project_list()
    project = random.choice(old_projects)
    time.sleep(1)
    app.project.select_project(project)
    time.sleep(1)
    app.project.delete_project()
    new_projects = app.soap.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    old_projects.sort()
    new_projects.sort()
    assert old_projects == new_projects
