# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from knack.log import get_logger
from typing import List
from azext_iot.central import services as central_services
from azext_iot.central.models.enum import DeviceStatus
from azext_iot.central.models.device import Device
from azext_iot.dps.services import global_service as dps_global_service

logger = get_logger(__name__)


class CentralDeviceProvider:
    def __init__(self, cmd, app_id: str, token=None):
        """
        Provider for device APIs

        Args:
            cmd: command passed into az
            app_id: name of app (used for forming request URL)
            token: (OPTIONAL) authorization token to fetch device details from IoTC.
                MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...')
                Useful in scenarios where user doesn't own the app
                therefore AAD token won't work, but a SAS token generated by owner will
        """
        self._cmd = cmd
        self._app_id = app_id
        self._token = token
        self._devices = {}
        self._device_templates = {}
        self._device_credentials = {}
        self._device_registration_info = {}

    def get_device_essential_info(
        self, device_id, central_dns_suffix="azureiotcentral.com",
    ) -> Device:
        device = self.get_device(device_id, central_dns_suffix)
        registration_info = device.get_device_registration_info()

        return registration_info

    def get_device(
        self, device_id, central_dns_suffix="azureiotcentral.com",
    ) -> Device:
        if not device_id:
            raise CLIError("Device id must be specified.")
        # get or add to cache
        device = self._devices.get(device_id)

        if not device:
            device = central_services.device.get_device(
                cmd=self._cmd,
                app_id=self._app_id,
                device_id=device_id,
                token=self._token,
                central_dns_suffix=central_dns_suffix,
            )
            self._devices[device_id] = device

        if not device:
            raise CLIError("No device found with id: '{}'.".format(device_id))

        return device

    def get_device_template_by_device_id(
        self, device_id, central_dns_suffix="azureiotcentral.com",
    ):
        from azext_iot.central.providers import CentralDeviceTemplateProvider

        if not device_id:
            raise CLIError("Device id must be specified.")

        device = self.get_device(device_id, central_dns_suffix)
        if not device.instance_of:
            raise CLIError(
                "Device '{}' does not have a corresponding device template.".format(
                    device_id
                )
            )

        template = CentralDeviceTemplateProvider.get_device_template(
            self=self,
            device_template_id=device.instance_of,
            central_dns_suffix=central_dns_suffix,
        )
        return template

    def list_devices(self, central_dns_suffix="azureiotcentral.com") -> List[Device]:
        devices = central_services.device.list_devices(
            cmd=self._cmd, app_id=self._app_id, token=self._token
        )

        # add to cache
        self._devices.update({device.id: device for device in devices})

        return self._devices

    def create_device(
        self,
        device_id,
        device_name=None,
        instance_of=None,
        simulated=False,
        central_dns_suffix="azureiotcentral.com",
    ) -> Device:
        if not device_id:
            raise CLIError("Device id must be specified.")

        if device_id in self._devices:
            raise CLIError("Device already exists")

        device = central_services.device.create_device(
            cmd=self._cmd,
            app_id=self._app_id,
            device_id=device_id,
            device_name=device_name,
            instance_of=instance_of,
            simulated=simulated,
            token=self._token,
            central_dns_suffix=central_dns_suffix,
        )

        if not device:
            raise CLIError("No device found with id: '{}'.".format(device_id))

        # add to cache
        self._devices[device.id] = device

        return device

    def delete_device(
        self, device_id, central_dns_suffix="azureiotcentral.com",
    ) -> dict:
        if not device_id:
            raise CLIError("Device id must be specified.")

        # get or add to cache
        result = central_services.device.delete_device(
            cmd=self._cmd,
            app_id=self._app_id,
            device_id=device_id,
            token=self._token,
            central_dns_suffix=central_dns_suffix,
        )

        # remove from cache
        # pop "miss" raises a KeyError if None is not provided
        self._devices.pop(device_id, None)
        self._device_credentials.pop(device_id, None)

        return result

    def get_device_credentials(
        self, device_id, central_dns_suffix="azureiotcentral.com",
    ) -> dict:
        credentials = self._device_credentials.get(device_id)

        if not credentials:
            credentials = central_services.device.get_device_credentials(
                cmd=self._cmd,
                app_id=self._app_id,
                device_id=device_id,
                token=self._token,
            )

        if not credentials:
            raise CLIError(
                "Could not find device credentials for device '{}'".format(device_id)
            )

        # add to cache
        self._device_credentials[device_id] = credentials

        return credentials

    def get_device_registration_info(
        self,
        device_id,
        device_status: DeviceStatus,
        central_dns_suffix="azureiotcentral.com",
    ) -> dict:
        dps_state = {}
        info = self._device_registration_info.get(device_id)

        if info:
            return info

        device_essential_info = self.get_device_essential_info(device_id)

        if (
            DeviceStatus(device_essential_info.get("device_status"))
            == DeviceStatus.provisioned
        ):
            credentials = self.get_device_credentials(
                device_id=device_id, central_dns_suffix=central_dns_suffix
            )
            id_scope = credentials["idScope"]
            key = credentials["symmetricKey"]["primaryKey"]
            dps_state = dps_global_service.get_registration_state(
                id_scope=id_scope, key=key, device_id=device_id
            )
        dps_state = self.dps_populate_essential_info(
            dps_state, device_essential_info.get("device_status")
        )
        info = {
            "@device_id": device_id,
            "dps_state": dps_state,
            "device_info": device_essential_info,
        }

        self._device_registration_info[device_id] = info

        return info

    def dps_populate_essential_info(self, dps_info, device_status):
        error = {
            "provisioned": "None",
            "registered": "Device it not yet provisioned.",
            "blocked": "Device is blocked by admin",
            "unassociated": "Device does not have a valid template associated with it",
        }

        filtered_dps_info = {
            "status": dps_info.get("status"),
            "error": error.get(device_status),
        }
        return filtered_dps_info

    def get_all_registration_info(
        self, device_status, central_dns_suffix="azureiotcentral.com"
    ):

        logger.warning("This command may take a long time to complete execution.")
        devices = self.list_devices(central_dns_suffix=central_dns_suffix)

        real_devices = [device for device in devices.values() if not device.simulated]

        filtered_devices = real_devices

        if device_status:
            filtered_devices = [
                device
                for device in real_devices
                if device.device_status == DeviceStatus(device_status)
            ]

        if len(devices) != len(filtered_devices):
            logger.warning(
                "Getting registration info for real devices. "
                "{}".format([device.id for device in filtered_devices])
            )

        result = [
            self.get_device_registration_info(device.id, device.device_status)
            for device in filtered_devices
        ]

        return result
