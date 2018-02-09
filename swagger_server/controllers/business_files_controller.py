import connexion
import six

from swagger_server.models.documents_object import DocumentsObject  # noqa: E501
from swagger_server.models.documents_object_array import DocumentsObjectArray  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server import util


def add_business_documents(businessId, body):  # noqa: E501
    """Upload a business file

    \&quot;This request uploads a file into CAS for a business.\&quot;  # noqa: E501

    :param businessId: Business ID of the business
    :type businessId: str
    :param body: Document and its details that needs to be uploaded
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = DocumentsObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_business_partner_documents(businessId, partnerPan, body):  # noqa: E501
    """Upload a business partner file

    \&quot;This request uploads a file into CAS for a business.\&quot;  # noqa: E501

    :param businessId: Business ID of the business
    :type businessId: str
    :param partnerPan: Pan ID of the business Partner
    :type partnerPan: str
    :param body: Document and its details that needs to be uploaded
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = DocumentsObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_business_documents(businessId, offset=None, limit=None, query=None):  # noqa: E501
    """Get all uploaded documents

    \&quot;This request retrieves uploaded documents from CAS.\&quot;  # noqa: E501

    :param businessId: Business ID of the business
    :type businessId: str
    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: 
    :type query: List[str]

    :rtype: DocumentsObjectArray
    """
    return 'do some magic!'


def find_business_partner_documents(businessId, partnerPan, offset=None, limit=None, query=None):  # noqa: E501
    """Get all uploaded documents

    \&quot;This request retrieves uploaded documents from CAS.\&quot;  # noqa: E501

    :param businessId: Business ID of the business
    :type businessId: str
    :param partnerPan: Pan ID of the business Partner
    :type partnerPan: str
    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: 
    :type query: List[str]

    :rtype: DocumentsObjectArray
    """
    return 'do some magic!'
