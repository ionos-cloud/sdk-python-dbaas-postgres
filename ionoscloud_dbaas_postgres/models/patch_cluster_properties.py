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


class PatchClusterProperties(object):
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

        'cores': 'int',

        'ram': 'int',

        'storage_size': 'int',

        'connections': 'list[Connection]',

        'display_name': 'str',

        'maintenance_window': 'MaintenanceWindow',

        'postgres_version': 'str',

        'instances': 'int',
    }

    attribute_map = {

        'cores': 'cores',

        'ram': 'ram',

        'storage_size': 'storageSize',

        'connections': 'connections',

        'display_name': 'displayName',

        'maintenance_window': 'maintenanceWindow',

        'postgres_version': 'postgresVersion',

        'instances': 'instances',
    }

    def __init__(self, cores=None, ram=None, storage_size=None, connections=None, display_name=None, maintenance_window=None, postgres_version=None, instances=None, local_vars_configuration=None):  # noqa: E501
        """PatchClusterProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cores = None
        self._ram = None
        self._storage_size = None
        self._connections = None
        self._display_name = None
        self._maintenance_window = None
        self._postgres_version = None
        self._instances = None
        self.discriminator = None

        if cores is not None:
            self.cores = cores
        if ram is not None:
            self.ram = ram
        if storage_size is not None:
            self.storage_size = storage_size
        if connections is not None:
            self.connections = connections
        if display_name is not None:
            self.display_name = display_name
        if maintenance_window is not None:
            self.maintenance_window = maintenance_window
        if postgres_version is not None:
            self.postgres_version = postgres_version
        if instances is not None:
            self.instances = instances


    @property
    def cores(self):
        """Gets the cores of this PatchClusterProperties.  # noqa: E501

        The number of CPU cores per instance.  # noqa: E501

        :return: The cores of this PatchClusterProperties.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this PatchClusterProperties.

        The number of CPU cores per instance.  # noqa: E501

        :param cores: The cores of this PatchClusterProperties.  # noqa: E501
        :type cores: int
        """
        if (self.local_vars_configuration.client_side_validation and
                cores is not None and cores < 1):  # noqa: E501
            raise ValueError("Invalid value for `cores`, must be a value greater than or equal to `1`")  # noqa: E501

        self._cores = cores

    @property
    def ram(self):
        """Gets the ram of this PatchClusterProperties.  # noqa: E501

        The amount of memory per instance in megabytes. Has to be a multiple of 1024.  # noqa: E501

        :return: The ram of this PatchClusterProperties.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this PatchClusterProperties.

        The amount of memory per instance in megabytes. Has to be a multiple of 1024.  # noqa: E501

        :param ram: The ram of this PatchClusterProperties.  # noqa: E501
        :type ram: int
        """
        if (self.local_vars_configuration.client_side_validation and
                ram is not None and ram < 2048):  # noqa: E501
            raise ValueError("Invalid value for `ram`, must be a value greater than or equal to `2048`")  # noqa: E501

        self._ram = ram

    @property
    def storage_size(self):
        """Gets the storage_size of this PatchClusterProperties.  # noqa: E501

        The amount of storage per instance in megabytes.  # noqa: E501

        :return: The storage_size of this PatchClusterProperties.  # noqa: E501
        :rtype: int
        """
        return self._storage_size

    @storage_size.setter
    def storage_size(self, storage_size):
        """Sets the storage_size of this PatchClusterProperties.

        The amount of storage per instance in megabytes.  # noqa: E501

        :param storage_size: The storage_size of this PatchClusterProperties.  # noqa: E501
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
    def connections(self):
        """Gets the connections of this PatchClusterProperties.  # noqa: E501


        :return: The connections of this PatchClusterProperties.  # noqa: E501
        :rtype: list[Connection]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this PatchClusterProperties.


        :param connections: The connections of this PatchClusterProperties.  # noqa: E501
        :type connections: list[Connection]
        """
        if (self.local_vars_configuration.client_side_validation and
                connections is not None and len(connections) > 1):
            raise ValueError("Invalid value for `connections`, number of items must be less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                connections is not None and len(connections) < 0):
            raise ValueError("Invalid value for `connections`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._connections = connections

    @property
    def display_name(self):
        """Gets the display_name of this PatchClusterProperties.  # noqa: E501

        The friendly name of your cluster.  # noqa: E501

        :return: The display_name of this PatchClusterProperties.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PatchClusterProperties.

        The friendly name of your cluster.  # noqa: E501

        :param display_name: The display_name of this PatchClusterProperties.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def maintenance_window(self):
        """Gets the maintenance_window of this PatchClusterProperties.  # noqa: E501


        :return: The maintenance_window of this PatchClusterProperties.  # noqa: E501
        :rtype: MaintenanceWindow
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """Sets the maintenance_window of this PatchClusterProperties.


        :param maintenance_window: The maintenance_window of this PatchClusterProperties.  # noqa: E501
        :type maintenance_window: MaintenanceWindow
        """

        self._maintenance_window = maintenance_window

    @property
    def postgres_version(self):
        """Gets the postgres_version of this PatchClusterProperties.  # noqa: E501

        The PostgreSQL version of your cluster.  # noqa: E501

        :return: The postgres_version of this PatchClusterProperties.  # noqa: E501
        :rtype: str
        """
        return self._postgres_version

    @postgres_version.setter
    def postgres_version(self, postgres_version):
        """Sets the postgres_version of this PatchClusterProperties.

        The PostgreSQL version of your cluster.  # noqa: E501

        :param postgres_version: The postgres_version of this PatchClusterProperties.  # noqa: E501
        :type postgres_version: str
        """

        self._postgres_version = postgres_version

    @property
    def instances(self):
        """Gets the instances of this PatchClusterProperties.  # noqa: E501

        The total number of instances in the cluster (one master and n-1 standbys).   # noqa: E501

        :return: The instances of this PatchClusterProperties.  # noqa: E501
        :rtype: int
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this PatchClusterProperties.

        The total number of instances in the cluster (one master and n-1 standbys).   # noqa: E501

        :param instances: The instances of this PatchClusterProperties.  # noqa: E501
        :type instances: int
        """
        if (self.local_vars_configuration.client_side_validation and
                instances is not None and instances > 5):  # noqa: E501
            raise ValueError("Invalid value for `instances`, must be a value less than or equal to `5`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instances is not None and instances < 1):  # noqa: E501
            raise ValueError("Invalid value for `instances`, must be a value greater than or equal to `1`")  # noqa: E501

        self._instances = instances
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
        if not isinstance(other, PatchClusterProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchClusterProperties):
            return True

        return self.to_dict() != other.to_dict()
