import connexion
import six

from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.models.loan_application_documents_array import LoanApplicationDocumentsArray  # noqa: E501
from swagger_server import util


def find_loan_application_docs(loanAppId, offset=None, limit=None, query=None):  # noqa: E501
    """Get all Loan Application Documents

    \&quot;This request retrieves Loan Application Documents from CAS.\&quot;  # noqa: E501

    :param loanAppId: ID of loan application
    :type loanAppId: str
    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: LoanApplicationDocumentsArray
    """
    return 'do some magic!'
