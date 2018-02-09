import connexion
import six

from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.models.loan_application_tasks_array import LoanApplicationTasksArray  # noqa: E501
from swagger_server.models.loan_application_tasks_object import LoanApplicationTasksObject  # noqa: E501
from swagger_server import util


def add_loan_application_tasks(loanAppId, body):  # noqa: E501
    """Add a new Loan Application Task

    \&quot;This request saves a Loan Application Task in CAS.\&quot;  # noqa: E501

    :param loanAppId: ID of loan application
    :type loanAppId: str
    :param body: Loan Application Task that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = LoanApplicationTasksObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_loan_application_task(body):  # noqa: E501
    """Edit a Loan Application Task

    \&quot;This request modifies a Loan Application Tasks in CAS.\&quot;  # noqa: E501

    :param body: Loan Application Task that needs to be modified in the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = LoanApplicationTasksObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_loan_application_tasks(loanAppId, offset=None, limit=None, query=None):  # noqa: E501
    """Get all Loan Application Tasks

    \&quot;This request retrieves Loan Application Tasks from CAS.\&quot;  # noqa: E501

    :param loanAppId: ID of loan application
    :type loanAppId: str
    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: LoanApplicationTasksArray
    """
    return 'do some magic!'
