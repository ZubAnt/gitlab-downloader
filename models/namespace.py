from typing import Optional


class NameSpace(object):

    def __init__(self, uid: int, name: str, path: str, kind: str, full_path: str, parent_id: Optional[int]) -> None:
        self._uid = uid
        self._name = name
        self._path = path
        self._kind = kind
        self._full_path = full_path
        self._parent_id = parent_id

    @property
    def uid(self) -> int:
        return self._uid

    @property
    def name(self) -> str:
        return self._name

    @property
    def path(self) -> str:
        return self._path

    @property
    def kind(self) -> str:
        return self._kind

    @property
    def full_path(self) -> str:
        return self._full_path

    @property
    def parent_id(self) -> Optional[int]:
        return self._parent_id
