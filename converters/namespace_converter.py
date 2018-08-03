from typing import Dict, Any

from models import NameSpace


class NameSpaceConverter(object):

    @staticmethod
    def load(data: Dict[str, Any]) -> NameSpace:
        uid = int(data['id'])
        name = data['name']
        path = data['path']
        kind = data['kind']
        full_path = data['full_path']
        parent_id = None if data.get('parent_id') in (None, 'null') else int(data['parent_id'])
        return NameSpace(uid=uid, name=name, path=path, kind=kind, full_path=full_path, parent_id=parent_id)
