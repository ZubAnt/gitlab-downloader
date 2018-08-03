import gitlab
import logging

from gitlab.v4.objects import GitlabAuthenticationError, GitlabListError, Project as GitlabProject
from typing import List

from converters import ProjectConverter
from data_contexts import GitlabContext
from models import Project


class GitlabService(object):

    def __init__(self, context: GitlabContext) -> None:
        self._context = context
        self._gl = gitlab.Gitlab(url=context.base_url, private_token=context.private_token, api_version=context.api_version)

    def get_projects(self) -> List[Project]:
        try:
            logging.info('getting projects...')
            gitlab_projects = self._gl.projects.list(all=True)
            return self._convert_many(gitlab_projects)
        except GitlabAuthenticationError:
            pass
        except GitlabListError:
            pass

    @classmethod
    def _convert_many(cls, items: List[GitlabProject]) -> List[Project]:
        return [ProjectConverter.load(item.attributes) for item in items]

