import unittest
import pandas as pd
from datetime import date

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from activity_date import ActivityDate
from activity_dates import ActivityDates


class ProPeopleActivityDatesTestCase(unittest.TestCase):


    def test_ActivityDates_init(self):
        propeople_activity_dates = ActivityDates()

        assert isinstance(propeople_activity_dates, ActivityDates), f"The ProPeople activity shift pattern table object is expected to be of class ActivityDates and not '{type(ActivityDates).__name__}'"


    def test_ActivityDates_repr(self):
        expected_repr = "Activity dates 0"

        propeople_activity_dates = ActivityDates()

        assert propeople_activity_dates.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activity_dates.__repr__()}'"


    def test_ActivityDates_add_activity_date(self):
        expected_repr = "Activity dates 2"

        propeople_activity_dates = ActivityDates()

        propeople_activity_dates.add_activity_date(
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
        propeople_activity_dates.add_activity_date(
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

        assert propeople_activity_dates.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activity_dates.__repr__()}'"

        propeople_activity_dates.list_patterns()


    def test_ActivityDates_populate(self):
        expected_repr = "Activity dates 2"

        propeople_activity_dates = ActivityDates()

        propeople_activity_dates.populate()

        assert propeople_activity_dates.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activity_dates.__repr__()}'"

        propeople_activity_dates.list_patterns()


# if __name__ == '__main__':
#     unittest.main()

tests = ProPeopleActivityDatesTestCase()
tests.test_ActivityDates_init()
tests.test_ActivityDates_repr()
tests.test_ActivityDates_add_activity_date()
tests.test_ActivityDates_populate()
