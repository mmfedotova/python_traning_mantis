from suds import WebFault
from suds.client import Client

from model.project import Project


class SoapHelper:
    def __init__(self, app):
        self.app = app
        self.client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")

    def get_project_list(self):
        username = self.app.admin_config["username"]
        password = self.app.admin_config["password"]
        try:
            projects = self.client.service.mc_projects_get_user_accessible(username, password)
            project_list = []
            for item in projects:
                project_list.append(
                    Project(name=item.name, description=item.description))
            return project_list
        except WebFault:
            return None
