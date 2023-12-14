
#     *****    ******    *******   **         **
#    **   **   **   **   **         **   *   **
#    **        ******    *****       ** *** **
#    **   **   ** **     **           *** ***
#     *****    **   **   *******       *   *

"""
The main application for creating the activity shift pattern date table for the ProPeople shift types for crew activities.
"""

import pandas as pd
import datetime
import exception


################
#    M A I N
################


##########################
#    F U N C T I O N S
##########################

tests.test_ActivityShiftPatternDate_init()






##############################################################
#       A Z U R E   D E L T A   L A K E   S T O R A G E
#             F O R    V I S U A L   S T U D I O
# -----------------------------------------------------------
#  Comment out this code if running as notebook in Synapse
##############################################################

def save_dataframe_to_delta_lake(data: pd.DataFrame, partition_column: str, merge_condition: str, full_delta_lake_path: str, loading_type: str) -> str:
    """
    Stores a given Pandas DataFrame to a full Azure Delta Lake path (folder+entity).

    Args:
        data (pd.DataFrame): Input data as a Pandas DataFrame.
        partition_column (str): Column in the DataFrame used for partitioning.
        merge_condition (str): Condition for merging new data with existing data.
        full_delta_lake_path (str): Full path to the Delta Lake (including entity name).
        loading_type (str): Loading operation type; 'initial', 'full', 'delta'.

    Returns:
        Status message. Example: 'Input data Pandas DataFrame is empty - no new data stored to Azure Delta Lake'

    Raises:
        InvalidArgumentTypeError: One or more parameters have invalid type.
        InvalidArgumentValueError: One or more parameters have invalid value.
        DataConversionError: Failed to to create a Spark DataFrame from the given Pandas DataFrame.
    """
    # logging.debug(f"('{partition_column}','{merge_condition}','{full_delta_lake_path}','{loading_type}')")
    if not isinstance(data, pd.DataFrame):
        raise exception.InvalidArgumentTypeError(f"The data parameter must be a Pandas DataFrame value type, the given value '{data}' is of type {type(data)}")
    if partition_column and not isinstance(partition_column, str):
        raise exception.InvalidArgumentTypeError(f"The partition_column parameter must be a string value type, the given value '{partition_column}' is of type {type(partition_column)}")
    if not isinstance(merge_condition, str):
        raise exception.InvalidArgumentTypeError(f"The merge_condition parameter must be a string value type, the given value '{merge_condition}' is of type {type(merge_condition)}")
    if not isinstance(full_delta_lake_path, str):
        raise exception.InvalidArgumentTypeError(f"The folder parameter must be a string value type, the given value '{full_delta_lake_path}' is of type {type(full_delta_lake_path)}")
    if not isinstance(loading_type, str):
        raise exception.InvalidArgumentTypeError(f"The loading_type parameter must be a string value type, the given value '{loading_type}' is of type {type(loading_type)}")
    if not loading_type in ["initial", "full", "delta"]:
        raise exception.InvalidArgumentValueError(f"The loading_type parameter must have one of the following values; 'initial', 'full', 'delta', the given value is '{loading_type}'")

    if data.empty:
        return "Pandas DataFrame is empty - no new data saved to Azure Delta Lake"

    entity_name = utility.extract_entity_name_from_full_path(full_delta_lake_path)
    data.to_csv(f"UnitTest/{entity_name}.csv", index=False)
    return "Pandas DataFrame saved OK"


def get_last_modified_datetime_from_delta_lake(full_delta_lake_path: str, last_modified_datetime_column: str, default_value: str = "2000.01.01") -> str:
    """
    Retreives the last modified date of a given delta lake file.

    Args:
        delta_lake_file_path (str): Full path to the delta lake folder.
        delta_lake_file (str): Name of the delta lake file.
        last_modified_datetime_column (str): Default returned data if extracting last modified date from given delta lake file fails. Example: '2010.01.11'

    Raises:
        TypeError: One or more of the passed parameter vales have invalid type.
    """
    # logging.debug(f"('{full_delta_lake_path}','{last_modified_datetime_column}','{default_value}')")
    if not type(full_delta_lake_path) is str:
        raise TypeError(f"the full_delta_lake_path argument must be a value of string type, the given value ({type(full_delta_lake_path)}) = '{full_delta_lake_path}' is invalid")
    if not type(last_modified_datetime_column) is str:
        raise TypeError(f"the last_modified_datetime_column argument must be a value of string type, the given value ({type(last_modified_datetime_column)}) = '{last_modified_datetime_column}' is invalid")
    if not type(default_value) is str:
        raise TypeError(f"the default_value argument must be a value of string type, the given value ({type(default_value)}) = '{default_value}' is invalid")

    return default_value


