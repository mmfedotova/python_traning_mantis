import time


def test_create_project(app):
    time.sleep(1)
    app.session.login("administrator", "root")
    app.project.open_manage_project_page()
    app.project.create_project()
