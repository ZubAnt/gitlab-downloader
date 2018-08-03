import logging
import os
from typing import List

import git

from data_contexts import GitlabContext
from models import Project


class CloneService(object):

    BASE_CLONE_DIR = os.getcwd() if not os.environ.get('BASE_CLONE_DIR') else os.environ['BASE_CLONE_DIR']

    def __init__(self, context: GitlabContext) -> None:
        self._context = context

    def clone(self, project: Project) -> None:
        self._create_path(project)
        try:
            ok = self._filter(project)
            if not ok:
                logging.info(f'skip project: {project.path_with_namespace}')
                return
            logging.info(f"cloning {project.name}...")
            working_dir = f"{self.BASE_CLONE_DIR}/{project.namespace.full_path}"
            git.Git(working_dir=working_dir).clone(project.ssh_url_to_repo)

        except Exception as e:
            print(f"Error on {e}")

    def clone_many(self, projects: List[Project]) -> None:
        for project in projects:
            self.clone(project)

    def _create_path(self, project: Project) -> None:
        path = f"{self.BASE_CLONE_DIR}/{project.namespace.full_path}"
        if not os.path.exists(path):
            os.makedirs(path)

    @classmethod
    def _filter(cls, project: Project) -> bool:
        if 'open-source' in project.namespace.full_path:
            return False

        return True
