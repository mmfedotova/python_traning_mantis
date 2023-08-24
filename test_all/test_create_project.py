import time
from operator import itemgetter

from model.project import Project


def test_create_project(app, json_project):
    time.sleep(1)
    project = json_project
    app.project.open_manage_project_page()
    old_projects = app.project.get_project_list()
    app.project.create_project(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    # assert sorted(old_projects, key=Project.get_name) == sorted(old_projects, key=Project.get_name)
    old_projects.sort()
    new_projects.sort()
    assert old_projects == new_projects
