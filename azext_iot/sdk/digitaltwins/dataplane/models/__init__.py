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

try:
    from .event_route_py3 import EventRoute
    from .digital_twins_model_data_py3 import DigitalTwinsModelData
    from .incoming_relationship_py3 import IncomingRelationship
    from .query_specification_py3 import QuerySpecification
    from .query_result_py3 import QueryResult
    from .inner_error_py3 import InnerError
    from .error_py3 import Error
    from .error_response_py3 import ErrorResponse, ErrorResponseException
    from .digital_twin_models_add_options_py3 import DigitalTwinModelsAddOptions
    from .digital_twin_models_list_options_py3 import DigitalTwinModelsListOptions
    from .digital_twin_models_get_by_id_options_py3 import DigitalTwinModelsGetByIdOptions
    from .digital_twin_models_update_options_py3 import DigitalTwinModelsUpdateOptions
    from .digital_twin_models_delete_options_py3 import DigitalTwinModelsDeleteOptions
    from .query_query_twins_options_py3 import QueryQueryTwinsOptions
    from .digital_twins_get_by_id_options_py3 import DigitalTwinsGetByIdOptions
    from .digital_twins_add_options_py3 import DigitalTwinsAddOptions
    from .digital_twins_delete_options_py3 import DigitalTwinsDeleteOptions
    from .digital_twins_update_options_py3 import DigitalTwinsUpdateOptions
    from .digital_twins_get_relationship_by_id_options_py3 import DigitalTwinsGetRelationshipByIdOptions
    from .digital_twins_add_relationship_options_py3 import DigitalTwinsAddRelationshipOptions
    from .digital_twins_delete_relationship_options_py3 import DigitalTwinsDeleteRelationshipOptions
    from .digital_twins_update_relationship_options_py3 import DigitalTwinsUpdateRelationshipOptions
    from .digital_twins_list_relationships_options_py3 import DigitalTwinsListRelationshipsOptions
    from .digital_twins_list_incoming_relationships_options_py3 import DigitalTwinsListIncomingRelationshipsOptions
    from .digital_twins_send_telemetry_options_py3 import DigitalTwinsSendTelemetryOptions
    from .digital_twins_send_component_telemetry_options_py3 import DigitalTwinsSendComponentTelemetryOptions
    from .digital_twins_get_component_options_py3 import DigitalTwinsGetComponentOptions
    from .digital_twins_update_component_options_py3 import DigitalTwinsUpdateComponentOptions
    from .event_routes_list_options_py3 import EventRoutesListOptions
    from .event_routes_get_by_id_options_py3 import EventRoutesGetByIdOptions
    from .event_routes_add_options_py3 import EventRoutesAddOptions
    from .event_routes_delete_options_py3 import EventRoutesDeleteOptions
except (SyntaxError, ImportError):
    from .event_route import EventRoute
    from .digital_twins_model_data import DigitalTwinsModelData
    from .incoming_relationship import IncomingRelationship
    from .query_specification import QuerySpecification
    from .query_result import QueryResult
    from .inner_error import InnerError
    from .error import Error
    from .error_response import ErrorResponse, ErrorResponseException
    from .digital_twin_models_add_options import DigitalTwinModelsAddOptions
    from .digital_twin_models_list_options import DigitalTwinModelsListOptions
    from .digital_twin_models_get_by_id_options import DigitalTwinModelsGetByIdOptions
    from .digital_twin_models_update_options import DigitalTwinModelsUpdateOptions
    from .digital_twin_models_delete_options import DigitalTwinModelsDeleteOptions
    from .query_query_twins_options import QueryQueryTwinsOptions
    from .digital_twins_get_by_id_options import DigitalTwinsGetByIdOptions
    from .digital_twins_add_options import DigitalTwinsAddOptions
    from .digital_twins_delete_options import DigitalTwinsDeleteOptions
    from .digital_twins_update_options import DigitalTwinsUpdateOptions
    from .digital_twins_get_relationship_by_id_options import DigitalTwinsGetRelationshipByIdOptions
    from .digital_twins_add_relationship_options import DigitalTwinsAddRelationshipOptions
    from .digital_twins_delete_relationship_options import DigitalTwinsDeleteRelationshipOptions
    from .digital_twins_update_relationship_options import DigitalTwinsUpdateRelationshipOptions
    from .digital_twins_list_relationships_options import DigitalTwinsListRelationshipsOptions
    from .digital_twins_list_incoming_relationships_options import DigitalTwinsListIncomingRelationshipsOptions
    from .digital_twins_send_telemetry_options import DigitalTwinsSendTelemetryOptions
    from .digital_twins_send_component_telemetry_options import DigitalTwinsSendComponentTelemetryOptions
    from .digital_twins_get_component_options import DigitalTwinsGetComponentOptions
    from .digital_twins_update_component_options import DigitalTwinsUpdateComponentOptions
    from .event_routes_list_options import EventRoutesListOptions
    from .event_routes_get_by_id_options import EventRoutesGetByIdOptions
    from .event_routes_add_options import EventRoutesAddOptions
    from .event_routes_delete_options import EventRoutesDeleteOptions
from .digital_twins_model_data_paged import DigitalTwinsModelDataPaged
from .object_paged import ObjectPaged
from .incoming_relationship_paged import IncomingRelationshipPaged
from .event_route_paged import EventRoutePaged

__all__ = [
    'EventRoute',
    'DigitalTwinsModelData',
    'IncomingRelationship',
    'QuerySpecification',
    'QueryResult',
    'InnerError',
    'Error',
    'ErrorResponse', 'ErrorResponseException',
    'DigitalTwinModelsAddOptions',
    'DigitalTwinModelsListOptions',
    'DigitalTwinModelsGetByIdOptions',
    'DigitalTwinModelsUpdateOptions',
    'DigitalTwinModelsDeleteOptions',
    'QueryQueryTwinsOptions',
    'DigitalTwinsGetByIdOptions',
    'DigitalTwinsAddOptions',
    'DigitalTwinsDeleteOptions',
    'DigitalTwinsUpdateOptions',
    'DigitalTwinsGetRelationshipByIdOptions',
    'DigitalTwinsAddRelationshipOptions',
    'DigitalTwinsDeleteRelationshipOptions',
    'DigitalTwinsUpdateRelationshipOptions',
    'DigitalTwinsListRelationshipsOptions',
    'DigitalTwinsListIncomingRelationshipsOptions',
    'DigitalTwinsSendTelemetryOptions',
    'DigitalTwinsSendComponentTelemetryOptions',
    'DigitalTwinsGetComponentOptions',
    'DigitalTwinsUpdateComponentOptions',
    'EventRoutesListOptions',
    'EventRoutesGetByIdOptions',
    'EventRoutesAddOptions',
    'EventRoutesDeleteOptions',
    'DigitalTwinsModelDataPaged',
    'ObjectPaged',
    'IncomingRelationshipPaged',
    'EventRoutePaged',
]
