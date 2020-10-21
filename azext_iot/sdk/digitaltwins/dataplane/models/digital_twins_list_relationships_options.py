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


class DigitalTwinsListRelationshipsOptions(Model):
    """Additional parameters for list_relationships operation.

    :param traceparent: Identifies the request in a distributed tracing
     system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification
     information and is a companion to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': '', 'type': 'str'},
        'tracestate': {'key': '', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DigitalTwinsListRelationshipsOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)
