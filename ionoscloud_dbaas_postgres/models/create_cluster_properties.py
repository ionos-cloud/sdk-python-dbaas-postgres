# coding: utf-8

"""
    IONOS DBaaS REST API

    An enterprise-grade Database is provided as a Service (DBaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.  The API allows you to create additional database clusters or modify existing ones. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_dbaas_postgres.configuration import Configuration


class CreateClusterProperties(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {

        'postgres_version': 'str',

        'instances': 'int',

        'cores': 'int',

        'ram': 'int',

        'storage_size': 'int',

        'storage_type': 'StorageType',

        'connections': 'list[Connection]',

        'location': 'Location',

        'display_name': 'str',

        'maintenance_window': 'MaintenanceWindow',

        'credentials': 'DBUser',

        'synchronization_mode': 'SynchronizationMode',

        'from_backup': 'CreateRestoreRequest',
    }

    attribute_map = {

        'postgres_version': 'postgresVersion',

        'instances': 'instances',

        'cores': 'cores',

        'ram': 'ram',

        'storage_size': 'storageSize',

        'storage_type': 'storageType',

        'connections': 'connections',

        'location': 'location',

        'display_name': 'displayName',

        'maintenance_window': 'maintenanceWindow',

        'credentials': 'credentials',

        'synchronization_mode': 'synchronizationMode',

        'from_backup': 'fromBackup',
    }

    def __init__(self, postgres_version=None, instances=None, cores=None, ram=None, storage_size=None, storage_type=None, connections=None, location=None, display_name=None, maintenance_window=None, credentials=None, synchronization_mode=None, from_backup=None, local_vars_configuration=None):  # noqa: E501
        """CreateClusterProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._postgres_version = None
        self._instances = None
        self._cores = None
        self._ram = None
        self._storage_size = None
        self._storage_type = None
        self._connections = None
        self._location = None
        self._display_name = None
        self._maintenance_window = None
        self._credentials = None
        self._synchronization_mode = None
        self._from_backup = None
        self.discriminator = None

        self.postgres_version = postgres_version
        self.instances = instances
        self.cores = cores
        self.ram = ram
        self.storage_size = storage_size
        self.storage_type = storage_type
        self.connections = connections
        self.location = location
        self.display_name = display_name
        if maintenance_window is not None:
            self.maintenance_window = maintenance_window
        self.credentials = credentials
        self.synchronization_mode = synchronization_mode
        if from_backup is not None:
            self.from_backup = from_backup


    @property
    def postgres_version(self):
        """Gets the postgres_version of this CreateClusterProperties.  # noqa: E501

        The PostgreSQL version of your cluster.  # noqa: E501

        :return: The postgres_version of this CreateClusterProperties.  # noqa: E501
        :rtype: str
        """
        return self._postgres_version

    @postgres_version.setter
    def postgres_version(self, postgres_version):
        """Sets the postgres_version of this CreateClusterProperties.

        The PostgreSQL version of your cluster.  # noqa: E501

        :param postgres_version: The postgres_version of this CreateClusterProperties.  # noqa: E501
        :type postgres_version: str
        """
        if self.local_vars_configuration.client_side_validation and postgres_version is None:  # noqa: E501
            raise ValueError("Invalid value for `postgres_version`, must not be `None`")  # noqa: E501

        self._postgres_version = postgres_version

    @property
    def instances(self):
        """Gets the instances of this CreateClusterProperties.  # noqa: E501

        The total number of instances in the cluster (one master and n-1 standbys).   # noqa: E501

        :return: The instances of this CreateClusterProperties.  # noqa: E501
        :rtype: int
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this CreateClusterProperties.

        The total number of instances in the cluster (one master and n-1 standbys).   # noqa: E501

        :param instances: The instances of this CreateClusterProperties.  # noqa: E501
        :type instances: int
        """
        if self.local_vars_configuration.client_side_validation and instances is None:  # noqa: E501
            raise ValueError("Invalid value for `instances`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instances is not None and instances > 5):  # noqa: E501
            raise ValueError("Invalid value for `instances`, must be a value less than or equal to `5`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instances is not None and instances < 1):  # noqa: E501
            raise ValueError("Invalid value for `instances`, must be a value greater than or equal to `1`")  # noqa: E501

        self._instances = instances

    @property
    def cores(self):
        """Gets the cores of this CreateClusterProperties.  # noqa: E501

        The number of CPU cores per instance.  # noqa: E501

        :return: The cores of this CreateClusterProperties.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this CreateClusterProperties.

        The number of CPU cores per instance.  # noqa: E501

        :param cores: The cores of this CreateClusterProperties.  # noqa: E501
        :type cores: int
        """
        if self.local_vars_configuration.client_side_validation and cores is None:  # noqa: E501
            raise ValueError("Invalid value for `cores`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cores is not None and cores < 1):  # noqa: E501
            raise ValueError("Invalid value for `cores`, must be a value greater than or equal to `1`")  # noqa: E501

        self._cores = cores

    @property
    def ram(self):
        """Gets the ram of this CreateClusterProperties.  # noqa: E501

        The amount of memory per instance in megabytes. Has to be a multiple of 1024.  # noqa: E501

        :return: The ram of this CreateClusterProperties.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this CreateClusterProperties.

        The amount of memory per instance in megabytes. Has to be a multiple of 1024.  # noqa: E501

        :param ram: The ram of this CreateClusterProperties.  # noqa: E501
        :type ram: int
        """
        if self.local_vars_configuration.client_side_validation and ram is None:  # noqa: E501
            raise ValueError("Invalid value for `ram`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ram is not None and ram < 2048):  # noqa: E501
            raise ValueError("Invalid value for `ram`, must be a value greater than or equal to `2048`")  # noqa: E501

        self._ram = ram

    @property
    def storage_size(self):
        """Gets the storage_size of this CreateClusterProperties.  # noqa: E501

        The amount of storage per instance in megabytes.  # noqa: E501

        :return: The storage_size of this CreateClusterProperties.  # noqa: E501
        :rtype: int
        """
        return self._storage_size

    @storage_size.setter
    def storage_size(self, storage_size):
        """Sets the storage_size of this CreateClusterProperties.

        The amount of storage per instance in megabytes.  # noqa: E501

        :param storage_size: The storage_size of this CreateClusterProperties.  # noqa: E501
        :type storage_size: int
        """
        if self.local_vars_configuration.client_side_validation and storage_size is None:  # noqa: E501
            raise ValueError("Invalid value for `storage_size`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                storage_size is not None and storage_size < 2048):  # noqa: E501
            raise ValueError("Invalid value for `storage_size`, must be a value greater than or equal to `2048`")  # noqa: E501

        self._storage_size = storage_size

    @property
    def storage_type(self):
        """Gets the storage_type of this CreateClusterProperties.  # noqa: E501


        :return: The storage_type of this CreateClusterProperties.  # noqa: E501
        :rtype: StorageType
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this CreateClusterProperties.


        :param storage_type: The storage_type of this CreateClusterProperties.  # noqa: E501
        :type storage_type: StorageType
        """
        if self.local_vars_configuration.client_side_validation and storage_type is None:  # noqa: E501
            raise ValueError("Invalid value for `storage_type`, must not be `None`")  # noqa: E501

        self._storage_type = storage_type

    @property
    def connections(self):
        """Gets the connections of this CreateClusterProperties.  # noqa: E501


        :return: The connections of this CreateClusterProperties.  # noqa: E501
        :rtype: list[Connection]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this CreateClusterProperties.


        :param connections: The connections of this CreateClusterProperties.  # noqa: E501
        :type connections: list[Connection]
        """
        if self.local_vars_configuration.client_side_validation and connections is None:  # noqa: E501
            raise ValueError("Invalid value for `connections`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                connections is not None and len(connections) > 1):
            raise ValueError("Invalid value for `connections`, number of items must be less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                connections is not None and len(connections) < 1):
            raise ValueError("Invalid value for `connections`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._connections = connections

    @property
    def location(self):
        """Gets the location of this CreateClusterProperties.  # noqa: E501


        :return: The location of this CreateClusterProperties.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CreateClusterProperties.


        :param location: The location of this CreateClusterProperties.  # noqa: E501
        :type location: Location
        """
        if self.local_vars_configuration.client_side_validation and location is None:  # noqa: E501
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def display_name(self):
        """Gets the display_name of this CreateClusterProperties.  # noqa: E501

        The friendly name of your cluster.  # noqa: E501

        :return: The display_name of this CreateClusterProperties.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateClusterProperties.

        The friendly name of your cluster.  # noqa: E501

        :param display_name: The display_name of this CreateClusterProperties.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def maintenance_window(self):
        """Gets the maintenance_window of this CreateClusterProperties.  # noqa: E501


        :return: The maintenance_window of this CreateClusterProperties.  # noqa: E501
        :rtype: MaintenanceWindow
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """Sets the maintenance_window of this CreateClusterProperties.


        :param maintenance_window: The maintenance_window of this CreateClusterProperties.  # noqa: E501
        :type maintenance_window: MaintenanceWindow
        """

        self._maintenance_window = maintenance_window

    @property
    def credentials(self):
        """Gets the credentials of this CreateClusterProperties.  # noqa: E501


        :return: The credentials of this CreateClusterProperties.  # noqa: E501
        :rtype: DBUser
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this CreateClusterProperties.


        :param credentials: The credentials of this CreateClusterProperties.  # noqa: E501
        :type credentials: DBUser
        """
        if self.local_vars_configuration.client_side_validation and credentials is None:  # noqa: E501
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    @property
    def synchronization_mode(self):
        """Gets the synchronization_mode of this CreateClusterProperties.  # noqa: E501


        :return: The synchronization_mode of this CreateClusterProperties.  # noqa: E501
        :rtype: SynchronizationMode
        """
        return self._synchronization_mode

    @synchronization_mode.setter
    def synchronization_mode(self, synchronization_mode):
        """Sets the synchronization_mode of this CreateClusterProperties.


        :param synchronization_mode: The synchronization_mode of this CreateClusterProperties.  # noqa: E501
        :type synchronization_mode: SynchronizationMode
        """
        if self.local_vars_configuration.client_side_validation and synchronization_mode is None:  # noqa: E501
            raise ValueError("Invalid value for `synchronization_mode`, must not be `None`")  # noqa: E501

        self._synchronization_mode = synchronization_mode

    @property
    def from_backup(self):
        """Gets the from_backup of this CreateClusterProperties.  # noqa: E501


        :return: The from_backup of this CreateClusterProperties.  # noqa: E501
        :rtype: CreateRestoreRequest
        """
        return self._from_backup

    @from_backup.setter
    def from_backup(self, from_backup):
        """Sets the from_backup of this CreateClusterProperties.


        :param from_backup: The from_backup of this CreateClusterProperties.  # noqa: E501
        :type from_backup: CreateRestoreRequest
        """

        self._from_backup = from_backup
    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateClusterProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateClusterProperties):
            return True

        return self.to_dict() != other.to_dict()
