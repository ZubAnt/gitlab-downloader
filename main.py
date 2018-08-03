import logging

from data_contexts import EnvGitlabContextFactory
from services import CloneService, GitlabService

logging.getLogger().setLevel(logging.INFO)


context = EnvGitlabContextFactory.create()
gitlab_service = GitlabService(context)
clone_service = CloneService(context)

projects = gitlab_service.get_projects()
clone_service.clone_many(projects)
