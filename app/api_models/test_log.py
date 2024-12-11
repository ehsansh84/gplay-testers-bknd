from datetime import datetime
from typing import List
from pydantic import BaseModel, Field

module_name = 'test_log'


class Base(BaseModel):
    f"""
    Use this model for base fields of a {module_name}
    """
    imei: str = Field(description="imei", example="imei")
    app_name: str = Field(description="app_name", example="app_name")
    app_version: str = Field(description="app_version", example="app_version")
    os_type: str = Field(description="os_type", example="os_type")
    os_version: str = Field(description="os_version", example="os_version")


class Write(Base):
    f"""
    Use this model to create a {module_name}
    """
    pass


class Read(Base):
    f"""
    Use this model to read a {module_name}
    """
    id: str = Field(description="id", readOnly=True)
    created_at: datetime = Field(readOnly=True)
    updated_at: datetime = Field(readOnly=True)


class Update(Base):
    f"""
    Use this model to update a {module_name}
    """
    pass


ListRead = List[Read]
