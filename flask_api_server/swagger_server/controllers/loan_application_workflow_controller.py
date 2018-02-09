import connexion
import six

from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server import util


def find_loan_application_workflow(loanAppId):  # noqa: E501
    """Get all Loan Application Workflow stages and tasks

    \&quot;This request retrieves Loan Application Workflow stages and tasks from Workflow.\&quot;  # noqa: E501

    :param loanAppId: ID of loan application
    :type loanAppId: str

    :rtype: None
    """
    return 'do some magic!'
