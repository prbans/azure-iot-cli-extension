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


class TestCases(Model):
    """Test cases of a DigitTwin test.

    :param certification_badge_test_cases:
    :type certification_badge_test_cases: list[object]
    """

    _attribute_map = {
        'certification_badge_test_cases': {'key': 'certificationBadgeTestCases', 'type': '[object]'},
    }

    def __init__(self, *, certification_badge_test_cases=None, **kwargs) -> None:
        super(TestCases, self).__init__(**kwargs)
        self.certification_badge_test_cases = certification_badge_test_cases