
#     *****    ******    *******   **         **
#    **   **   **   **   **         **   *   **
#    **        ******    *****       ** *** **
#    **   **   ** **     **           *** ***
#     *****    **   **   *******       *   *

"""
A class representing a table of activity shift patterns for the ProPeople shift types for crew activities.
"""

import pandas as pd
from datetime import date
import exception
from activity_date import ActivityDate


class ActivityDates:
    """
    A class representing a table of activity dates for the ProPeople shift types for crew activities.
    """

    ###########################
    #    I N I T I A L I Z E
    ###########################

    def __init__(self):
        """
        Initializing the activity date table class.
        """
        
        self.activity_dates_df = pd.DataFrame(columns=[
            "ID", 
            "ActivityID",
            "ActivityDate",
            "PersonID",
            "FromDate",
            "ToDate",
            "DurationInDays",
            "ShiftPattern",
            "ShiftCode",
            "DayCode",
            "Hours",
            "OriginalFromDate",
            "OriginalToDate",
            "OriginalShiftPattern"
            ])


    def __repr__(self) -> str:
        count = len(self.activity_dates_df)
        return f"Activity dates {count}"


    ############################
    #    P R O P E R T I E S
    ############################


    # ######################
    # #    M E T H O D S
    # ######################

    def add_activity_date(self, activity_date):
        """
        Add a activity date object to the table.

        Parameters:
        - activity_date (ActivityDate): A activity date object to be added to the table.
        """
        activity_date_id = len(self.activity_dates_df) + 1
        activity_date_dict = {
            "ID": activity_date_id,
            "ActivityID": activity_date.activity_id,
            "ActivityDate": activity_date.activity_date,
            "PersonID": activity_date.person_id,
            "FromDate": activity_date.from_date,
            "ToDate": activity_date.to_date,
            "DurationInDays": activity_date.duration_in_days,
            "ShiftPattern": activity_date.shift_pattern,
            "ShiftCode": activity_date.shift_code,
            "DayCode": activity_date.day_code,
            "Hours": activity_date.hours,
            "OriginalFromDate": activity_date.original_from_date,
            "OriginalToDate": activity_date.original_to_date,
            "OriginalShiftPattern": activity_date.original_shift_pattern
        }
        self.activity_dates_df = self.activity_dates_df.append(activity_date_dict, ignore_index=True)


    def list_activity_dates(self):
        """
        Iterate over all activity dates in the table and print their information.
        """
        if self.activity_dates_df.empty:
            print("No activity dates in the table.")
        else:
            print("List of activity dates:")
            print(self.activity_dates_df)


    def populate(self):
        """
        Fills the table with activity dates for the ProPeople shift types for crew activities.
        """
        self.activity_dates = []
        self.add_activity_date(
            ActivityDate(
                activity_id = 1,
                activity_date = date(2023, 11, 1),
                person_id = "KIMO",
                from_date = date(2023, 11, 1),
                to_date = date(2023, 11, 16),
                duration_in_days = 16,
                shift_pattern = "DDNNNNNNNDDDDDDD",
                shift_code = "D",
                day_code = "M",
                hours = 6.0,
                original_from_date = date(2023, 11, 3),
                original_to_date = date(2023, 11, 15),
                original_shift_pattern = "NNNNNNNDDDDDDD" ))
        self.add_activity_date(
            ActivityDate(
                activity_id = 2,
                activity_date = date(2023, 12, 1),
                person_id = "PAHE",
                from_date = date(2023, 12, 1),
                to_date = date(2023, 12, 24),
                duration_in_days = 24,
                shift_pattern = "DDDDDDDNNNNNNNDDDDDDDNNN",
                shift_code = "D",
                day_code = "M",
                hours = 6.0,
                original_from_date = date(2023, 12, 1),
                original_to_date = date(2023, 12, 24),
                original_shift_pattern = "DDDDDDDNNNNNNN" ))
