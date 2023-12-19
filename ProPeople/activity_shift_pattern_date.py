
#     *****    ******    *******   **         **
#    **   **   **   **   **         **   *   **
#    **        ******    *****       ** *** **
#    **   **   ** **     **           *** ***
#     *****    **   **   *******       *   *

"""
The activity shift pattern date class contains additional properties for the ProPeople shift types for crew activities.
"""

import pandas as pd
import datetime
from datetime import date
import exception


class ActivityShiftPatternDate:
    """
    The activity shift pattern date class contains the properties of a given activity shift pattern on a give date.
    These include the shift (night or day), mobilization hours, work hours, and demobilization hours.

    Attributes:
    - date (date): The date for the activity.
    - shift_pattern_id (int): Unique ProPeople identification number for the activity shift pattern.
    - shift (str): A string character defining the shift. N represents night shift and D represents day shift.
    - mobilization_hours (int): Number of working hours in the day of mobilization (first day of the activity) as defined by the activity shift pattern.
    - work_hours (int): Number of normal working hours as defined by the activity shift pattern.
    - demobilization_hours (int): Number of working hours in the day of demobilization (last day of the activity) as defined by the activity shift pattern.
    """

    ###########################
    #    I N I T I A L I Z E
    ###########################

    def __init__(self,
        date: datetime.date,
        shift_pattern_id: int,
        shift: str,
        mobilization_hours: float,
        work_hours: float,
        demobilization_hours: float
    ):
        """
        Initializing the activity shift pattern date class.

        Args:
            date (date, mandatory): The date for the activity.
            shift_pattern_id (int, mandatory): Unique ProPeople identification number for the activity shift pattern.
            shift (str, mandatory): A string character defining the shift. N represents night shift and D represents day shift.
            mobilization_hours (float, mandatory): Number of working hours in the day of mobilization (first day of the activity) as defined by the activity shift pattern.
            work_hours (float, mandatory): Number of normal working hours as defined by the activity shift pattern.
            demobilization_hours (float, mandatory): Number of working hours in the day of demobilization (last day of the activity) as defined by the activity shift pattern.

        Raises:
            InvalidArgumentTypeError: One or more of the passed parameter vales have invalid type.
            InvalidArgumentValueError: One or more of the passed parameter vales are invalid.
        """
        if not isinstance(date, datetime.date):
            raise exception.InvalidArgumentTypeError("The date parameter must be a date value!")
        if date is None:
            raise exception.InvalidArgumentTypeError("The date parameter must have a value!")
        if not isinstance(shift_pattern_id, int):
            raise exception.InvalidArgumentTypeError("The shift_pattern_id parameter must be an integer value!")
        if shift_pattern_id is None:
            raise exception.InvalidArgumentTypeError("The shift_pattern_id parameter must have a value!")
        if not isinstance(shift, str):
            raise exception.InvalidArgumentTypeError("The shift parameter must be a string value!")
        if shift is None:
            raise exception.InvalidArgumentTypeError("The shift parameter must have a value!")
        if not isinstance(mobilization_hours, float):
            raise exception.InvalidArgumentTypeError("The mobilization_hours parameter must be a float value!")
        if mobilization_hours is None:
            raise exception.InvalidArgumentTypeError("The mobilization_hours parameter must have a value!")
        if not isinstance(work_hours, float):
            raise exception.InvalidArgumentTypeError("The work_hours parameter must be a float value!")
        if work_hours is None:
            raise exception.InvalidArgumentTypeError("The work_hours parameter must have a value!")
        if not isinstance(demobilization_hours, float):
            raise exception.InvalidArgumentTypeError("The demobilization_hours parameter must be a float value!")
        if demobilization_hours is None:
            raise exception.InvalidArgumentTypeError("The demobilization_hours parameter must have a value!")

        self.date = date
        self.shift_pattern_id = shift_pattern_id
        self.shift = shift
        self.mobilization_hours = mobilization_hours
        self.work_hours = work_hours
        self.demobilization_hours = demobilization_hours


    def __repr__(self) -> str:
        # return f"({self.date},{self.shift_pattern_id}) - {self.shift}, {self.mobilization_hours}, {self.work_hours}, {self.demobilization_hours}"
        return f"({self.shift_pattern_id}) - {self.shift}, {self.mobilization_hours}, {self.work_hours}, {self.demobilization_hours}"


    ############################
    #    P R O P E R T I E S
    ############################


    # ######################
    # #    M E T H O D S
    # ######################

    def to_dataframe_row(self) -> pd.DataFrame:
        """
        Returns the activity shift pattern date's properties as a Pandas DataFrame row.
        """
        data = {
            "Date": [self.date],
            "ShiftPatternID": [self.shift_pattern_id],
            "Shift": [self.shift],
            "MobilizationHours": [self.mobilization_hours],
            "WorkHours": [self.work_hours],
            "DemobilizationHours": [self.demobilization_hours],
        }
        return pd.DataFrame(data)
