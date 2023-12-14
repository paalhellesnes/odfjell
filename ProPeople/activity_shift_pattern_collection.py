
#     *****    ******    *******   **         **
#    **   **   **   **   **         **   *   **
#    **        ******    *****       ** *** **
#    **   **   ** **     **           *** ***
#     *****    **   **   *******       *   *

"""
A class representing a collection of activity shift patterns for the ProPeople shift types for crew activities.
"""

import pandas as pd

import exception
from activity_shift_pattern import ActivityShiftPattern


class ActivityShiftPatternCollection:
    """
    A class representing a collection of activity shift patterns for the ProPeople shift types for crew activities.
    """

    ###########################
    #    I N I T I A L I Z E
    ###########################

    def __init__(self):
        """
        Initializing the activity shift pattern class class.
        """
        
        self.patterns = []


    def __repr__(self) -> str:
        len = self.patterns.__len__()
        return f"Activity shift patterns {len}"


    ############################
    #    P R O P E R T I E S
    ############################


    # ######################
    # #    M E T H O D S
    # ######################

    def add_pattern(self, pattern):
        """
        Add a activity shift pattern object to the collection.

        Parameters:
        - pattern (ActivityShiftPattern): A activity shift pattern object to be added to the collection.
        """
        self.patterns.append(pattern)


    def iterate_over_patterns(self):
        """
        Iterate over all activity shift patterns in the collection and print their information.
        """
        for index, pattern in enumerate(self.patterns, start=1):
            print(f"Activity Shift Pattern {index} - {pattern.shift_pattern_code}:")
            print(f"  Shift Pattern ID: {pattern.shift_pattern_id}")
            print(f"  Shift Pattern Code: {pattern.shift_pattern_code}")
            print(f"  Shift Pattern Description: {pattern.shift_pattern_description}")
            print(f"  Shift Pattern Days: {pattern.shift_pattern_days} days")
            print(f"  Shift Pattern: {pattern.shift_pattern}")
            print(f"  Mobilization Hours: {pattern.mobilization_hours} hours")
            print(f"  Work Hours: {pattern.work_hours} hours")
            print(f"  Demobilization Hours: {pattern.demobilization_hours} hours")
            print("---")


    def to_dataframe(self) -> pd.DataFrame:
        """
        Convert the activity shift pattern collection to a Pandas DataFrame.

        Returns:
        pandas.DataFrame: A Pandas DataFrame representing the collection of activity shift patterns.
        """
        data = {"ShiftPatternID": [], "ShiftPatternCode": [], "ShiftPatternDescription": [], "ShiftPatternDays": [], "ShiftPattern": [], "MobilizationHours": [], "WorkHours": [], "DemobilizationHours": []}
        for pattern in self.patterns:
            data["ShiftPatternID"].append(pattern.shift_pattern_id)
            data["ShiftPatternCode"].append(pattern.shift_pattern_code)
            data["ShiftPatternDescription"].append(pattern.shift_pattern_description)
            data["ShiftPatternDays"].append(pattern.shift_pattern_days)
            data["ShiftPattern"].append(pattern.shift_pattern)
            data["MobilizationHours"].append(pattern.mobilization_hours)
            data["WorkHours"].append(pattern.work_hours)
            data["DemobilizationHours"].append(pattern.demobilization_hours)

        return pd.DataFrame(data)


    def populate(self):
        """
        Fills the collection with activity shift patterns for the ProPeople shift types for crew activities.
        """
        self.patterns = []
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 2,
                shift_pattern_code = "D7N7",
                shift_pattern_description = "First 7 dayshift, then 7 nightshift. 6 hours on mobilization day, then 12 hours next shifts and 6 hours on demobilization day.",
                shift_pattern_days = 14,
                shift_pattern = "DDDDDDDNNNNNNN",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 3,
                shift_pattern_code = "N7D7",
                shift_pattern_description = "First 7 nightshift, then 7 dayshift. 6 hours on mobilization day, then 12 hours next shifts and 6 hours on demobilization day.",
                shift_pattern_days = 14,
                shift_pattern = "NNNNNNNDDDDDDD",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 6,
                shift_pattern_code = "D",
                shift_pattern_description = "Only dayshift. 6 hours on mob day, then 12 hours next shifts, then 6 hours demob day.",
                shift_pattern_days = 1,
                shift_pattern = "D",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 7,
                shift_pattern_code = "N",
                shift_pattern_description = "Only nightshift. 6 hours on mob day, then 12 hours next shifts, then 6 hours demob day.",
                shift_pattern_days = 1,
                shift_pattern = "N",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 26,
                shift_pattern_code = "D(H9-12-9)",
                shift_pattern_description = "Only dayshift. 9 hours on mob day, then 12 hours next shifts, then 9 hours demob day.",
                shift_pattern_days = 1,
                shift_pattern = "D",
                mobilization_hours = 9.0,
                work_hours = 12.0,
                demobilization_hours = 9.0 ))
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 27,
                shift_pattern_code = "D(H9-12-0)",
                shift_pattern_description = "Only dayshift. 9 hours on mob day, then 12 hours next shifts, then 0 hours demob day.",
                shift_pattern_days = 1,
                shift_pattern = "D",
                mobilization_hours = 9.0,
                work_hours = 12.0,
                demobilization_hours = 0.0 ))
        
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 45,
                shift_pattern_code = "D14N7",
                shift_pattern_description = "First 14 dayshift, then 7 nightshift. 6 hours on mob day, then 12 hours next shifts, then 6 hours demob day.",
                shift_pattern_days = 21,
                shift_pattern = "DDDDDDDDDDDDDDNNNNNNN",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 46,
                shift_pattern_code = "N14D7",
                shift_pattern_description = "First 14 nightshift, then 7 dayshift. 6 hours on mob day, then 12 hours next shifts, then 6 hours demob day.",
                shift_pattern_days = 21,
                shift_pattern = "NNNNNNNNNNNNNNDDDDDDD",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 47,
                shift_pattern_code = "D7N14",
                shift_pattern_description = "First 7 dayshift, then 14 nightshift. 6 hours on mob day, then 12 hours next shifts, then 6 hours demob day.",
                shift_pattern_days = 21,
                shift_pattern = "DDDDDDDNNNNNNNNNNNNNN",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 48,
                shift_pattern_code = "N7D14",
                shift_pattern_description = "First 7 nightshift, then 14 dayshift. 6 hours on mob day, then 12 hours next shifts, then 6 hours demob day.",
                shift_pattern_days = 21,
                shift_pattern = "NNNNNNNDDDDDDDDDDDDDD",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 65,
                shift_pattern_code = "D14N14",
                shift_pattern_description = "First 14 dayshift, then 14 nightshift. 6 hours on mob day, then 12 hours next shifts, then 6 hours demob day.",
                shift_pattern_days = 28,
                shift_pattern = "DDDDDDDDDDDDDDNNNNNNNNNNNNNN",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 66,
                shift_pattern_code = "N14D14",
                shift_pattern_description = "First 14 nightshift, then 14 dayshift. 6 hours on mob day, then 12 hours next shifts, then 6 hours demob day.",
                shift_pattern_days = 28,
                shift_pattern = "NNNNNNNNNNNNNNDDDDDDDDDDDDDD",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 85,
                shift_pattern_code = "Sick/Leave OWS 8,7 H 4/4 Rota",
                shift_pattern_description = "Only dayshift (but does we want that?do we use it Yanira ?). 8,7 hours all shifts.",
                shift_pattern_days = 1,
                shift_pattern = "D",
                mobilization_hours = 8.7,
                work_hours = 8.7,
                demobilization_hours = 8.7 ))
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 86,
                shift_pattern_code = "Sick/Leave OWS 7,8 H 4/5 Rota",
                shift_pattern_description = "Only dayshift (but does we want that?do we use it Yanira ?). 7,8 hours all shifts.",
                shift_pattern_days = 1,
                shift_pattern = "D",
                mobilization_hours = 7.8,
                work_hours = 7.8,
                demobilization_hours = 7.8 ))
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 105,
                shift_pattern_code = "Sick/Leave C-Pool 4 H",
                shift_pattern_description = "Only dayshift (but does we want that?do we use it Yanira ?). 4 hours all shifts.",
                shift_pattern_days = 1,
                shift_pattern = "D",
                mobilization_hours = 4.0,
                work_hours = 4.0,
                demobilization_hours = 4.0 ))
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 145,
                shift_pattern_code = "Sick/Leave MODU-PDR & OWS Rota",
                shift_pattern_description = "Only dayshift. 6 hours on mob day, then 12 hours next shifts, then 6 hours demob day.",
                shift_pattern_days = 1,
                shift_pattern = "D",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))
        self.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 186,
                shift_pattern_code = "D(H12-12-9)",
                shift_pattern_description = "Only dayshift. 12 hours on mob day, then 12 hours next shifts, then 9 hours demob day.",
                shift_pattern_days = 1,
                shift_pattern = "D",
                mobilization_hours = 12.0,
                work_hours = 12.0,
                demobilization_hours = 9.0 ))

