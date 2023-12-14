
#     *****    ******    *******   **         **
#    **   **   **   **   **         **   *   **
#    **        ******    *****       ** *** **
#    **   **   ** **     **           *** ***
#     *****    **   **   *******       *   *

"""
The activity shift pattern class contains additional properties for the ProPeople shift types for crew activities.
"""

import pandas as pd
from datetime import date
import exception


class ActivityShiftPattern:
    """
    The activity shift pattern class contains additional properties for the ProPeople shift types for crew activities.

    Attributes:
    - shift_pattern_id (int): Unique ProPeople identification number for the activity shift pattern.
    - shift_pattern_code (str): Unique ProPeople identification code for the activity shift pattern.
    - shift_pattern_description (str): Short text describing the activity shift pattern.
    - shift_pattern_days (int): Number of days defined by the activity shift pattern.
    - shift_pattern (str): Text string defining the activity shift pattern. N represents night shift and D represents day shift.
    - start_date (date): The date that the activity shift pattern will start. The pattern will then repeat indefinitely into the future.
    - mobilization_hours (int): Number of working hours in the day of mobilization (first day of the activity) as defined by the activity shift pattern.
    - work_hours (int): Number of normal working hours as defined by the activity shift pattern.
    - demobilization_hours (int): Number of working hours in the day of demobilization (last day of the activity) as defined by the activity shift pattern.
    """

    ###########################
    #    I N I T I A L I Z E
    ###########################

    def __init__(self,
        shift_pattern_id: int,
        shift_pattern_code: str,
        shift_pattern_description: str,
        shift_pattern_days: int,
        shift_pattern: str,
        start_date: date,
        mobilization_hours: int,
        work_hours: int,
        demobilization_hours: int
    ):
        """
        Initializing the activity shift pattern class class.

        Args:
            shift_pattern_id (int, mandatory): Unique ProPeople identification number for the activity shift pattern.
            shift_pattern_code (str, mandatory): Unique ProPeople identification code for the activity shift pattern.
            shift_pattern_description (str, mandatory): Short text describing the activity shift pattern.
            shift_pattern_days (int, mandatory): Number of days defined by the activity shift pattern.
            shift_pattern (str, mandatory): Text string defining the activity shift pattern. N represents night shift and D represents day shift.
            start_date (date, mandatory): The date that the activity shift pattern will start. The pattern will then repeat indefinitely into the future.
            mobilization_hours (int, mandatory): Number of working hours in the day of mobilization (first day of the activity) as defined by the activity shift pattern.
            work_hours (int, mandatory): Number of normal working hours as defined by the activity shift pattern.
            demobilization_hours (int, mandatory): Number of working hours in the day of demobilization (last day of the activity) as defined by the activity shift pattern.

        Raises:
            InvalidArgumentTypeError: One or more of the passed parameter vales have invalid type.
            InvalidArgumentValueError: One or more of the passed parameter vales are invalid.
        """
        if not isinstance(shift_pattern_id, int):
            raise exception.InvalidArgumentTypeError("The shift_pattern_id parameter must be an integer value!")
        if not shift_pattern_id:
            raise exception.InvalidArgumentTypeError("The shift_pattern_id parameter must have a value!")
        if not isinstance(shift_pattern_code, str):
            raise exception.InvalidArgumentTypeError("The shift_pattern_code parameter must be a string value!")
        if not shift_pattern_code:
            raise exception.InvalidArgumentTypeError("The shift_pattern_code parameter must have a value!")
        if not isinstance(shift_pattern_description, str):
            raise exception.InvalidArgumentTypeError("The shift_pattern_description parameter must be a string value!")
        if not shift_pattern_description:
            raise exception.InvalidArgumentTypeError("The shift_pattern_description parameter must have a value!")
        if not isinstance(shift_pattern_days, int):
            raise exception.InvalidArgumentTypeError("The shift_pattern_days parameter must be an integer value!")
        if not shift_pattern_days:
            raise exception.InvalidArgumentTypeError("The shift_pattern_days parameter must have a value!")
        if not isinstance(shift_pattern, str):
            raise exception.InvalidArgumentTypeError("The shift_pattern parameter must be a string value!")
        if not shift_pattern:
            raise exception.InvalidArgumentTypeError("The shift_pattern parameter must have a value!")
        if not isinstance(start_date, date):
            raise exception.InvalidArgumentTypeError("The start_date parameter must be a date value!")
        if not start_date:
            raise exception.InvalidArgumentTypeError("The start_date parameter must have a value!")
        if not isinstance(mobilization_hours, int):
            raise exception.InvalidArgumentTypeError("The mobilization_hours parameter must be an integer value!")
        if not mobilization_hours:
            raise exception.InvalidArgumentTypeError("The mobilization_hours parameter must have a value!")
        if not isinstance(work_hours, int):
            raise exception.InvalidArgumentTypeError("The work_hours parameter must be an integer value!")
        if not work_hours:
            raise exception.InvalidArgumentTypeError("The work_hours parameter must have a value!")
        if not isinstance(demobilization_hours, int):
            raise exception.InvalidArgumentTypeError("The demobilization_hours parameter must be an integer value!")
        if not demobilization_hours:
            raise exception.InvalidArgumentTypeError("The demobilization_hours parameter must have a value!")
        
        self.shift_pattern_id = shift_pattern_id
        self.shift_pattern_code = shift_pattern_code
        self.shift_pattern_description = shift_pattern_description
        self.shift_pattern_days = shift_pattern_days
        self.shift_pattern = shift_pattern
        self.start_date = start_date
        self.mobilization_hours = mobilization_hours
        self.work_hours = work_hours
        self.demobilization_hours = demobilization_hours


    def __repr__(self) -> str:
        #return f"{self.shift_pattern_code} - {self.shift_pattern} starting at {self.start_date}"
        return f"{self.shift_pattern_code} - {self.shift_pattern}"


    ############################
    #    P R O P E R T I E S
    ############################


    # ######################
    # #    M E T H O D S
    # ######################

    def to_dataframe_row(self) -> pd.DataFrame:
        """
        Returns the activity shift pattern's properties as a Pandas DataFrame row.
        """
        data = {
            "ShiftPatternID": [self.shift_pattern_id],
            "ShiftPatternCode": [self.shift_pattern_code],
            "ShiftPatternDescription": [self.shift_pattern_description],
            "ShiftPatternDays": [self.shift_pattern_days],
            "ShiftPattern": [self.shift_pattern],
            "StartDate": [self.start_date],
            "MobilizationHours": [self.mobilization_hours],
            "WorkHours": [self.work_hours],
            "DemobilizationHours": [self.demobilization_hours],
        }
        return pd.DataFrame(data)