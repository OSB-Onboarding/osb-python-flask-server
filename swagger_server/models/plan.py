# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.maintenance_info import MaintenanceInfo
from swagger_server.models.metadata import Metadata
from swagger_server.models.schemas_object import SchemasObject
from swagger_server import util


class Plan(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, description: str=None, metadata: Metadata=None, free: bool=True, bindable: bool=None, plan_updateable: bool=None, schemas: SchemasObject=None, maximum_polling_duration: int=None, maintenance_info: MaintenanceInfo=None, binding_rotatable: bool=False):  # noqa: E501
        """Plan - a model defined in Swagger

        :param id: The id of this Plan.  # noqa: E501
        :type id: str
        :param name: The name of this Plan.  # noqa: E501
        :type name: str
        :param description: The description of this Plan.  # noqa: E501
        :type description: str
        :param metadata: The metadata of this Plan.  # noqa: E501
        :type metadata: Metadata
        :param free: The free of this Plan.  # noqa: E501
        :type free: bool
        :param bindable: The bindable of this Plan.  # noqa: E501
        :type bindable: bool
        :param plan_updateable: The plan_updateable of this Plan.  # noqa: E501
        :type plan_updateable: bool
        :param schemas: The schemas of this Plan.  # noqa: E501
        :type schemas: SchemasObject
        :param maximum_polling_duration: The maximum_polling_duration of this Plan.  # noqa: E501
        :type maximum_polling_duration: int
        :param maintenance_info: The maintenance_info of this Plan.  # noqa: E501
        :type maintenance_info: MaintenanceInfo
        :param binding_rotatable: The binding_rotatable of this Plan.  # noqa: E501
        :type binding_rotatable: bool
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'description': str,
            'metadata': Metadata,
            'free': bool,
            'bindable': bool,
            'plan_updateable': bool,
            'schemas': SchemasObject,
            'maximum_polling_duration': int,
            'maintenance_info': MaintenanceInfo,
            'binding_rotatable': bool
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'metadata': 'metadata',
            'free': 'free',
            'bindable': 'bindable',
            'plan_updateable': 'plan_updateable',
            'schemas': 'schemas',
            'maximum_polling_duration': 'maximum_polling_duration',
            'maintenance_info': 'maintenance_info',
            'binding_rotatable': 'binding_rotatable'
        }

        self._id = id
        self._name = name
        self._description = description
        self._metadata = metadata
        self._free = free
        self._bindable = bindable
        self._plan_updateable = plan_updateable
        self._schemas = schemas
        self._maximum_polling_duration = maximum_polling_duration
        self._maintenance_info = maintenance_info
        self._binding_rotatable = binding_rotatable

    @classmethod
    def from_dict(cls, dikt) -> 'Plan':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Plan of this Plan.  # noqa: E501
        :rtype: Plan
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Plan.


        :return: The id of this Plan.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Plan.


        :param id: The id of this Plan.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Plan.


        :return: The name of this Plan.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Plan.


        :param name: The name of this Plan.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this Plan.


        :return: The description of this Plan.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Plan.


        :param description: The description of this Plan.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this Plan.


        :return: The metadata of this Plan.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this Plan.


        :param metadata: The metadata of this Plan.
        :type metadata: Metadata
        """

        self._metadata = metadata

    @property
    def free(self) -> bool:
        """Gets the free of this Plan.


        :return: The free of this Plan.
        :rtype: bool
        """
        return self._free

    @free.setter
    def free(self, free: bool):
        """Sets the free of this Plan.


        :param free: The free of this Plan.
        :type free: bool
        """

        self._free = free

    @property
    def bindable(self) -> bool:
        """Gets the bindable of this Plan.


        :return: The bindable of this Plan.
        :rtype: bool
        """
        return self._bindable

    @bindable.setter
    def bindable(self, bindable: bool):
        """Sets the bindable of this Plan.


        :param bindable: The bindable of this Plan.
        :type bindable: bool
        """

        self._bindable = bindable

    @property
    def plan_updateable(self) -> bool:
        """Gets the plan_updateable of this Plan.


        :return: The plan_updateable of this Plan.
        :rtype: bool
        """
        return self._plan_updateable

    @plan_updateable.setter
    def plan_updateable(self, plan_updateable: bool):
        """Sets the plan_updateable of this Plan.


        :param plan_updateable: The plan_updateable of this Plan.
        :type plan_updateable: bool
        """

        self._plan_updateable = plan_updateable

    @property
    def schemas(self) -> SchemasObject:
        """Gets the schemas of this Plan.


        :return: The schemas of this Plan.
        :rtype: SchemasObject
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas: SchemasObject):
        """Sets the schemas of this Plan.


        :param schemas: The schemas of this Plan.
        :type schemas: SchemasObject
        """

        self._schemas = schemas

    @property
    def maximum_polling_duration(self) -> int:
        """Gets the maximum_polling_duration of this Plan.


        :return: The maximum_polling_duration of this Plan.
        :rtype: int
        """
        return self._maximum_polling_duration

    @maximum_polling_duration.setter
    def maximum_polling_duration(self, maximum_polling_duration: int):
        """Sets the maximum_polling_duration of this Plan.


        :param maximum_polling_duration: The maximum_polling_duration of this Plan.
        :type maximum_polling_duration: int
        """

        self._maximum_polling_duration = maximum_polling_duration

    @property
    def maintenance_info(self) -> MaintenanceInfo:
        """Gets the maintenance_info of this Plan.


        :return: The maintenance_info of this Plan.
        :rtype: MaintenanceInfo
        """
        return self._maintenance_info

    @maintenance_info.setter
    def maintenance_info(self, maintenance_info: MaintenanceInfo):
        """Sets the maintenance_info of this Plan.


        :param maintenance_info: The maintenance_info of this Plan.
        :type maintenance_info: MaintenanceInfo
        """

        self._maintenance_info = maintenance_info

    @property
    def binding_rotatable(self) -> bool:
        """Gets the binding_rotatable of this Plan.


        :return: The binding_rotatable of this Plan.
        :rtype: bool
        """
        return self._binding_rotatable

    @binding_rotatable.setter
    def binding_rotatable(self, binding_rotatable: bool):
        """Sets the binding_rotatable of this Plan.


        :param binding_rotatable: The binding_rotatable of this Plan.
        :type binding_rotatable: bool
        """

        self._binding_rotatable = binding_rotatable
