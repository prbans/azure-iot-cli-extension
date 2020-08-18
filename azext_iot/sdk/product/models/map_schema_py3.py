# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MapSchema(Model):
    """MapSchema.

    :param key_schema:
    :type key_schema: ~product.models.SchemaField
    :param value_schema:
    :type value_schema: ~product.models.SchemaField
    :param schema_type: Possible values include: 'Unknown', 'Boolean', 'Date',
     'DateTime', 'Double', 'Duration', 'Float', 'Integer', 'Long', 'String',
     'Time', 'Enum', 'Object', 'Map', 'Array'
    :type schema_type: str or ~product.models.enum
    :param name:
    :type name: str
    :param comment:
    :type comment: str
    :param display_name:
    :type display_name: dict[str, str]
    :param id:
    :type id: str
    :param description:
    :type description: dict[str, str]
    :param language_version:
    :type language_version: int
    """

    _attribute_map = {
        'key_schema': {'key': 'keySchema', 'type': 'SchemaField'},
        'value_schema': {'key': 'valueSchema', 'type': 'SchemaField'},
        'schema_type': {'key': 'schemaType', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': '{str}'},
        'id': {'key': 'id', 'type': 'str'},
        'description': {'key': 'description', 'type': '{str}'},
        'language_version': {'key': 'languageVersion', 'type': 'int'},
    }

    def __init__(self, *, key_schema=None, value_schema=None, schema_type=None, name: str=None, comment: str=None, display_name=None, id: str=None, description=None, language_version: int=None, **kwargs) -> None:
        super(MapSchema, self).__init__(**kwargs)
        self.key_schema = key_schema
        self.value_schema = value_schema
        self.schema_type = schema_type
        self.name = name
        self.comment = comment
        self.display_name = display_name
        self.id = id
        self.description = description
        self.language_version = language_version
