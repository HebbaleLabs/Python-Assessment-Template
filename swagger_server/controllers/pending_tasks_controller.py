import connexion
import six

from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server import util


def find_all_pending_tasks(userId):  # noqa: E501
    """Get all pending tasks for the user

    Get all pending tasks for the user # noqa: E501

    :param userId: user id
    :type userId: str

    :rtype: None
    """
    return 'do some magic!'
