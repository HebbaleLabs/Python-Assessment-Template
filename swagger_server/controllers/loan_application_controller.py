import connexion
import six

from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.models.loan_application_object import LoanApplicationObject  # noqa: E501
from swagger_server.models.loan_application_object_update import LoanApplicationObjectUpdate  # noqa: E501
from swagger_server.models.loan_application_results_object import LoanApplicationResultsObject  # noqa: E501
from swagger_server.models.loan_application_summary_results_object import LoanApplicationSummaryResultsObject  # noqa: E501
from swagger_server import util


def add_loan_application(body):  # noqa: E501
    """Add a new Loan Application

    \&quot;This request saves a Loan Application in CAS.\&quot;  # noqa: E501

    :param body: Loan Application that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = LoanApplicationObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_loan_application(version, loanApplicationId, body):  # noqa: E501
    """Modify an existing Loan Application

    \&quot;This request updates a Business in CAS.\&quot;  # noqa: E501

    :param version: Current Version Number obtained before update
    :type version: int
    :param loanApplicationId: ID of Loan application that needs to be updated
    :type loanApplicationId: str
    :param body: Loan Application object that needs to be modified in the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = LoanApplicationObjectUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_loan_applications(offset=None, limit=None, query=None):  # noqa: E501
    """Get all Loan Applications

    \&quot;This request retrieves Loan Applications from CAS.\&quot;  # noqa: E501

    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: List[LoanApplicationSummaryResultsObject]
    """
    return 'do some magic!'


def get_loan_application_by_id(loanApplicationId):  # noqa: E501
    """Find Loan Application by ID

    Returns a Business # noqa: E501

    :param loanApplicationId: ID of loan application that needs to be fetched
    :type loanApplicationId: str

    :rtype: LoanApplicationResultsObject
    """
    return 'do some magic!'
