import connexion
import six

from swagger_server.models.business_object import BusinessObject  # noqa: E501
from swagger_server.models.business_object_update import BusinessObjectUpdate  # noqa: E501
from swagger_server.models.business_results_object import BusinessResultsObject  # noqa: E501
from swagger_server.models.business_summary_results_object import BusinessSummaryResultsObject  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server import util


def add_business(body):  # noqa: E501
    """Add a new Business

    \&quot;This request saves a Business in CAS.\&quot;  # noqa: E501

    :param body: Business object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = BusinessObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_business(businessId, version, body):  # noqa: E501
    """Modify an existing Business

    \&quot;This request updates a Business in CAS.\&quot;  # noqa: E501

    :param businessId: Id of Business that needs to be updated
    :type businessId: str
    :param version: Current Version Number obtained before update
    :type version: int
    :param body: Business object that needs to be modified in the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = BusinessObjectUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_businesess(offset=None, limit=None, query=None):  # noqa: E501
    """Get all Businessess

    \&quot;This request retrieves customers from CAS.\&quot;  # noqa: E501

    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: str

    :rtype: List[BusinessSummaryResultsObject]
    """
    return 'do some magic!'


def get_business_by_id(businessId):  # noqa: E501
    """Find Business by Id

    Returns a Business # noqa: E501

    :param businessId: Id of Business that needs to be queried
    :type businessId: str

    :rtype: BusinessResultsObject
    """
    return 'do some magic!'
