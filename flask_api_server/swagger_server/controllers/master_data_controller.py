import connexion
import six

from swagger_server.models.bank_results_object import BankResultsObject  # noqa: E501
from swagger_server.models.business_category_results_object import BusinessCategoryResultsObject  # noqa: E501
from swagger_server.models.business_file_type_code_results_object import BusinessFileTypeCodeResultsObject  # noqa: E501
from swagger_server.models.business_sub_category_results_object import BusinessSubCategoryResultsObject  # noqa: E501
from swagger_server.models.city_summary_results_object import CitySummaryResultsObject  # noqa: E501
from swagger_server.models.customer_category_results_object import CustomerCategoryResultsObject  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.models.operating_type_results_object import OperatingTypeResultsObject  # noqa: E501
from swagger_server.models.pin_code_summary_results_object import PinCodeSummaryResultsObject  # noqa: E501
from swagger_server.models.relationship_results_object import RelationshipResultsObject  # noqa: E501
from swagger_server.models.state_results_object import StateResultsObject  # noqa: E501
from swagger_server import util


def find_all_banks(offset=None, limit=None, query=None):  # noqa: E501
    """Get all Banks

    This request gets all Banks in CAS. # noqa: E501

    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: List[BankResultsObject]
    """
    return 'do some magic!'


def find_all_business_categories(offset=None, limit=None, query=None):  # noqa: E501
    """Get all BusinessCategories

    \&quot;This request gets all cities in CAS.\&quot;  # noqa: E501

    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: List[BusinessCategoryResultsObject]
    """
    return 'do some magic!'


def find_all_business_file_types(offset=None, limit=None, query=None):  # noqa: E501
    """Get all Business File Types

    This request gets all Business File Types in CAS. # noqa: E501

    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: List[BusinessFileTypeCodeResultsObject]
    """
    return 'do some magic!'


def find_all_business_sub_categories(offset=None, limit=None, query=None):  # noqa: E501
    """Get all BusinessSubCategories

    \&quot;This request gets all cities in CAS.\&quot;  # noqa: E501

    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: List[BusinessSubCategoryResultsObject]
    """
    return 'do some magic!'


def find_all_cities(offset=None, limit=None, query=None):  # noqa: E501
    """Get all cities

    \&quot;This request gets all cities in CAS.\&quot;  # noqa: E501

    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: List[CitySummaryResultsObject]
    """
    return 'do some magic!'


def find_all_customer_categories(offset=None, limit=None, query=None):  # noqa: E501
    """Get all CustomerCategories

    \&quot;This request gets all cities in CAS.\&quot;  # noqa: E501

    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: List[CustomerCategoryResultsObject]
    """
    return 'do some magic!'


def find_all_operating_types(offset=None, limit=None, query=None):  # noqa: E501
    """Get all operatingTypes

    \&quot;This request gets all cities in CAS.\&quot;  # noqa: E501

    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: List[OperatingTypeResultsObject]
    """
    return 'do some magic!'


def find_all_pin_codes(offset=None, limit=None, query=None):  # noqa: E501
    """Get all pin codes

    \&quot;This request gets all pin codes in CAS.\&quot;  # noqa: E501

    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: List[PinCodeSummaryResultsObject]
    """
    return 'do some magic!'


def find_all_relationships(offset=None, limit=None, query=None):  # noqa: E501
    """Get all Relationships

    \&quot;This request gets all cities in CAS.\&quot;  # noqa: E501

    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: List[RelationshipResultsObject]
    """
    return 'do some magic!'


def find_all_retailers(offset=None, limit=None, query=None):  # noqa: E501
    """Get all retailers

    \&quot;This request gets all retailers in CAS.\&quot;  # noqa: E501

    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: str

    :rtype: None
    """
    return 'do some magic!'


def find_all_states(offset=None, limit=None, query=None):  # noqa: E501
    """Get all States

    \&quot;This request gets all States in CAS.\&quot;  # noqa: E501

    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param query: search text to perform fuzzy search. 
    :type query: List[str]

    :rtype: List[StateResultsObject]
    """
    return 'do some magic!'


def get_pin_code_summary_by_city_id(offset=None, limit=None, cityId=None, stateId=None, cityName=None, stateName=None):  # noqa: E501
    """Get all pin codes summary by cityId

    \&quot;This request fetches pin code summary based on city Id. Basically this is a Pin code lookup service by city.\&quot;  # noqa: E501

    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int
    :param cityId: city id used for pin code look up.  
    :type cityId: int
    :param stateId: state id used for pin code look up.  
    :type stateId: int
    :param cityName: city name used for pin code look up.  
    :type cityName: str
    :param stateName: state name used for pin code look up.    
    :type stateName: str

    :rtype: List[PinCodeSummaryResultsObject]
    """
    return 'do some magic!'


def get_pin_code_summary_by_pin_code(pinCode, offset=None, limit=None):  # noqa: E501
    """Get all pin codes summary by pinCode

    \&quot;This request fetches pin code summary based on PinCode. Basically this is a Pin code lookup service.\&quot;  # noqa: E501

    :param pinCode: pin code that is passed for lookup
    :type pinCode: str
    :param offset: the offset from where the data has to be fetched. By default this is 0.
    :type offset: int
    :param limit: total number of records to be fetched.  If limit is sent as zero, just the metaData will be returned with total number of records. 
    :type limit: int

    :rtype: PinCodeSummaryResultsObject
    """
    return 'do some magic!'
