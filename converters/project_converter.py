from typing import Dict, Any

from .namespace_converter import NameSpaceConverter

from models import Project


class ProjectConverter(object):

    @staticmethod
    def load(data: Dict[str, Any]) -> Project:
        name = data['name']
        ssh_url_to_repo = data['ssh_url_to_repo']
        path_with_namespace = data['path_with_namespace']
        namespace = NameSpaceConverter.load(data['namespace'])
        return Project(name=name,
                       ssh_url_to_repo=ssh_url_to_repo,
                       path_with_namespace=path_with_namespace,
                       namespace=namespace)
