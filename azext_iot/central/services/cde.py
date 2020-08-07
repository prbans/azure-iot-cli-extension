# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import requests

from knack.log import get_logger
from azext_iot.constants import CENTRAL_ENDPOINT
from azext_iot.central.services import _utility


logger = get_logger(__name__)

BASE_PATH = "api/preview/continuousDataExports"


def add_cde(
    cmd,
    app_id: str,
    token: str,
    sources: str,
    ep_type,
    ep_conn,
    export_id,
    name,
    enable,
    central_dns_suffix=CENTRAL_ENDPOINT,
):
    """
    Add an API token to a Central app

    Args:
        cmd: command passed into az
        app_id: name of app (used for forming request URL)        
        token: (OPTIONAL) authorization token to fetch device details from IoTC.
            MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...')
        central_dns_suffix: {centralDnsSuffixInPath} as found in docs
        sources: Data sources to export to the endpoint.
        ep_type: Type of endpoint where exported data should be sent.
        ep_conn: Connections string for the endpoint. 

    Returns:
    token: dict
    """
    ep = {
        "type": ep_type,
        "connectionString": ep_conn,
        "name": name,
    }
    # data = sources.split(",")
    url = "https://{}.{}/{}/{}".format(app_id, central_dns_suffix, BASE_PATH, export_id)

    payload = {
        "displayName": "Export to Storage 2",
        "endpoint": ep,
        "enabled": enable,
        "sources": sources,
    }
    headers = _utility.get_headers(token, cmd, has_json_payload=True)

    response = requests.put(url, headers=headers, json=payload)
    return _utility.try_extract_result(response)


def get_cde_list(
    cmd, app_id: str, token: str, central_dns_suffix=CENTRAL_ENDPOINT,
):
    """
    Get the list continuous data exports in an application

    Args:
        cmd: command passed into az
        app_id: name of app (used for forming request URL)
        token: (OPTIONAL) authorization token to fetch device details from IoTC.
            MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...')
        central_dns_suffix: {centralDnsSuffixInPath} as found in docs

    Returns:
        tokens: dict
    """
    url = "https://{}.{}/{}".format(app_id, central_dns_suffix, BASE_PATH)

    headers = _utility.get_headers(token, cmd)

    response = requests.get(url, headers=headers)
    return _utility.try_extract_result(response)


def get_cde(
    cmd, app_id: str, token: str, export_id: str, central_dns_suffix=CENTRAL_ENDPOINT,
):
    """
    Get information about a specified continuous data export

    Args:
        cmd: command passed into az
        app_id: name of app (used for forming request URL)
        token: (OPTIONAL) authorization token to fetch device details from IoTC.
            MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...')
        export_id: Unique ID for the continous data export
        central_dns_suffix: {centralDnsSuffixInPath} as found in docs

    Returns:
        token: dict
    """
    url = "https://{}.{}/{}/{}".format(app_id, central_dns_suffix, BASE_PATH, export_id)

    headers = _utility.get_headers(token, cmd)

    response = requests.get(url, headers=headers)
    return _utility.try_extract_result(response)


def delete_cde(
    cmd, app_id: str, token: str, export_id: str, central_dns_suffix=CENTRAL_ENDPOINT,
):
    """
    delete API token from the app.

    Args:
        cmd: command passed into az
        app_id: name of app (used for forming request URL)
        token: (OPTIONAL) authorization token to fetch device details from IoTC.
            MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...')
        export_id: Unique ID for the continous data export
        central_dns_suffix: {centralDnsSuffixInPath} as found in docs

    Returns:
       result (currently a 204)
    """
    url = "https://{}.{}/{}/{}".format(app_id, central_dns_suffix, BASE_PATH, export_id)

    headers = _utility.get_headers(token, cmd)

    response = requests.delete(url, headers=headers)
    return _utility.try_extract_result(response)