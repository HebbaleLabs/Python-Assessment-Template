import connexion
import six

from swagger_server.models.documents_object import DocumentsObject  # noqa: E501
from swagger_server.models.documents_object_array import DocumentsObjectArray  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server import util


def add_org_platform_documents(org_name, body):  # noqa: E501
    """Upload a platform purchase/sale Info file

    \&quot;This request uploads a platform purchase/sale Info file into CAS for a business.\&quot;  # noqa: E501

    :param org_name: Organization Name
    :type org_name: str
    :param body: Document and its details that needs to be uploaded
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = DocumentsObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_org_platform_documents(org_name, offset=None, limit=None, query=None):  # noqa: E501
    """Get all uploaded documents

    \&quot;This request retrieves uploaded documents from CAS.\&quot;  # noqa: E501

    :param org_name: Organization Name
    :type org_name: str
    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: 
    :type query: List[str]

    :rtype: DocumentsObjectArray
    """
    return 'do some magic!'
