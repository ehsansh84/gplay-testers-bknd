from typing import List
from app.core.base_db import DB

module_name = 'test_log'
module_text = 'TestLog'


class TestLog(DB):
    f"""
    Use this model to manage a {module_text}
    """

    def __init__(self, _id=None, module_name=module_name, module_text=module_text, db=None,
                 imei='', app_name='', app_version='', os_type='', os_version=''):
        self._id: str = _id
        self.imei: str = imei
        self.app_name: str = app_name
        self.app_version: str = app_version
        self.os_type: str = os_type
        self.os_version: str = os_version

        super().__init__(_id=_id, module_name=module_name, module_text=module_text, db=db)

    def list(self, query=None) -> List['TestLog']:
        return super().list(query=query)
