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
from msrest.exceptions import HttpOperationError


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ErrorDetail(Model):
    """Error details.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. The error's code.
    :type code: str
    :param message: Required. A human readable error message.
    :type message: str
    :param target: Indicates which property in the request is responsible for
     the error.
    :type target: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, *, code: str, message: str, target: str=None, **kwargs) -> None:
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target


class ErrorInfo(Model):
    """The code and message for an error.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. A machine readable error code.
    :type code: str
    :param message: Required. A human readable error message.
    :type message: str
    :param details: error details.
    :type details: list[~azure.mgmt.databricks.models.ErrorDetail]
    :param innererror: Inner error details if they exist.
    :type innererror: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'innererror': {'key': 'innererror', 'type': 'str'},
    }

    def __init__(self, *, code: str, message: str, details=None, innererror: str=None, **kwargs) -> None:
        super(ErrorInfo, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.details = details
        self.innererror = innererror


class ErrorResponse(Model):
    """Error response.

    Contains details when the response code indicates an error.

    All required parameters must be populated in order to send to Azure.

    :param error: Required. The error details.
    :type error: ~azure.mgmt.databricks.models.ErrorInfo
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorInfo'},
    }

    def __init__(self, *, error, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class Operation(Model):
    """REST API operation.

    :param name: Operation name: {provider}/{resource}/{operation}
    :type name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.databricks.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, *, name: str=None, display=None, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display


class OperationDisplay(Model):
    """The object that represents the operation.

    :param provider: Service provider: Microsoft.ResourceProvider
    :type provider: str
    :param resource: Resource on which the operation is performed.
    :type resource: str
    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(self, *, provider: str=None, resource: str=None, operation: str=None, **kwargs) -> None:
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation


class Resource(Model):
    """The core properties of ARM resources.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class Sku(Model):
    """SKU for the resource.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The SKU name.
    :type name: str
    :param tier: The SKU tier.
    :type tier: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(self, *, name: str, tier: str=None, **kwargs) -> None:
        super(Sku, self).__init__(**kwargs)
        self.name = name
        self.tier = tier


class TrackedResource(Resource):
    """The resource model definition for a ARM tracked top level resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class Workspace(TrackedResource):
    """Information about workspace.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param managed_resource_group_id: Required. The managed resource group Id.
    :type managed_resource_group_id: str
    :param parameters: The workspace's custom parameters.
    :type parameters: ~azure.mgmt.databricks.models.WorkspaceCustomParameters
    :ivar provisioning_state: The workspace provisioning state. Possible
     values include: 'Accepted', 'Running', 'Ready', 'Creating', 'Created',
     'Deleting', 'Deleted', 'Canceled', 'Failed', 'Succeeded', 'Updating'
    :vartype provisioning_state: str or
     ~azure.mgmt.databricks.models.ProvisioningState
    :param ui_definition_uri: The blob URI where the UI definition file is
     located.
    :type ui_definition_uri: str
    :param authorizations: The workspace provider authorizations.
    :type authorizations:
     list[~azure.mgmt.databricks.models.WorkspaceProviderAuthorization]
    :param sku: The SKU of the resource.
    :type sku: ~azure.mgmt.databricks.models.Sku
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'managed_resource_group_id': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'managed_resource_group_id': {'key': 'properties.managedResourceGroupId', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': 'WorkspaceCustomParameters'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'ui_definition_uri': {'key': 'properties.uiDefinitionUri', 'type': 'str'},
        'authorizations': {'key': 'properties.authorizations', 'type': '[WorkspaceProviderAuthorization]'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, *, location: str, managed_resource_group_id: str, tags=None, parameters=None, ui_definition_uri: str=None, authorizations=None, sku=None, **kwargs) -> None:
        super(Workspace, self).__init__(tags=tags, location=location, **kwargs)
        self.managed_resource_group_id = managed_resource_group_id
        self.parameters = parameters
        self.provisioning_state = None
        self.ui_definition_uri = ui_definition_uri
        self.authorizations = authorizations
        self.sku = sku


class WorkspaceCustomBooleanParameter(Model):
    """The value which should be used for this field.

    All required parameters must be populated in order to send to Azure.

    :param type: The type of variable that this is. Possible values include:
     'Bool', 'Object', 'String'
    :type type: str or ~azure.mgmt.databricks.models.CustomParameterType
    :param value: Required. The value which should be used for this field.
    :type value: bool
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'bool'},
    }

    def __init__(self, *, value: bool, type=None, **kwargs) -> None:
        super(WorkspaceCustomBooleanParameter, self).__init__(**kwargs)
        self.type = type
        self.value = value


class WorkspaceCustomObjectParameter(Model):
    """The value which should be used for this field.

    All required parameters must be populated in order to send to Azure.

    :param type: The type of variable that this is. Possible values include:
     'Bool', 'Object', 'String'
    :type type: str or ~azure.mgmt.databricks.models.CustomParameterType
    :param value: Required. The value which should be used for this field.
    :type value: object
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'},
    }

    def __init__(self, *, value, type=None, **kwargs) -> None:
        super(WorkspaceCustomObjectParameter, self).__init__(**kwargs)
        self.type = type
        self.value = value


class WorkspaceCustomParameters(Model):
    """Custom Parameters used for Cluster Creation.

    :param aml_workspace_id: The Workspace ID of an Azure Machine Learning
     Workspace
    :type aml_workspace_id:
     ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param custom_virtual_network_id: The ID of a Virtual Network where this
     Databricks Cluster should be created
    :type custom_virtual_network_id:
     ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param custom_public_subnet_name: The name of a Public Subnet within the
     Virtual Network
    :type custom_public_subnet_name:
     ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param custom_private_subnet_name: The name of the Private Subnet within
     the Virtual Network
    :type custom_private_subnet_name:
     ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param enable_no_public_ip: Should the Public IP be Disabled?
    :type enable_no_public_ip:
     ~azure.mgmt.databricks.models.WorkspaceCustomBooleanParameter
    :param load_balancer_backend_pool_name: The name of a Backend Address Pool
     within an Azure Load Balancer
    :type load_balancer_backend_pool_name:
     ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param load_balancer_id: The Resource ID of an Azure Load Balancer
    :type load_balancer_id:
     ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param relay_namespace_name: The name of an Azure Relay Namespace
    :type relay_namespace_name:
     ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param storage_account_name: The name which should be used for the Storage
     Account
    :type storage_account_name:
     ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param storage_account_sku_name: The SKU which should be used for this
     Storage Account
    :type storage_account_sku_name:
     ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    :param resource_tags: A map of Tags which should be applied to the
     resources used by this Databricks Cluster.
    :type resource_tags:
     ~azure.mgmt.databricks.models.WorkspaceCustomObjectParameter
    :param vnet_address_prefix: The first 2 octets of the virtual network /16
     address range (e.g., '10.139' for the address range 10.139.0.0/16).
    :type vnet_address_prefix:
     ~azure.mgmt.databricks.models.WorkspaceCustomStringParameter
    """

    _attribute_map = {
        'aml_workspace_id': {'key': 'amlWorkspaceId', 'type': 'WorkspaceCustomStringParameter'},
        'custom_virtual_network_id': {'key': 'customVirtualNetworkId', 'type': 'WorkspaceCustomStringParameter'},
        'custom_public_subnet_name': {'key': 'customPublicSubnetName', 'type': 'WorkspaceCustomStringParameter'},
        'custom_private_subnet_name': {'key': 'customPrivateSubnetName', 'type': 'WorkspaceCustomStringParameter'},
        'enable_no_public_ip': {'key': 'enableNoPublicIp', 'type': 'WorkspaceCustomBooleanParameter'},
        'load_balancer_backend_pool_name': {'key': 'loadBalancerBackendPoolName', 'type': 'WorkspaceCustomStringParameter'},
        'load_balancer_id': {'key': 'loadBalancerId', 'type': 'WorkspaceCustomStringParameter'},
        'relay_namespace_name': {'key': 'relayNamespaceName', 'type': 'WorkspaceCustomStringParameter'},
        'storage_account_name': {'key': 'storageAccountName', 'type': 'WorkspaceCustomStringParameter'},
        'storage_account_sku_name': {'key': 'storageAccountSkuName', 'type': 'WorkspaceCustomStringParameter'},
        'resource_tags': {'key': 'resourceTags', 'type': 'WorkspaceCustomObjectParameter'},
        'vnet_address_prefix': {'key': 'vnetAddressPrefix', 'type': 'WorkspaceCustomStringParameter'},
    }

    def __init__(self, *, aml_workspace_id=None, custom_virtual_network_id=None, custom_public_subnet_name=None, custom_private_subnet_name=None, enable_no_public_ip=None, load_balancer_backend_pool_name=None, load_balancer_id=None, relay_namespace_name=None, storage_account_name=None, storage_account_sku_name=None, resource_tags=None, vnet_address_prefix=None, **kwargs) -> None:
        super(WorkspaceCustomParameters, self).__init__(**kwargs)
        self.aml_workspace_id = aml_workspace_id
        self.custom_virtual_network_id = custom_virtual_network_id
        self.custom_public_subnet_name = custom_public_subnet_name
        self.custom_private_subnet_name = custom_private_subnet_name
        self.enable_no_public_ip = enable_no_public_ip
        self.load_balancer_backend_pool_name = load_balancer_backend_pool_name
        self.load_balancer_id = load_balancer_id
        self.relay_namespace_name = relay_namespace_name
        self.storage_account_name = storage_account_name
        self.storage_account_sku_name = storage_account_sku_name
        self.resource_tags = resource_tags
        self.vnet_address_prefix = vnet_address_prefix


class WorkspaceCustomStringParameter(Model):
    """The Value.

    All required parameters must be populated in order to send to Azure.

    :param type: The type of variable that this is. Possible values include:
     'Bool', 'Object', 'String'
    :type type: str or ~azure.mgmt.databricks.models.CustomParameterType
    :param value: Required. The value which should be used for this field.
    :type value: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, *, value: str, type=None, **kwargs) -> None:
        super(WorkspaceCustomStringParameter, self).__init__(**kwargs)
        self.type = type
        self.value = value


class WorkspaceProviderAuthorization(Model):
    """The workspace provider authorization.

    All required parameters must be populated in order to send to Azure.

    :param principal_id: Required. The provider's principal identifier. This
     is the identity that the provider will use to call ARM to manage the
     workspace resources.
    :type principal_id: str
    :param role_definition_id: Required. The provider's role definition
     identifier. This role will define all the permissions that the provider
     must have on the workspace's container resource group. This role
     definition cannot have permission to delete the resource group.
    :type role_definition_id: str
    """

    _validation = {
        'principal_id': {'required': True},
        'role_definition_id': {'required': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'role_definition_id': {'key': 'roleDefinitionId', 'type': 'str'},
    }

    def __init__(self, *, principal_id: str, role_definition_id: str, **kwargs) -> None:
        super(WorkspaceProviderAuthorization, self).__init__(**kwargs)
        self.principal_id = principal_id
        self.role_definition_id = role_definition_id


class WorkspaceUpdate(Model):
    """An update to a workspace.

    :param tags: Resource tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, tags=None, **kwargs) -> None:
        super(WorkspaceUpdate, self).__init__(**kwargs)
        self.tags = tags