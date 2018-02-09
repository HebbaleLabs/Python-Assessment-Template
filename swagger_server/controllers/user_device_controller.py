import connexion
import six

from swagger_server.models.device_array import DeviceArray  # noqa: E501
from swagger_server.models.device_object import DeviceObject  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server import util


def add_device(userId, body):  # noqa: E501
    """Add a new device to the user

    \&quot;This request saves a device for a user.\&quot;  # noqa: E501

    :param userId: user id
    :type userId: str
    :param body: device data that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = DeviceObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_all_devices(userId):  # noqa: E501
    """Get all user registered devices

    Get all user registered devices # noqa: E501

    :param userId: user id
    :type userId: str

    :rtype: List[DeviceArray]
    """
    return 'do some magic!'
