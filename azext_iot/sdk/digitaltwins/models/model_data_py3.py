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


class ModelData(Model):
    """A model definition and metadata for that model.

    All required parameters must be populated in order to send to Azure.

    :param display_name: A language map that contains the localized display
     names as specified in the model definition.
    :type display_name: object
    :param description: A language map that contains the localized
     descriptions as specified in the model definition.
    :type description: object
    :param id: Required. The id of the model as specified in the model
     definition.
    :type id: str
    :param upload_time: The time the model was uploaded to the service.
    :type upload_time: datetime
    :param decommissioned: Indicates if the model is decommissioned.
     Decommissioned models cannot be referenced by newly created digital twins.
     Default value: False .
    :type decommissioned: bool
    :param model: The model definition.
    :type model: object
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'object'},
        'description': {'key': 'description', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'upload_time': {'key': 'uploadTime', 'type': 'iso-8601'},
        'decommissioned': {'key': 'decommissioned', 'type': 'bool'},
        'model': {'key': 'model', 'type': 'object'},
    }

    def __init__(self, *, id: str, display_name=None, description=None, upload_time=None, decommissioned: bool=False, model=None, **kwargs) -> None:
        super(ModelData, self).__init__(**kwargs)
        self.display_name = display_name
        self.description = description
        self.id = id
        self.upload_time = upload_time
        self.decommissioned = decommissioned
        self.model = model
