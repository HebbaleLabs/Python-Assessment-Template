import connexion
import six

from swagger_server.models.business_platform_object_array import BusinessPlatformObjectArray  # noqa: E501
from swagger_server.models.business_platform_object_update import BusinessPlatformObjectUpdate  # noqa: E501
from swagger_server.models.business_platform_results_objects import BusinessPlatformResultsObjects  # noqa: E501
from swagger_server.models.business_platform_summary_results_object import BusinessPlatformSummaryResultsObject  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server import util


def add_business_platforms(businessId, body):  # noqa: E501
    """Add a new Business Platform for a Business

    \&quot;This request saves one or many Customer Platforms in CAS.\&quot;  # noqa: E501

    :param businessId: Id of Business for which platform is getting saved.
    :type businessId: str
    :param body: Business Platform object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = BusinessPlatformObjectArray.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_business_platform(businessId, orgName, version, body):  # noqa: E501
    """Modify an existing Business Platform

    \&quot;This request updates a Business Platform in CAS.\&quot;  # noqa: E501

    :param businessId: Business Id
    :type businessId: str
    :param orgName: organization name
    :type orgName: str
    :param version: Current Version Number obtained before update
    :type version: int
    :param body: Business Platform object that needs to be modified in the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = BusinessPlatformObjectUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_all_business_platforms(businessId, offset=None, limit=None, query=None):  # noqa: E501
    """Get all Business Platforms

    \&quot;This request retrieves all Business Platforms from CAS.\&quot;  # noqa: E501

    :param businessId: Pan of Business for which platform is getting saved.
    :type businessId: str
    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: BusinessPlatformSummaryResultsObject
    """
    return 'do some magic!'


def get_business_platform_by_id(businessId, orgName):  # noqa: E501
    """Find Business Platform by ID

    Returns an Customer # noqa: E501

    :param businessId: Business Id
    :type businessId: str
    :param orgName: organization name
    :type orgName: str

    :rtype: BusinessPlatformResultsObjects
    """
    return 'do some magic!'
