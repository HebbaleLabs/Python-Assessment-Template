import connexion
import six

from swagger_server import util


def find_all_business_loan_applications(businessId, offset=None, limit=None, query=None):  # noqa: E501
    """Get all Loan Applications for  business

    \&quot;This request retrieves all Loan applications belonging to a business from CAS.\&quot;  # noqa: E501

    :param businessId: Id of Business
    :type businessId: str
    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: None
    """
    return 'do some magic!'
