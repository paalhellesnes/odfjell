import unittest
import pandas as pd
from datetime import date

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from activity_shift_pattern import ActivityShiftPattern
from activity_shift_pattern_collection import ActivityShiftPatternCollection


class ProPeopleActivityShiftPatternCollectionTestCase(unittest.TestCase):


    def test_ActivityShiftPatternCollection_init(self):
        propeople_activity_shift_pattern_collection = ActivityShiftPatternCollection()

        assert isinstance(propeople_activity_shift_pattern_collection, ActivityShiftPatternCollection), f"The ProPeople activity shift pattern collection object is expected to be of class ActivityShiftPatternCollection and not '{type(ActivityShiftPatternCollection).__name__}'"


    def test_ActivityShiftPatternCollection_repr(self):
        expected_repr = "Activity shift patterns 0"

        propeople_activity_shift_pattern_collection = ActivityShiftPatternCollection()

        assert propeople_activity_shift_pattern_collection.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activity_shift_pattern_collection.__repr__()}'"


    def test_ActivityShiftPatternCollection_add_pattern(self):
        expected_repr = "Activity shift patterns 2"

        propeople_activity_shift_pattern_collection = ActivityShiftPatternCollection()

        propeople_activity_shift_pattern_collection.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 2,
                shift_pattern_code = "D7N7",
                shift_pattern_description = "First 7 dayshift, then 7 nightshift. 6 hours on mobilization day, then 12 hours next shifts and 6 hours on demobilization day.",
                shift_pattern_days = 14,
                shift_pattern = "DDDDDDDNNNNNNN",
                mobilization_hours = 6,
                work_hours = 12,
                demobilization_hours = 6 ))
        propeople_activity_shift_pattern_collection.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 3,
                shift_pattern_code = "N7D7",
                shift_pattern_description = "First 7 nightshift, then 7 dayshift. 6 hours on mobilization day, then 12 hours next shifts and 6 hours on demobilization day.",
                shift_pattern_days = 14,
                shift_pattern = "NNNNNNNDDDDDDD",
                mobilization_hours = 6,
                work_hours = 12,
                demobilization_hours = 6 ))

        assert propeople_activity_shift_pattern_collection.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activity_shift_pattern_collection.__repr__()}'"

        propeople_activity_shift_pattern_collection.iterate_over_patterns()


    def test_ActivityShiftPatternCollection_to_dataframe(self):
        expected_shape = 2
        expected_shift_pattern_id = 3
        expected_shift_pattern_code = "N7D7"
        expected_shift_pattern_description = "First 7 nightshift, then 7 dayshift. 6 hours on mobilization day, then 12 hours next shifts and 6 hours on demobilization day."
        expected_shift_pattern_days = 14
        expected_shift_pattern = "NNNNNNNDDDDDDD"
        expected_mobilization_hours = 6
        expected_work_hours = 12
        expected_demobilization_hours = 6

        propeople_activity_shift_pattern_collection = ActivityShiftPatternCollection()

        propeople_activity_shift_pattern_collection.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 2,
                shift_pattern_code = "D7N7",
                shift_pattern_description = "First 7 dayshift, then 7 nightshift. 6 hours on mobilization day, then 12 hours next shifts and 6 hours on demobilization day.",
                shift_pattern_days = 14,
                shift_pattern = "DDDDDDDNNNNNNN",
                mobilization_hours = 6,
                work_hours = 12,
                demobilization_hours = 6 ))
        propeople_activity_shift_pattern_collection.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 3,
                shift_pattern_code = "N7D7",
                shift_pattern_description = "First 7 nightshift, then 7 dayshift. 6 hours on mobilization day, then 12 hours next shifts and 6 hours on demobilization day.",
                shift_pattern_days = 14,
                shift_pattern = "NNNNNNNDDDDDDD",
                mobilization_hours = 6,
                work_hours = 12,
                demobilization_hours = 6 ))

        propeople_activity_shift_pattern_df = propeople_activity_shift_pattern_collection.to_dataframe()

        assert isinstance(propeople_activity_shift_pattern_df, pd.DataFrame), f"The ProPeople activity shift pattern collection object is expected to be of class pandas DataFrame and not '{type(pd.DataFrame).__name__}'"
        assert propeople_activity_shift_pattern_df.shape[0] == expected_shape, f"The expected value of the class repr is '{expected_shape}' and not '{propeople_activity_shift_pattern_df.shape[0]}'"
        assert propeople_activity_shift_pattern_df.loc[1, "ShiftPatternID"] == expected_shift_pattern_id, f"The expected value of ShiftPatternID is '{expected_shift_pattern_id}' and not '{propeople_activity_shift_pattern_df.loc[1, 'ShiftPatternID']}'"
        assert propeople_activity_shift_pattern_df.loc[1, "ShiftPatternCode"] == expected_shift_pattern_code, f"The expected value of ShiftPatternCode is '{expected_shift_pattern_code}' and not '{propeople_activity_shift_pattern_df.loc[1, 'ShiftPatternCode']}'"
        assert propeople_activity_shift_pattern_df.loc[1, "ShiftPatternDescription"] == expected_shift_pattern_description, f"The expected value of ShiftPatternDescription is '{expected_shift_pattern_description}' and not '{propeople_activity_shift_pattern_df.loc[1, 'ShiftPatternDescription']}'"
        assert propeople_activity_shift_pattern_df.loc[1, "ShiftPatternDays"] == expected_shift_pattern_days, f"The expected value of ShiftPatternDays is '{expected_shift_pattern_days}' and not '{propeople_activity_shift_pattern_df.loc[1, 'ShiftPatternDays']}'"
        assert propeople_activity_shift_pattern_df.loc[1, "ShiftPattern"] == expected_shift_pattern, f"The expected value of ShiftPattern is '{expected_shift_pattern}' and not '{propeople_activity_shift_pattern_df.loc[1, 'ShiftPattern']}'"
        assert propeople_activity_shift_pattern_df.loc[1, "MobilizationHours"] == expected_mobilization_hours, f"The expected value of MobilizationHours is '{expected_mobilization_hours}' and not '{propeople_activity_shift_pattern_df.loc[1, 'MobilizationHours']}'"
        assert propeople_activity_shift_pattern_df.loc[1, "WorkHours"] == expected_work_hours, f"The expected value of WorkHours is '{expected_work_hours}' and not '{propeople_activity_shift_pattern_df.loc[1, 'WorkHours']}'"
        assert propeople_activity_shift_pattern_df.loc[1, "DemobilizationHours"] == expected_demobilization_hours, f"The expected value of DemobilizationHours is '{expected_demobilization_hours}' and not '{propeople_activity_shift_pattern_df.loc[1, 'DemobilizationHours']}'"


    def test_ActivityShiftPatternCollection_populate(self):
        expected_repr = "Activity shift patterns 2"

        propeople_activity_shift_pattern_collection = ActivityShiftPatternCollection()

        propeople_activity_shift_pattern_collection.populate()

        # assert propeople_activity_shift_pattern_collection.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activity_shift_pattern_collection.__repr__()}'"

        propeople_activity_shift_pattern_collection.iterate_over_patterns()


# if __name__ == '__main__':
#     unittest.main()

tests = ProPeopleActivityShiftPatternCollectionTestCase()
# tests.test_ActivityShiftPatternCollection_init()
# tests.test_ActivityShiftPatternCollection_repr()
# tests.test_ActivityShiftPatternCollection_add_pattern()
# tests.test_ActivityShiftPatternCollection_to_dataframe()
tests.test_ActivityShiftPatternCollection_populate()
