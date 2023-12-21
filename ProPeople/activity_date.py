
#     *****    ******    *******   **         **
#    **   **   **   **   **         **   *   **
#    **        ******    *****       ** *** **
#    **   **   ** **     **           *** ***
#     *****    **   **   *******       *   *

"""
The activity class contains properties for crew activities planned in ProPeople.
This data is gathered from the ProPeople API.
"""

import pandas as pd
from datetime import date, datetime
import exception
from activity_shift_patterns import ActivityShiftPatterns

class ActivityDate:
    """
    The activity date class contains properties for crew activities planned in ProPeople.
    """

    ###########################
    #    I N I T I A L I Z E
    ###########################

    def __init__(self,
        activity_id: int,
        activity_date: date,
        person_id: str,
        from_date: date,
        to_date: date,
        duration_in_days: int,
        shift_pattern: str,
        shift_code: str,
        day_code: str,
        hours: float,
        original_from_date: date,
        original_to_date: date,
        original_shift_pattern: str
    ):
        """
        Initializing the activity class.

        Args:
            activity_id (int, mandatory): Unique identification number for a given person in the ProPeople database.
            activity_date (date, mandatory): The actuall date for this activity day.
            person_id (str, mandatory): The person's unique Person id.
            from_date (date): The actuall start date for this activity.
            to_date (date): The actuall end date for this activity.
            duration_in_days (int): Number of days this activity lasts.
            shift_pattern (str): Shift pattern string to identify the combination of D (dayshifts) or a N (night shifts).
            shift_code (str): Shift code to identify if it is a D (dayshift) or a N (night shift).
            day_code (str): Day code to identify if it is a M (mobilization day), a W (normal working day) or a D (demobilization day).
            hours (float): Number of working hours as defined by the activity shift pattern and the day code.
            original_from_date (date): The start date originally planned for this activity.
            original_to_date (date): The end date originally planned for this activity.
            original_shift_pattern (str, mandatory): Text string defining the activity shift pattern. N represents night shift and D represents day shift.

        Raises:
            InvalidArgumentTypeError: One or more of the passed parameter vales have invalid type.
            InvalidArgumentValueError: One or more of the passed parameter vales are invalid.
        """
        if not isinstance(activity_id, int):
            raise exception.InvalidArgumentTypeError("The activity_id parameter must be an integer value!")
        if activity_id is None:
            raise exception.InvalidArgumentTypeError("The activity_id parameter must have a value!")
        if not isinstance(activity_date, date):
            raise exception.InvalidArgumentTypeError("The activity_date parameter must be a date value!")
        if activity_date is None:
            raise exception.InvalidArgumentTypeError("The activity_date parameter must have a value!")
        if not isinstance(person_id, str):
            raise exception.InvalidArgumentTypeError("The person_id parameter must be a string value!")
        if person_id is None:
            raise exception.InvalidArgumentTypeError("The person_id parameter must have a value!")
        if not isinstance(from_date, date):
            raise exception.InvalidArgumentTypeError("The from_date parameter must be a date value!")
        if not isinstance(to_date, date):
            raise exception.InvalidArgumentTypeError("The to_date parameter must be a date value!")
        if not isinstance(duration_in_days, int):
            raise exception.InvalidArgumentTypeError("The duration_in_days parameter must be an integer value!")
        if not isinstance(shift_pattern, str):
            raise exception.InvalidArgumentTypeError("The shift_pattern parameter must be a string value!")
        if not isinstance(shift_code, str):
            raise exception.InvalidArgumentTypeError("The shift_code parameter must be a string value!")
        if not isinstance(day_code, str):
            raise exception.InvalidArgumentTypeError("The day_code parameter must be a string value!")
        if not isinstance(hours, float):
            raise exception.InvalidArgumentTypeError("The hours parameter must be a float value!")
        if not isinstance(original_from_date, date):
            raise exception.InvalidArgumentTypeError("The original_from_date parameter must be a date value!")
        if not isinstance(original_to_date, date):
            raise exception.InvalidArgumentTypeError("The original_to_date parameter must be a date value!")
        if not isinstance(original_shift_pattern, str):
            raise exception.InvalidArgumentTypeError("The original_shift_pattern parameter must be a string value!")
        
        self.activity_id = activity_id
        self.activity_date = activity_date
        self.person_id = person_id
        self.from_date = from_date
        self.to_date = to_date
        self.duration_in_days = duration_in_days
        self.shift_pattern = shift_pattern
        self.shift_code = shift_code
        self.day_code = day_code
        self.hours = hours
        self.original_from_date = original_from_date
        self.original_to_date = original_to_date
        self.original_shift_pattern = original_shift_pattern


    def __repr__(self) -> str:
        return f"{self.activity_id} [{self.activity_date}] - {self.person_id}"


    ############################
    #    P R O P E R T I E S
    ############################


    # ######################
    # #    M E T H O D S
    # ######################

    def to_dataframe_row(self) -> pd.DataFrame:
        """
        Returns the activity date's properties as a Pandas DataFrame row.
        """
        data = {
            "ActivityID": [self.activity_id],
            "ActivityDate": [self.activity_date],
            "PersonID": [self.person_id],
            "FromDate": [self.from_date],
            "ToDate": [self.to_date],
            "DurationInDays": [self.duration_in_days],
            "ShiftPattern": [self.shift_pattern],
            "ShiftCode": [self.shift_code],
            "DayCode": [self.day_code],
            "Hours": [self.hours],
            "OriginalFromDate": [self.original_from_date],
            "OriginalToDate": [self.original_to_date],
            "OriginalShiftPattern": [self.original_shift_pattern],
        }
        return pd.DataFrame(data)
