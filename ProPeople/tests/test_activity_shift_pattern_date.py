import unittest
import pandas as pd
import datetime
from datetime import date

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from activity_shift_pattern_date import ActivityShiftPatternDate


class ProPeopleActivityShiftPatternDateTestCase(unittest.TestCase):


    def test_ActivityShiftPatternDate_init(self):
        date = datetime.date(2023, 11, 28)
        shift_pattern_id = 1
        shift = "N"
        mobilization_hours = 6
        work_hours = 12
        demobilization_hours = 6

        propeople_activity_shift_pattern_date = ActivityShiftPatternDate(
            date = date,
            shift_pattern_id = shift_pattern_id,
            shift = shift,
            mobilization_hours = mobilization_hours,
            work_hours = work_hours,
            demobilization_hours = demobilization_hours
        )

        assert isinstance(propeople_activity_shift_pattern_date, ActivityShiftPatternDate), f"The ProPeople activity shift pattern object is expected to be of class ActivityShiftPattern and not '{type(ActivityShiftPatternDate).__name__}'"
        assert propeople_activity_shift_pattern_date.date == date, f"The expected value of the date is '{date}' and not '{propeople_activity_shift_pattern_date.date}'"
        assert propeople_activity_shift_pattern_date.shift_pattern_id == shift_pattern_id, f"The expected value of the shift pattern ID is '{shift_pattern_id}' and not '{propeople_activity_shift_pattern_date.shift_pattern_id}'"
        assert propeople_activity_shift_pattern_date.shift == shift, f"The expected value of the shift is '{shift}' and not '{propeople_activity_shift_pattern_date.shift}'"
        assert propeople_activity_shift_pattern_date.mobilization_hours == mobilization_hours, f"The expected value of the mobilization hours is '{mobilization_hours}' and not '{propeople_activity_shift_pattern_date.mobilization_hours}'"
        assert propeople_activity_shift_pattern_date.work_hours == work_hours, f"The expected value of the work hours is '{work_hours}' and not '{propeople_activity_shift_pattern_date.work_hours}'"
        assert propeople_activity_shift_pattern_date.demobilization_hours == demobilization_hours, f"The expected value of the shift pattern ID is '{demobilization_hours}' and not '{propeople_activity_shift_pattern_date.demobilization_hours}'"


    def test_ActivityShiftPatternDate_repr(self):
        date = datetime.date(2023, 11, 28)
        shift_pattern_id = 1
        shift = "N"
        mobilization_hours = 6
        work_hours = 12
        demobilization_hours = 6

        expected_repr = "(1) - N, 6, 12, 6"

        propeople_activity_shift_pattern_date = ActivityShiftPatternDate(
            date = date,
            shift_pattern_id = shift_pattern_id,
            shift = shift,
            mobilization_hours = mobilization_hours,
            work_hours = work_hours,
            demobilization_hours = demobilization_hours
        )

        assert propeople_activity_shift_pattern_date.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activity_shift_pattern_date.__repr__()}'"


# if __name__ == '__main__':
#     unittest.main()

tests = ProPeopleActivityShiftPatternDateTestCase()
tests.test_ActivityShiftPatternDate_init()
tests.test_ActivityShiftPatternDate_repr()
