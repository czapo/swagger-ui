# from projects.operations import NPMOperations
from projects import operations


class Project(operations.NPMOperations):

    def get_project_name(self):
        return 'swaggerui'