# coding: utf-8

"""
    IONOS DBaaS REST API

    An enterprise-grade Database is provided as a Service (DBaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.  The API allows you to create additional database clusters or modify existing ones. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_dbaas_postgres.configuration import Configuration


class PaginationLinks(object):
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

        'prev': 'str',

        '_self': 'str',

        'next': 'str',
    }

    attribute_map = {

        'prev': 'prev',

        '_self': 'self',

        'next': 'next',
    }

    def __init__(self, prev=None, _self=None, next=None, local_vars_configuration=None):  # noqa: E501
        """PaginationLinks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._prev = None
        self.__self = None
        self._next = None
        self.discriminator = None

        if prev is not None:
            self.prev = prev
        if _self is not None:
            self._self = _self
        if next is not None:
            self.next = next


    @property
    def prev(self):
        """Gets the prev of this PaginationLinks.  # noqa: E501

        URL (with offset and limit parameters) of the previous page; only present if offset is greater than 0.   # noqa: E501

        :return: The prev of this PaginationLinks.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this PaginationLinks.

        URL (with offset and limit parameters) of the previous page; only present if offset is greater than 0.   # noqa: E501

        :param prev: The prev of this PaginationLinks.  # noqa: E501
        :type prev: str
        """

        self._prev = prev

    @property
    def _self(self):
        """Gets the _self of this PaginationLinks.  # noqa: E501

        URL (with offset and limit parameters) of the current page.   # noqa: E501

        :return: The _self of this PaginationLinks.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this PaginationLinks.

        URL (with offset and limit parameters) of the current page.   # noqa: E501

        :param _self: The _self of this PaginationLinks.  # noqa: E501
        :type _self: str
        """

        self.__self = _self

    @property
    def next(self):
        """Gets the next of this PaginationLinks.  # noqa: E501

        URL (with offset and limit parameters) of the next page; only present if offset + limit is less than the total number of elements.   # noqa: E501

        :return: The next of this PaginationLinks.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this PaginationLinks.

        URL (with offset and limit parameters) of the next page; only present if offset + limit is less than the total number of elements.   # noqa: E501

        :param next: The next of this PaginationLinks.  # noqa: E501
        :type next: str
        """

        self._next = next
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
        if not isinstance(other, PaginationLinks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaginationLinks):
            return True

        return self.to_dict() != other.to_dict()
