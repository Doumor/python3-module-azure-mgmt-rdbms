# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class CreateMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The mode to create a new server.
    """

    DEFAULT = "Default"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    GEO_RESTORE = "GeoRestore"
    REPLICA = "Replica"

class GeoRedundantBackup(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enable Geo-redundant or not for server backup.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class IdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The identity type. Set this to 'SystemAssigned' in order to automatically create and assign an
    Azure Active Directory principal for the resource.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"

class InfrastructureEncryption(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Add a second layer of encryption for your data using new encryption algorithm which gives
    additional data protection. Value is optional but if passed in, must be 'Disabled' or
    'Enabled'.
    """

    #: Default value for single layer of encryption for data at rest.
    ENABLED = "Enabled"
    #: Additional (2nd) layer of encryption for data at rest.
    DISABLED = "Disabled"

class MinimalTlsVersionEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enforce a minimal Tls version for the server.
    """

    TLS1_0 = "TLS1_0"
    TLS1_1 = "TLS1_1"
    TLS1_2 = "TLS1_2"
    TLS_ENFORCEMENT_DISABLED = "TLSEnforcementDisabled"

class OperationOrigin(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The intended executor of the operation.
    """

    NOT_SPECIFIED = "NotSpecified"
    USER = "user"
    SYSTEM = "system"

class PrivateEndpointProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """State of the private endpoint connection.
    """

    APPROVING = "Approving"
    READY = "Ready"
    DROPPING = "Dropping"
    FAILED = "Failed"
    REJECTING = "Rejecting"

class PrivateLinkServiceConnectionStateActionsRequire(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The actions required for private link service connection.
    """

    NONE = "None"

class PrivateLinkServiceConnectionStateStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The private link service connection status.
    """

    APPROVED = "Approved"
    PENDING = "Pending"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"

class PublicNetworkAccessEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Whether or not public network access is allowed for this server. Value is optional but if
    passed in, must be 'Enabled' or 'Disabled'
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class QueryPerformanceInsightResetDataResultState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates result of the operation.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"

class SecurityAlertPolicyName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "Default"

class ServerKeyType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The key type like 'AzureKeyVault'.
    """

    AZURE_KEY_VAULT = "AzureKeyVault"

class ServerSecurityAlertPolicyState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the state of the policy, whether it is enabled or disabled.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class ServerState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """A state of a server that is visible to user.
    """

    READY = "Ready"
    DROPPING = "Dropping"
    DISABLED = "Disabled"
    INACCESSIBLE = "Inaccessible"

class ServerVersion(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The version of a server.
    """

    FIVE6 = "5.6"
    FIVE7 = "5.7"
    EIGHT0 = "8.0"

class SkuTier(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The tier of the particular SKU, e.g. Basic.
    """

    BASIC = "Basic"
    GENERAL_PURPOSE = "GeneralPurpose"
    MEMORY_OPTIMIZED = "MemoryOptimized"

class SslEnforcementEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enable ssl enforcement or not when connect to server.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class StorageAutogrow(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enable Storage Auto Grow.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class VirtualNetworkRuleState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Virtual Network Rule State
    """

    INITIALIZING = "Initializing"
    IN_PROGRESS = "InProgress"
    READY = "Ready"
    DELETING = "Deleting"
    UNKNOWN = "Unknown"