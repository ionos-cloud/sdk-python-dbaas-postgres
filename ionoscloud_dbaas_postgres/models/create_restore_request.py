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


class CreateRestoreRequest(object):
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

        'backup_id': 'str',

        'recovery_target_time': 'datetime',
    }

    attribute_map = {

        'backup_id': 'backupId',

        'recovery_target_time': 'recoveryTargetTime',
    }

    def __init__(self, backup_id=None, recovery_target_time=None, local_vars_configuration=None):  # noqa: E501
        """CreateRestoreRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._backup_id = None
        self._recovery_target_time = None
        self.discriminator = None

        self.backup_id = backup_id
        if recovery_target_time is not None:
            self.recovery_target_time = recovery_target_time


    @property
    def backup_id(self):
        """Gets the backup_id of this CreateRestoreRequest.  # noqa: E501

        The unique ID of the backup you want to restore.  # noqa: E501

        :return: The backup_id of this CreateRestoreRequest.  # noqa: E501
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this CreateRestoreRequest.

        The unique ID of the backup you want to restore.  # noqa: E501

        :param backup_id: The backup_id of this CreateRestoreRequest.  # noqa: E501
        :type backup_id: str
        """
        if self.local_vars_configuration.client_side_validation and backup_id is None:  # noqa: E501
            raise ValueError("Invalid value for `backup_id`, must not be `None`")  # noqa: E501

        self._backup_id = backup_id

    @property
    def recovery_target_time(self):
        """Gets the recovery_target_time of this CreateRestoreRequest.  # noqa: E501

        If this value is supplied as ISO 8601 timestamp, the backup will be replayed up until the given timestamp. If empty, the backup will be applied completely.   # noqa: E501

        :return: The recovery_target_time of this CreateRestoreRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._recovery_target_time

    @recovery_target_time.setter
    def recovery_target_time(self, recovery_target_time):
        """Sets the recovery_target_time of this CreateRestoreRequest.

        If this value is supplied as ISO 8601 timestamp, the backup will be replayed up until the given timestamp. If empty, the backup will be applied completely.   # noqa: E501

        :param recovery_target_time: The recovery_target_time of this CreateRestoreRequest.  # noqa: E501
        :type recovery_target_time: datetime
        """

        self._recovery_target_time = recovery_target_time
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
        if not isinstance(other, CreateRestoreRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateRestoreRequest):
            return True

        return self.to_dict() != other.to_dict()
