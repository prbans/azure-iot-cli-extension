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


class D2CTest(Model):
    """D2CTest.

    :param expected_message:
    :type expected_message: str
    :param expected_message_count:
    :type expected_message_count: int
    :param validation_timeout:
    :type validation_timeout: int
    :param is_mandatory:
    :type is_mandatory: bool
    :param should_validate:
    :type should_validate: bool
    """

    _attribute_map = {
        'expected_message': {'key': 'expectedMessage', 'type': 'str'},
        'expected_message_count': {'key': 'expectedMessageCount', 'type': 'int'},
        'validation_timeout': {'key': 'validationTimeout', 'type': 'int'},
        'is_mandatory': {'key': 'isMandatory', 'type': 'bool'},
        'should_validate': {'key': 'shouldValidate', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(D2CTest, self).__init__(**kwargs)
        self.expected_message = kwargs.get('expected_message', None)
        self.expected_message_count = kwargs.get('expected_message_count', None)
        self.validation_timeout = kwargs.get('validation_timeout', None)
        self.is_mandatory = kwargs.get('is_mandatory', None)
        self.should_validate = kwargs.get('should_validate', None)
