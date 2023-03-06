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


class ClusterList(object):
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

        'type': 'ResourceType',

        'id': 'str',

        'items': 'list[ClusterResponse]',

        'offset': 'int',

        'limit': 'int',

        'links': 'PaginationLinks',
    }

    attribute_map = {

        'type': 'type',

        'id': 'id',

        'items': 'items',

        'offset': 'offset',

        'limit': 'limit',

        'links': '_links',
    }

    def __init__(self, type=None, id=None, items=None, offset=None, limit=None, links=None, local_vars_configuration=None):  # noqa: E501
        """ClusterList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._id = None
        self._items = None
        self._offset = None
        self._limit = None
        self._links = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if items is not None:
            self.items = items
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if links is not None:
            self.links = links


    @property
    def type(self):
        """Gets the type of this ClusterList.  # noqa: E501


        :return: The type of this ClusterList.  # noqa: E501
        :rtype: ResourceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClusterList.


        :param type: The type of this ClusterList.  # noqa: E501
        :type type: ResourceType
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this ClusterList.  # noqa: E501

        The unique ID of the resource.  # noqa: E501

        :return: The id of this ClusterList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterList.

        The unique ID of the resource.  # noqa: E501

        :param id: The id of this ClusterList.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def items(self):
        """Gets the items of this ClusterList.  # noqa: E501


        :return: The items of this ClusterList.  # noqa: E501
        :rtype: list[ClusterResponse]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ClusterList.


        :param items: The items of this ClusterList.  # noqa: E501
        :type items: list[ClusterResponse]
        """

        self._items = items

    @property
    def offset(self):
        """Gets the offset of this ClusterList.  # noqa: E501

        The offset specified in the request (if none was specified, the default offset is 0) (not implemented yet).   # noqa: E501

        :return: The offset of this ClusterList.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ClusterList.

        The offset specified in the request (if none was specified, the default offset is 0) (not implemented yet).   # noqa: E501

        :param offset: The offset of this ClusterList.  # noqa: E501
        :type offset: int
        """
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset < 0):  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ClusterList.  # noqa: E501

        The limit specified in the request (if none was specified, use the endpoint's default pagination limit) (not implemented yet, always return number of items).   # noqa: E501

        :return: The limit of this ClusterList.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ClusterList.

        The limit specified in the request (if none was specified, use the endpoint's default pagination limit) (not implemented yet, always return number of items).   # noqa: E501

        :param limit: The limit of this ClusterList.  # noqa: E501
        :type limit: int
        """
        if (self.local_vars_configuration.client_side_validation and
                limit is not None and limit < 0):  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._limit = limit

    @property
    def links(self):
        """Gets the links of this ClusterList.  # noqa: E501


        :return: The links of this ClusterList.  # noqa: E501
        :rtype: PaginationLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ClusterList.


        :param links: The links of this ClusterList.  # noqa: E501
        :type links: PaginationLinks
        """

        self._links = links
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
        if not isinstance(other, ClusterList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterList):
            return True

        return self.to_dict() != other.to_dict()
