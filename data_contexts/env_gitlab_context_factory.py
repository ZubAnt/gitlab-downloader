import os

from .gitlab_context import GitlabContext


class EnvGitlabContextFactory(object):

    @staticmethod
    def create() -> GitlabContext:
        env = os.environ
        base_url = env['GITLAB_BASE_URL']
        private_token = env['GITLAB_PRIVATE_TOKEN']
        return GitlabContext(base_url=base_url, private_token=private_token)
