import connexion
import six

from swagger_server.models.business_address_object import BusinessAddressObject  # noqa: E501
from swagger_server.models.business_address_object_update import BusinessAddressObjectUpdate  # noqa: E501
from swagger_server.models.business_address_results_object import BusinessAddressResultsObject  # noqa: E501
from swagger_server.models.business_address_results_object_single import BusinessAddressResultsObjectSingle  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server import util


def add_business_address(businessId, body):  # noqa: E501
    """Add a new Business Address

    \&quot;This request saves one or many Business Addresses in CAS.\&quot;  # noqa: E501

    :param businessId: Id of Business for which address is getting saved.
    :type businessId: str
    :param body: Business address object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = BusinessAddressObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_business_address(businessId, addressTag, version, body):  # noqa: E501
    """Modify an existing Business Address

    \&quot;This request updates a Customer Bank Account in CAS.\&quot;  # noqa: E501

    :param businessId: Business Id
    :type businessId: str
    :param addressTag: Address Tag
    :type addressTag: str
    :param version: Current Version Number obtained before update
    :type version: int
    :param body: Business Address object that needs to be modified in the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = BusinessAddressObjectUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_all_business_addresses(businessId, offset=None, limit=None, query=None):  # noqa: E501
    """Get all Business Addresses

    \&quot;This request retrieves all Business Addresses from CAS.\&quot;  # noqa: E501

    :param businessId: Pan of Business for which address is getting saved.
    :type businessId: str
    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: BusinessAddressResultsObject
    """
    return 'do some magic!'


def get_business_address_by_id(businessId, addressTag):  # noqa: E501
    """Find Business Address by ID

    Returns an Customer # noqa: E501

    :param businessId: Business Id
    :type businessId: str
    :param addressTag: Address Tag
    :type addressTag: str

    :rtype: BusinessAddressResultsObjectSingle
    """
    return 'do some magic!'
