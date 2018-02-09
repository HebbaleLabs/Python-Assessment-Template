import connexion
import six

from swagger_server.models.business_bank_ac_summary_results_object import BusinessBankAcSummaryResultsObject  # noqa: E501
from swagger_server.models.business_bank_account_object import BusinessBankAccountObject  # noqa: E501
from swagger_server.models.business_bank_account_object_single import BusinessBankAccountObjectSingle  # noqa: E501
from swagger_server.models.business_bank_account_object_update import BusinessBankAccountObjectUpdate  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server import util


def add_business_bank_accounts(businessId, body):  # noqa: E501
    """Add a new Business Bank Account

    \&quot;This request saves one or many Business Bank Accounts in CAS.\&quot;  # noqa: E501

    :param businessId: Id of Business that needs to be updated
    :type businessId: str
    :param body: Business Bank account object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = BusinessBankAccountObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_business_bank_account(businessId, bankName, version, accountNumber, body):  # noqa: E501
    """Modify an existing Business Bank Account

    \&quot;This request updates a Customer Bank Account in CAS.\&quot;  # noqa: E501

    :param businessId: Business Pan
    :type businessId: str
    :param bankName: Bank Name
    :type bankName: str
    :param version: Current Version Number obtained before update
    :type version: int
    :param accountNumber: ID of Business Bank Account that needs to be updated. This is a combination of business, bank name and account number.
    :type accountNumber: int
    :param body: Business Bank Account object that needs to be modified in the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = BusinessBankAccountObjectUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_all_business_bank_accounts(businessId, offset=None, limit=None, query=None):  # noqa: E501
    """Get all Business Bank Accounts for  business

    \&quot;This request retrieves all Business Bank Accounts from CAS.\&quot;  # noqa: E501

    :param businessId: Id of Business that needs to be updated
    :type businessId: str
    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: BusinessBankAcSummaryResultsObject
    """
    return 'do some magic!'


def get_business_bank_account_by_id(businessId, bankName, accountNumber):  # noqa: E501
    """Find Business Bank Account by ID

    Returns an Customer # noqa: E501

    :param businessId: Business Id
    :type businessId: str
    :param bankName: Bank Name
    :type bankName: str
    :param accountNumber: ID of Business Bank Account that needs to be fetched
    :type accountNumber: int

    :rtype: BusinessBankAccountObjectSingle
    """
    return 'do some magic!'
