from models import NameSpace


class Project(object):

    def __init__(self, name: str,
                 ssh_url_to_repo: str,
                 path_with_namespace: str,
                 namespace: NameSpace) -> None:
        self._namespace = namespace
        self._name = name
        self._ssh_url_to_repo = ssh_url_to_repo
        self._path_with_namespace = path_with_namespace

    @property
    def name(self) -> str:
        return self._name

    @property
    def ssh_url_to_repo(self) -> str:
        return self._ssh_url_to_repo

    @property
    def path_with_namespace(self) -> str:
        return self._path_with_namespace

    @property
    def namespace(self) -> NameSpace:
        return self._namespace
