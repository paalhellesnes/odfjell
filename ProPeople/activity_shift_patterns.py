
#     *****    ******    *******   **         **
#    **   **   **   **   **         **   *   **
#    **        ******    *****       ** *** **
#    **   **   ** **     **           *** ***
#     *****    **   **   *******       *   *

"""
A class representing a table of activity shift patterns for the ProPeople shift types for crew activities.
"""

import pandas as pd

import exception
from activity_shift_pattern import ActivityShiftPattern


class ActivityShiftPatterns:
    """
    A class representing a table of activity shift patterns for the ProPeople shift types for crew activities.
    """

    ###########################
    #    I N I T I A L I Z E
    ###########################

    def __init__(self):
        """
        Initializing the activity shift pattern table class.
        """
        
        self.patterns_df = pd.DataFrame(columns=['ID', 'ShiftPatternID', 'ShiftPatternCode', 'ShiftPatternDescription', 'ShiftPatternDays', 'ShiftPattern', 'MobilizationHours', 'WorkHours', 'DemobilizationHours'])


    def __repr__(self) -> str:
        count = len(self.patterns_df)
        return f"Activity shift patterns {count}"


    ############################
    #    P R O P E R T I E S
    ############################


    # ######################
    # #    M E T H O D S
    # ######################

    def add_pattern(self, pattern):
        """
        Add a activity shift pattern object to the table.

        Parameters:
        - pattern (ActivityShiftPattern): A activity shift pattern object to be added to the table.
        """
        pattern_id = len(self.patterns_df) + 1
        pattern_dict = {
            'ID': pattern_id,
            'ShiftPatternID': pattern.shift_pattern_id, # shift_pattern_id
            'ShiftPatternCode': pattern.shift_pattern_code,
            'ShiftPatternDescription': pattern.shift_pattern_description,
            'ShiftPatternDays': pattern.shift_pattern_days,
            'ShiftPattern': pattern.shift_pattern,
            'MobilizationHours': pattern.mobilization_hours,
            'WorkHours': pattern.work_hours,
            'DemobilizationHours': pattern.demobilization_hours
        }
        self.patterns_df = self.patterns_df.append(pattern_dict, ignore_index=True)


    def get_shift_pattern_by_id(self, shift_pattern_id):
        """
        Retreive a activity shift pattern string from the table with a given shift pattern ID.

        Parameters:
        - shift_pattern_id (int): The shift pattern ID for which we wish to retreive the activity shift pattern string.
        """
        shift_pattern_series = self.patterns_df.loc[self.patterns_df['ShiftPatternID'] == shift_pattern_id, 'ShiftPattern']
        if not shift_pattern_series.empty:
            return shift_pattern_series.iloc[0]
        return None


    def get_shift_pattern_by_code(self, shift_pattern_code):
        """
        Retreive a activity shift pattern string from the table with a given shift pattern code.

        Parameters:
        - shift_pattern_code (str): The shift pattern code for which we wish to retreive the activity shift pattern string.
        """
        shift_pattern_series = self.patterns_df.loc[self.patterns_df['ShiftPatternCode'] == shift_pattern_code, 'ShiftPattern']
        if not shift_pattern_series.empty:
            return shift_pattern_series.iloc[0]
        return None



        # print(f"{type(pattern)}")
        # shift_pattern_idx = int(pattern['ShiftPatternID']),
        # shift_pattern_code = str(pattern['ShiftPatternCode']),
        # shift_pattern_description = str(pattern.ShiftPatternDescription),
        # shift_pattern_days = int(pattern.ShiftPatternDays),
        # shift_pattern = str(pattern.ShiftPattern),
        # mobilization_hours = float(pattern.MobilizationHours),
        # work_hours = float(pattern.WorkHours),
        # demobilization_hours = float(pattern.DemobilizationHours)

        # activity_shift_pattern = ActivityShiftPattern(
        #     shift_pattern_id = int(pattern.ShiftPatternID),
        #     shift_pattern_code = str(pattern.ShiftPatternCode),
        #     shift_pattern_description = str(pattern.ShiftPatternDescription),
        #     shift_pattern_days = int(pattern.ShiftPatternDays),
        #     shift_pattern = str(pattern.ShiftPattern),
        #     mobilization_hours = float(pattern.MobilizationHours),
        #     work_hours = float(pattern.WorkHours),
        #     demobilization_hours = float(pattern.DemobilizationHours)
        # )

        # return activity_shift_pattern if not pattern.empty else None


    def get_pattern_by_code(self, shift_pattern_code):
        """
        Retreive a activity shift pattern object from the table with a given shift pattern code.

        Parameters:
        - shift_pattern_code (str): The shift pattern code for which we wish to retreive the activity shift pattern object.
        """
        pattern = self.patterns_df.loc[self.patterns_df['ShiftPatternCode'] == shift_pattern_code]
        return pattern if not pattern.empty else None
    

    def list_patterns(self):
        """
        Iterate over all activity shift patterns in the table and print their information.
        """
        if self.patterns_df.empty:
            print("No activity shift patterns in the table.")
        else:
            print("List of activity shift patterns:")
            print(self.patterns_df)


    def populate(self):
        """
        Fills the table with activity shift patterns for the ProPeople shift types for crew activities.
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

