import connexion
import six

from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.models.loan_application_notes_array import LoanApplicationNotesArray  # noqa: E501
from swagger_server.models.loan_application_notes_object import LoanApplicationNotesObject  # noqa: E501
from swagger_server import util


def add_loan_application_notes(loanAppId, body):  # noqa: E501
    """Add a new Loan Application Notes

    \&quot;This request saves a Loan Application Notes in CAS.\&quot;  # noqa: E501

    :param loanAppId: ID of loan application
    :type loanAppId: str
    :param body: Loan Application that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = LoanApplicationNotesObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_loan_application_notes(loanAppId, noteId, version, body):  # noqa: E501
    """Add a new Loan Application Notes

    \&quot;This request saves a Loan Application Notes in CAS.\&quot;  # noqa: E501

    :param loanAppId: ID of loan application
    :type loanAppId: str
    :param noteId: Note ID of loan application Notes
    :type noteId: int
    :param version: current version
    :type version: int
    :param body: Loan Application that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = LoanApplicationNotesObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_loan_app_notes_by_id(loanAppId, noteId):  # noqa: E501
    """Get all Loan Application Notes

    \&quot;This request retrieves Loan Applications from CAS.\&quot;  # noqa: E501

    :param loanAppId: ID of loan application
    :type loanAppId: str
    :param noteId: Note ID of loan application Notes
    :type noteId: int

    :rtype: LoanApplicationNotesObject
    """
    return 'do some magic!'


def find_loan_application_notes(loanAppId, offset=None, limit=None, query=None):  # noqa: E501
    """Get all Loan Application Notes

    \&quot;This request retrieves Loan Applications from CAS.\&quot;  # noqa: E501

    :param loanAppId: ID of loan application
    :type loanAppId: str
    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: LoanApplicationNotesArray
    """
    return 'do some magic!'
