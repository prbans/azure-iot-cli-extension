# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger

from azext_iot.constants import CENTRAL_ENDPOINT
from azext_iot.central import services as central_services


logger = get_logger(__name__)


class CentralContDataExportProvider:
    def __init__(self, cmd, app_id: str, token=None):
        """
        Provider for continuous data export

        Args:
            cmd: command passed into az
            app_id: name of app (used for forming request URL)
            token: (OPTIONAL) authorization token to fetch API token details from IoTC.
                MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...')
                Useful in scenarios where user doesn't own the app
                therefore AAD token won't work, but a SAS token generated by owner will
        """
        self._cmd = cmd
        self._app_id = app_id
        self._token = token

    def add_cde(
        self,
        export_id,
        display_name,
        enable,
        ep_type,
        ep_conn,
        entity_name,
        sources,
        central_dns_suffix=CENTRAL_ENDPOINT,
    ):

        return central_services.cde.add_cde(
            cmd=self._cmd,
            app_id=self._app_id,
            sources=sources,
            ep_type=ep_type,
            ep_conn=ep_conn,
            entity_name=entity_name,
            display_name=display_name,
            export_id=export_id,
            token=self._token,
            enable=enable,
            central_dns_suffix=central_dns_suffix,
        )

    def get_cde_list(
        self, central_dns_suffix=CENTRAL_ENDPOINT,
    ):

        return central_services.cde.get_cde_list(
            cmd=self._cmd,
            app_id=self._app_id,
            token=self._token,
            central_dns_suffix=central_dns_suffix,
        )

    def get_cde(
        self, export_id, central_dns_suffix=CENTRAL_ENDPOINT,
    ):
        return central_services.cde.get_cde(
            cmd=self._cmd,
            app_id=self._app_id,
            export_id=export_id,
            token=self._token,
            central_dns_suffix=central_dns_suffix,
        )

    def delete_cde(
        self, export_id, central_dns_suffix=CENTRAL_ENDPOINT,
    ):
        return central_services.cde.delete_cde(
            cmd=self._cmd,
            app_id=self._app_id,
            export_id=export_id,
            token=self._token,
            central_dns_suffix=central_dns_suffix,
        )
