# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# This is largely derived from https://docs.microsoft.com/en-us/rest/api/iotcentral/devicetemplates

import requests

from knack.util import CLIError
from . import _utility as utility


def get_device_template(
    cmd,
    device_template_urn: str,
    app_id: str,
    token: str,
    central_dns_suffix="azureiotcentral.com",
) -> dict:
    """
    Get device template given a device id

    Args:
        cmd: command passed into az
        device_template_urn: case sensitive device template urn,
        app_id: name of app (used for forming request URL)
        token: (OPTIONAL) authorization token to fetch device details from IoTC.
            MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...')
        central_dns_suffix: {centralDnsSuffixInPath} as found in docs

    Returns:
        device: dict
    """
    url = "https://{}.{}/api/preview/deviceTemplates/{}".format(
        app_id, central_dns_suffix, device_template_urn
    )
    headers = utility.get_headers(token, cmd)

    response = requests.get(url, headers=headers)

    body = response.json()

    if "error" in body:
        raise CLIError(body["error"])

    return body
