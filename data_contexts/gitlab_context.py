class GitlabContext(object):

    def __init__(self, base_url: str, private_token: str, api_version: str = None) -> None:
        self._base_url = base_url
        self._private_token = private_token
        self._api_version = '4' if not api_version else api_version

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def private_token(self) -> str:
        return self._private_token

    @property
    def api_version(self) -> str:
        return self._api_version
