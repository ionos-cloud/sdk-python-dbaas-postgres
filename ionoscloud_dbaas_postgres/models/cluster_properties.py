# coding: utf-8

"""
    IONOS DBaaS PostgreSQL REST API

    An enterprise-grade Database is provided as a Service (DBaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.  The API allows you to create additional PostgreSQL database clusters or modify existing ones. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_dbaas_postgres.configuration import Configuration


class ClusterProperties(object):
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

        'display_name': 'str',

        'postgres_version': 'str',

        'location': 'str',

        'dns_name': 'str',

        'backup_location': 'str',

        'instances': 'int',

        'ram': 'int',

        'cores': 'int',

        'storage_size': 'int',

        'storage_type': 'StorageType',

        'connections': 'list[Connection]',

        'maintenance_window': 'MaintenanceWindow',

        'synchronization_mode': 'SynchronizationMode',
    }

    attribute_map = {

        'display_name': 'displayName',

        'postgres_version': 'postgresVersion',

        'location': 'location',

        'dns_name': 'dnsName',

        'backup_location': 'backupLocation',

        'instances': 'instances',

        'ram': 'ram',

        'cores': 'cores',

        'storage_size': 'storageSize',

        'storage_type': 'storageType',

        'connections': 'connections',

        'maintenance_window': 'maintenanceWindow',

        'synchronization_mode': 'synchronizationMode',
    }

    def __init__(self, display_name=None, postgres_version=None, location=None, dns_name=None, backup_location=None, instances=None, ram=None, cores=None, storage_size=None, storage_type=None, connections=None, maintenance_window=None, synchronization_mode=None, local_vars_configuration=None):  # noqa: E501
        """ClusterProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._postgres_version = None
        self._location = None
        self._dns_name = None
        self._backup_location = None
        self._instances = None
        self._ram = None
        self._cores = None
        self._storage_size = None
        self._storage_type = None
        self._connections = None
        self._maintenance_window = None
        self._synchronization_mode = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if postgres_version is not None:
            self.postgres_version = postgres_version
        if location is not None:
            self.location = location
        if dns_name is not None:
            self.dns_name = dns_name
        if backup_location is not None:
            self.backup_location = backup_location
        if instances is not None:
            self.instances = instances
        if ram is not None:
            self.ram = ram
        if cores is not None:
            self.cores = cores
        if storage_size is not None:
            self.storage_size = storage_size
        if storage_type is not None:
            self.storage_type = storage_type
        if connections is not None:
            self.connections = connections
        if maintenance_window is not None:
            self.maintenance_window = maintenance_window
        if synchronization_mode is not None:
            self.synchronization_mode = synchronization_mode


    @property
    def display_name(self):
        """Gets the display_name of this ClusterProperties.  # noqa: E501

        The friendly name of your cluster.  # noqa: E501

        :return: The display_name of this ClusterProperties.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ClusterProperties.

        The friendly name of your cluster.  # noqa: E501

        :param display_name: The display_name of this ClusterProperties.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def postgres_version(self):
        """Gets the postgres_version of this ClusterProperties.  # noqa: E501

        The PostgreSQL version of your cluster.  # noqa: E501

        :return: The postgres_version of this ClusterProperties.  # noqa: E501
        :rtype: str
        """
        return self._postgres_version

    @postgres_version.setter
    def postgres_version(self, postgres_version):
        """Sets the postgres_version of this ClusterProperties.

        The PostgreSQL version of your cluster.  # noqa: E501

        :param postgres_version: The postgres_version of this ClusterProperties.  # noqa: E501
        :type postgres_version: str
        """

        self._postgres_version = postgres_version

    @property
    def location(self):
        """Gets the location of this ClusterProperties.  # noqa: E501

        The physical location where the cluster will be created. This will be where all of your instances live. Property cannot be modified after datacenter creation.   # noqa: E501

        :return: The location of this ClusterProperties.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ClusterProperties.

        The physical location where the cluster will be created. This will be where all of your instances live. Property cannot be modified after datacenter creation.   # noqa: E501

        :param location: The location of this ClusterProperties.  # noqa: E501
        :type location: str
        """

        self._location = location

    @property
    def dns_name(self):
        """Gets the dns_name of this ClusterProperties.  # noqa: E501

        The DNS name pointing to your cluster.  # noqa: E501

        :return: The dns_name of this ClusterProperties.  # noqa: E501
        :rtype: str
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        """Sets the dns_name of this ClusterProperties.

        The DNS name pointing to your cluster.  # noqa: E501

        :param dns_name: The dns_name of this ClusterProperties.  # noqa: E501
        :type dns_name: str
        """

        self._dns_name = dns_name

    @property
    def backup_location(self):
        """Gets the backup_location of this ClusterProperties.  # noqa: E501

        The S3 location where the backups will be stored.  # noqa: E501

        :return: The backup_location of this ClusterProperties.  # noqa: E501
        :rtype: str
        """
        return self._backup_location

    @backup_location.setter
    def backup_location(self, backup_location):
        """Sets the backup_location of this ClusterProperties.

        The S3 location where the backups will be stored.  # noqa: E501

        :param backup_location: The backup_location of this ClusterProperties.  # noqa: E501
        :type backup_location: str
        """

        self._backup_location = backup_location

    @property
    def instances(self):
        """Gets the instances of this ClusterProperties.  # noqa: E501

        The total number of instances in the cluster (one master and n-1 standbys).   # noqa: E501

        :return: The instances of this ClusterProperties.  # noqa: E501
        :rtype: int
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ClusterProperties.

        The total number of instances in the cluster (one master and n-1 standbys).   # noqa: E501

        :param instances: The instances of this ClusterProperties.  # noqa: E501
        :type instances: int
        """
        if (self.local_vars_configuration.client_side_validation and
                instances is not None and instances > 5):  # noqa: E501
            raise ValueError("Invalid value for `instances`, must be a value less than or equal to `5`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instances is not None and instances < 1):  # noqa: E501
            raise ValueError("Invalid value for `instances`, must be a value greater than or equal to `1`")  # noqa: E501

        self._instances = instances

    @property
    def ram(self):
        """Gets the ram of this ClusterProperties.  # noqa: E501

        The amount of memory per instance in megabytes. Has to be a multiple of 1024.  # noqa: E501

        :return: The ram of this ClusterProperties.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this ClusterProperties.

        The amount of memory per instance in megabytes. Has to be a multiple of 1024.  # noqa: E501

        :param ram: The ram of this ClusterProperties.  # noqa: E501
        :type ram: int
        """
        if (self.local_vars_configuration.client_side_validation and
                ram is not None and ram < 2048):  # noqa: E501
            raise ValueError("Invalid value for `ram`, must be a value greater than or equal to `2048`")  # noqa: E501

        self._ram = ram

    @property
    def cores(self):
        """Gets the cores of this ClusterProperties.  # noqa: E501

        The number of CPU cores per instance.  # noqa: E501

        :return: The cores of this ClusterProperties.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this ClusterProperties.

        The number of CPU cores per instance.  # noqa: E501

        :param cores: The cores of this ClusterProperties.  # noqa: E501
        :type cores: int
        """
        if (self.local_vars_configuration.client_side_validation and
                cores is not None and cores < 1):  # noqa: E501
            raise ValueError("Invalid value for `cores`, must be a value greater than or equal to `1`")  # noqa: E501

        self._cores = cores

    @property
    def storage_size(self):
        """Gets the storage_size of this ClusterProperties.  # noqa: E501

        The amount of storage per instance in megabytes.  # noqa: E501

        :return: The storage_size of this ClusterProperties.  # noqa: E501
        :rtype: int
        """
        return self._storage_size

    @storage_size.setter
    def storage_size(self, storage_size):
        """Sets the storage_size of this ClusterProperties.

        The amount of storage per instance in megabytes.  # noqa: E501

        :param storage_size: The storage_size of this ClusterProperties.  # noqa: E501
        :type storage_size: int
        """
        if (self.local_vars_configuration.client_side_validation and
                storage_size is not None and storage_size > 2097152):  # noqa: E501
            raise ValueError("Invalid value for `storage_size`, must be a value less than or equal to `2097152`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                storage_size is not None and storage_size < 2048):  # noqa: E501
            raise ValueError("Invalid value for `storage_size`, must be a value greater than or equal to `2048`")  # noqa: E501

        self._storage_size = storage_size

    @property
    def storage_type(self):
        """Gets the storage_type of this ClusterProperties.  # noqa: E501


        :return: The storage_type of this ClusterProperties.  # noqa: E501
        :rtype: StorageType
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this ClusterProperties.


        :param storage_type: The storage_type of this ClusterProperties.  # noqa: E501
        :type storage_type: StorageType
        """

        self._storage_type = storage_type

    @property
    def connections(self):
        """Gets the connections of this ClusterProperties.  # noqa: E501


        :return: The connections of this ClusterProperties.  # noqa: E501
        :rtype: list[Connection]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this ClusterProperties.


        :param connections: The connections of this ClusterProperties.  # noqa: E501
        :type connections: list[Connection]
        """
        if (self.local_vars_configuration.client_side_validation and
                connections is not None and len(connections) > 1):
            raise ValueError("Invalid value for `connections`, number of items must be less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                connections is not None and len(connections) < 1):
            raise ValueError("Invalid value for `connections`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._connections = connections

    @property
    def maintenance_window(self):
        """Gets the maintenance_window of this ClusterProperties.  # noqa: E501


        :return: The maintenance_window of this ClusterProperties.  # noqa: E501
        :rtype: MaintenanceWindow
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """Sets the maintenance_window of this ClusterProperties.


        :param maintenance_window: The maintenance_window of this ClusterProperties.  # noqa: E501
        :type maintenance_window: MaintenanceWindow
        """

        self._maintenance_window = maintenance_window

    @property
    def synchronization_mode(self):
        """Gets the synchronization_mode of this ClusterProperties.  # noqa: E501


        :return: The synchronization_mode of this ClusterProperties.  # noqa: E501
        :rtype: SynchronizationMode
        """
        return self._synchronization_mode

    @synchronization_mode.setter
    def synchronization_mode(self, synchronization_mode):
        """Sets the synchronization_mode of this ClusterProperties.


        :param synchronization_mode: The synchronization_mode of this ClusterProperties.  # noqa: E501
        :type synchronization_mode: SynchronizationMode
        """

        self._synchronization_mode = synchronization_mode
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
        if not isinstance(other, ClusterProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterProperties):
            return True

        return self.to_dict() != other.to_dict()
