import unittest
import pandas as pd
from datetime import date, datetime

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from activity_date import ActivityDate


class ProPeopleActivityDateTestCase(unittest.TestCase):


    def test_ActivityDate_init(self):
        activity_id = 1
        activity_date = date(2023, 11, 1)
        person_id = "KIMO"
        from_date = date(2023, 11, 1)
        to_date = date(2023, 11, 16)
        duration_in_days = 16
        shift_pattern = "DDNNNNNNNDDDDDDD"
        shift_code = "D"
        day_code = "M"
        hours = 6.0
        original_from_date = date(2023, 11, 3)
        original_to_date = date(2023, 11, 15)
        original_shift_pattern = "NNNNNNNDDDDDDD"

        propeople_activity_date = ActivityDate(
            activity_date = activity_date,
            activity_id = activity_id,
            person_id = person_id,
            from_date = from_date,
            to_date = to_date,
            duration_in_days = duration_in_days,
            shift_pattern = shift_pattern,
            shift_code = shift_code,
            day_code = day_code,
            hours = hours,
            original_from_date = original_from_date,
            original_to_date = original_to_date,
            original_shift_pattern = original_shift_pattern
        )

        assert isinstance(propeople_activity_date, ActivityDate), f"The ProPeople activity date object is expected to be of class ActivityDate and not '{type(ActivityDate).__name__}'"
        assert propeople_activity_date.activity_id == activity_id, f"The expected value of the activity activity ID is '{activity_id}' and not '{propeople_activity_date.activity_id}'"
        assert propeople_activity_date.activity_date == activity_date, f"The expected value of the activity date is '{activity_date}' and not '{propeople_activity_date.activity_date}'"
        assert propeople_activity_date.person_id == person_id, f"The expected value of the activity person ID is '{person_id}' and not '{propeople_activity_date.person_id}'"
        assert propeople_activity_date.from_date == from_date, f"The expected value of the activity from date is '{from_date}' and not '{propeople_activity_date.from_date}'"
        assert propeople_activity_date.to_date == to_date, f"The expected value of the activity to date is '{to_date}' and not '{propeople_activity_date.to_date}'"
        assert propeople_activity_date.duration_in_days == duration_in_days, f"The expected value of the activity duration in days is '{duration_in_days}' and not '{propeople_activity_date.duration_in_days}'"
        assert propeople_activity_date.shift_pattern == shift_pattern, f"The expected value of the activity shift pattern is '{shift_pattern}' and not '{propeople_activity_date.shift_pattern}'"
        assert propeople_activity_date.shift_code == shift_code, f"The expected value of the activity shift code is '{shift_code}' and not '{propeople_activity_date.shift_code}'"
        assert propeople_activity_date.day_code == day_code, f"The expected value of the activity day code is '{day_code}' and not '{propeople_activity_date.day_code}'"
        assert propeople_activity_date.hours == hours, f"The expected value of the activity hours is '{hours}' and not '{propeople_activity_date.hours}'"
        assert propeople_activity_date.original_from_date == original_from_date, f"The expected value of the activity original from date is '{original_from_date}' and not '{propeople_activity_date.original_from_date}'"
        assert propeople_activity_date.original_to_date == original_to_date, f"The expected value of the activity original to date is '{original_to_date}' and not '{propeople_activity_date.original_to_date}'"
        assert propeople_activity_date.original_shift_pattern == original_shift_pattern, f"The expected value of the activity original shift pattern is '{original_shift_pattern}' and not '{propeople_activity_date.original_shift_pattern}'"


    def test_ActivityDate_repr(self):
        propeople_activity_date = ActivityDate(
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
            original_shift_pattern = "NNNNNNNDDDDDDD"
        )

        expected_repr = "1 [2023-11-01] - KIMO"

        assert propeople_activity_date.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activity_date.__repr__()}'"


# if __name__ == '__main__':
#     unittest.main()

tests = ProPeopleActivityDateTestCase()
tests.test_ActivityDate_init()
tests.test_ActivityDate_repr()
