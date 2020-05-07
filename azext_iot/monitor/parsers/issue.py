# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from enum import IntEnum
from typing import List
from knack.log import get_logger

logger = get_logger(__name__)


class Severity(IntEnum):
    info = 1
    warning = 2
    error = 3


class Issue:
    def __init__(self, severity: Severity, details: str, message, device_id=""):
        self.severity = severity
        self.details = details
        self.device_id = device_id
        self.message = str(message)

        if not self.device_id:
            self.device_id = "Unknown"

    def log(self):
        to_log = "[{}] [DeviceId: {}] {}".format(
            self.severity.name.upper(), self.device_id, self.details
        )

        self._log(to_log)

    def _log(self, to_log: str):
        if self.severity == Severity.info:
            logger.info(to_log)

        if self.severity == Severity.warning:
            logger.warn(to_log)

        if self.severity == Severity.error:
            logger.error(to_log)

    def json_repr(self):
        json_repr = vars(self)
        json_repr["severity"] = self.severity.name
        return json_repr


class CentralIssue(Issue):
    def __init__(
        self, severity: Severity, details: str, message, device_id="", template_id=""
    ):
        super(CentralIssue, self).__init__(severity, details, message, device_id)
        self.template_id = template_id

        if not self.template_id:
            self.template_id = "Unknown"

    def log(self):
        to_log = "[{}] [DeviceId: {}] [TemplateId: {}] {}".format(
            self.severity.name.upper(), self.device_id, self.template_id, self.details
        )

        self._log(to_log)


class IssueHandler:
    def __init__(self):
        self._issues = []

    def add_issue(self, severity: Severity, details: str, message, device_id=""):
        issue = Issue(
            severity=severity, details=details, message=message, device_id=device_id
        )
        self._issues.append(issue)

    def add_central_issue(
        self, severity: Severity, details: str, message, device_id="", template_id=""
    ):
        issue = CentralIssue(
            severity=severity,
            details=details,
            message=message,
            device_id=device_id,
            template_id=template_id,
        )
        self._issues.append(issue)

    def get_all_issues(self) -> List[Issue]:
        return self._issues

    def get_issues_with_severity(self, severity: Severity) -> List[Issue]:
        """
        arguments:
            severity: Severity
        returns:
            all issues where severity equal specified severity

        example:
            issue_handler.get_issues_with_severity(Severity.info)
            returns all issues classified as "info"
        """
        return [issue for issue in self._issues if issue.severity == severity]

    def get_issues_with_minimum_severity(self, severity: Severity) -> List[Issue]:
        """
        arguments:
            severity: Severity
        returns:
            all issues where severity >= specified severity

        example:
            issue_handler.get_issues_with_minimum_severity(Severity.warning)
            returns all issues classified as "warning" and "error"
            "info" will not be included
        """
        return [issue for issue in self._issues if issue.severity >= severity]

    def get_issues_with_maximum_severity(self, severity: Severity) -> List[Issue]:
        """
        arguments:
            severity: Severity
        returns:
            all issues where severity <= specified severity

        example:
            issue_handler.get_issues_with_maximum_severity(Severity.warning)
            returns all issues classified as "warning" and "info"
            "error" will not be included
        """
        return [issue for issue in self._issues if issue.severity <= severity]


SUPPORTED_ENCODING = ["utf-8"]
SUPPORTED_FIELD_NAME_CHARS = ["a-z", "A-Z", "0-9", "_"]
SUPPORTED_CONTENT_TYPE = ["application/json"]
SUPPORTED_MESSAGE_HEADERS = []


class IssueMessageBuilder:
    @staticmethod
    def unknown_device_id():
        return "Device ID not found in message".format()

    @staticmethod
    def invalid_json():
        return "Invalid JSON format.".format()

    @staticmethod
    def invalid_encoding(encoding: str):
        return "Encoding type '{}' is not supported. Expected encoding '{}'.".format(
            encoding, SUPPORTED_ENCODING
        )

    @staticmethod
    def invalid_field_name(invalid_field_names: list):
        return (
            "Invalid characters detected. Invalid field names: '{}'. "
            "Allowed characters: {}."
        ).format(invalid_field_names, SUPPORTED_FIELD_NAME_CHARS)

    @staticmethod
    def invalid_pnp_property_not_value_wrapped():
        raise NotImplementedError()

    @staticmethod
    def invalid_non_pnp_field_name_duplicate():
        raise NotImplementedError()

    @staticmethod
    def invalid_content_type(content_type: str):
        return "Content type '{}' is not supported. Expected Content type: {}.".format(
            content_type, SUPPORTED_CONTENT_TYPE
        )

    @staticmethod
    def invalid_custom_headers():
        return (
            "Custom message headers are not supported in IoT Central. "
            "All the custom message headers will be dropped. "
            "Supported message headers: '{}'."
        ).format(SUPPORTED_MESSAGE_HEADERS)

    @staticmethod
    def invalid_field_name_mismatch_template(
        unmodeled_capabilities: list, modeled_capabilities: list
    ):
        return (
            "Device is sending data that has not been defined in the device template. "
            "Following capabilities have NOT been defined in the device template '{}'. "
            "Following capabilities have been defined in the device template '{}'. "
        ).format(unmodeled_capabilities, modeled_capabilities)

    @staticmethod
    def invalid_primitive_schema_mismatch_template(
        field_name: str, data_type: str, data
    ):
        return (
            "Datatype of field '{}' does not match the datatype '{}'. Data '{}'. "
            "All dates/times/datetimes/durations must be ISO 8601 compliant.".format(
                field_name, data_type, data,
            )
        )

    @staticmethod
    def invalid_interface_name_not_found():
        return "Interface name not found."

    @staticmethod
    def invalid_interface_name_mismatch(
        expected_interface_name: str, actual_interface_name: str
    ):
        return "Inteface name mismatch. Expected: {}, Actual: {}.".format(
            expected_interface_name, actual_interface_name
        )

    @staticmethod
    def invalid_system_properties():
        return "Failed to parse system properties.".format()

    @staticmethod
    def invalid_encoding_none_found():
        return "No encoding found.".format()

    @staticmethod
    def invalid_encoding_missing(system_properties: dict):
        return "Content type not found in system properties. System properties: {}.".format(
            system_properties
        )

    @staticmethod
    def invalid_annotations(message):
        return "Unable to decode message.annotations: {}.".format(message.annotations)

    @staticmethod
    def invalid_application_properties(message):
        return "Unable to decode message.application_properties: {}.".format(
            message.application_properties
        )

    @staticmethod
    def device_template_not_found(error: Exception):
        return "Error retrieving template '{}'".format(error)

    @staticmethod
    def invalid_template_extract_schema_failed(template: dict):
        return "Unable to extract device schema from template '{}'".format(template)
