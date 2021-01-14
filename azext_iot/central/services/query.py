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

BASE_PATH = "api/preview/query"


def query(
    cmd,
    app_id: str,
    token: str,
    query_string: str,
    central_dns_suffix=CENTRAL_ENDPOINT,
):
    """
    run query api

    Args:
        cmd: command passed into az
        app_id: name of app (used for forming request URL)
        token: (OPTIONAL) authorization token to fetch device details from IoTC.
            MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...')
        token_id:Unique ID for the API token.
        central_dns_suffix: {centralDnsSuffixInPath} as found in docs

    Returns:
       result (currently a 201)
    """
    url = "https://{}.{}/{}".format(app_id, central_dns_suffix, BASE_PATH)

    payload = {"query": query_string}

    headers = _utility.get_headers(token, cmd, has_json_payload=True)

    response = requests.get(url, headers=headers, json=payload)
    return _utility.try_extract_result(response)
