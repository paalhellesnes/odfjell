import unittest
import pandas as pd
from datetime import date

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from activity_shift_pattern import ActivityShiftPattern


class ProPeopleActivityShiftPatternTestCase(unittest.TestCase):


    def test_ActivityShiftPattern_init(self):
        shift_pattern_id = 1
        shift_pattern_code = "D7N7"
        shift_pattern_description = "First 7 dayshift, then 7 nightshift"
        shift_pattern_days = 14
        shift_pattern = "DDDDDDDNNNNNNN"
        start_date = date(2023, 11, 28)
        mobilization_hours = 6
        work_hours = 12
        demobilization_hours = 6

        propeople_activity_shift_pattern = ActivityShiftPattern(
            shift_pattern_id = shift_pattern_id,
            shift_pattern_code = shift_pattern_code,
            shift_pattern_description = shift_pattern_description,
            shift_pattern_days = shift_pattern_days,
            shift_pattern = shift_pattern,
            start_date = start_date,
            mobilization_hours = mobilization_hours,
            work_hours = work_hours,
            demobilization_hours = demobilization_hours
        )

        assert isinstance(propeople_activity_shift_pattern, ActivityShiftPattern), f"The ProPeople activity shift pattern object is expected to be of class ActivityShiftPattern and not '{type(ActivityShiftPattern).__name__}'"
        assert propeople_activity_shift_pattern.shift_pattern_id == shift_pattern_id, f"The expected value of the shift pattern ID is '{shift_pattern_id}' and not '{propeople_activity_shift_pattern.shift_pattern_id}'"
        assert propeople_activity_shift_pattern.shift_pattern_code == shift_pattern_code, f"The expected value of the shift pattern code is '{shift_pattern_code}' and not '{propeople_activity_shift_pattern.shift_pattern_code}'"
        assert propeople_activity_shift_pattern.shift_pattern_description == shift_pattern_description, f"The expected value of the shift pattern description is '{shift_pattern_description}' and not '{propeople_activity_shift_pattern.shift_pattern_description}'"
        assert propeople_activity_shift_pattern.shift_pattern_days == shift_pattern_days, f"The expected value of the shift pattern days is '{shift_pattern_days}' and not '{propeople_activity_shift_pattern.shift_pattern_days}'"
        assert propeople_activity_shift_pattern.shift_pattern == shift_pattern, f"The expected value of the shift pattern is '{shift_pattern}' and not '{propeople_activity_shift_pattern.shift_pattern}'"
        assert propeople_activity_shift_pattern.start_date == start_date, f"The expected value of the start date is '{start_date}' and not '{propeople_activity_shift_pattern.start_date}'"
        assert propeople_activity_shift_pattern.mobilization_hours == mobilization_hours, f"The expected value of the mobilization hours is '{mobilization_hours}' and not '{propeople_activity_shift_pattern.mobilization_hours}'"
        assert propeople_activity_shift_pattern.work_hours == work_hours, f"The expected value of the work hours is '{work_hours}' and not '{propeople_activity_shift_pattern.work_hours}'"
        assert propeople_activity_shift_pattern.demobilization_hours == demobilization_hours, f"The expected value of the shift pattern ID is '{demobilization_hours}' and not '{propeople_activity_shift_pattern.demobilization_hours}'"


    def test_ActivityShiftPattern_repr(self):
        shift_pattern_id = 1
        shift_pattern_code = "D7N7"
        shift_pattern_description = "First 7 dayshift, then 7 nightshift"
        shift_pattern_days = 14
        shift_pattern = "DDDDDDDNNNNNNN"
        start_date = date(2023, 11, 28)
        mobilization_hours = 6
        work_hours = 12
        demobilization_hours = 6

        expected_repr = "D7N7 - DDDDDDDNNNNNNN"

        propeople_activity_shift_pattern = ActivityShiftPattern(
            shift_pattern_id = shift_pattern_id,
            shift_pattern_code = shift_pattern_code,
            shift_pattern_description = shift_pattern_description,
            shift_pattern_days = shift_pattern_days,
            shift_pattern = shift_pattern,
            start_date = start_date,
            mobilization_hours = mobilization_hours,
            work_hours = work_hours,
            demobilization_hours = demobilization_hours
        )

        assert propeople_activity_shift_pattern.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activity_shift_pattern.__repr__()}'"


# if __name__ == '__main__':
#     unittest.main()

tests = ProPeopleActivityShiftPatternTestCase()
tests.test_ActivityShiftPattern_init()
tests.test_ActivityShiftPattern_repr()
