import unittest
import pandas as pd
from datetime import date

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from activity_shift_pattern import ActivityShiftPattern
from activity_shift_patterns import ActivityShiftPatterns


class ProPeopleActivityShiftPatternsTestCase(unittest.TestCase):


    def test_ActivityShiftPatterns_init(self):
        propeople_activity_shift_patterns = ActivityShiftPatterns()

        assert isinstance(propeople_activity_shift_patterns, ActivityShiftPatterns), f"The ProPeople activity shift pattern table object is expected to be of class ActivityShiftPatterns and not '{type(ActivityShiftPatterns).__name__}'"


    def test_ActivityShiftPatterns_repr(self):
        expected_repr = "Activity shift patterns 0"

        propeople_activity_shift_patterns = ActivityShiftPatterns()

        assert propeople_activity_shift_patterns.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activity_shift_patterns.__repr__()}'"


    def test_ActivityShiftPatterns_add_pattern(self):
        expected_repr = "Activity shift patterns 2"

        propeople_activity_shift_patterns = ActivityShiftPatterns()

        propeople_activity_shift_patterns.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 2,
                shift_pattern_code = "D7N7",
                shift_pattern_description = "First 7 dayshift, then 7 nightshift. 6 hours on mobilization day, then 12 hours next shifts and 6 hours on demobilization day.",
                shift_pattern_days = 14,
                shift_pattern = "DDDDDDDNNNNNNN",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))
        propeople_activity_shift_patterns.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 3,
                shift_pattern_code = "N7D7",
                shift_pattern_description = "First 7 nightshift, then 7 dayshift. 6 hours on mobilization day, then 12 hours next shifts and 6 hours on demobilization day.",
                shift_pattern_days = 14,
                shift_pattern = "NNNNNNNDDDDDDD",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))

        assert propeople_activity_shift_patterns.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activity_shift_patterns.__repr__()}'"

        propeople_activity_shift_patterns.list_patterns()


    def test_ActivityShiftPatterns_get_pattern_by_id(self):
        expected_repr = "NNNNNNNDDDDDDD"

        propeople_activity_shift_patterns = ActivityShiftPatterns()

        propeople_activity_shift_patterns.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 2,
                shift_pattern_code = "D7N7",
                shift_pattern_description = "First 7 dayshift, then 7 nightshift. 6 hours on mobilization day, then 12 hours next shifts and 6 hours on demobilization day.",
                shift_pattern_days = 14,
                shift_pattern = "DDDDDDDNNNNNNN",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))
        propeople_activity_shift_patterns.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 3,
                shift_pattern_code = "N7D7",
                shift_pattern_description = "First 7 nightshift, then 7 dayshift. 6 hours on mobilization day, then 12 hours next shifts and 6 hours on demobilization day.",
                shift_pattern_days = 14,
                shift_pattern = "NNNNNNNDDDDDDD",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))

        propeople_activity_shift_pattern = propeople_activity_shift_patterns.get_shift_pattern_by_id(
            shift_pattern_id = 3)

        assert propeople_activity_shift_pattern == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activity_shift_pattern.__repr__()}'"


    def test_ActivityShiftPatterns_get_pattern_by_code(self):
        expected_repr = "NNNNNNNDDDDDDD"

        propeople_activity_shift_patterns = ActivityShiftPatterns()

        propeople_activity_shift_patterns.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 2,
                shift_pattern_code = "D7N7",
                shift_pattern_description = "First 7 dayshift, then 7 nightshift. 6 hours on mobilization day, then 12 hours next shifts and 6 hours on demobilization day.",
                shift_pattern_days = 14,
                shift_pattern = "DDDDDDDNNNNNNN",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))
        propeople_activity_shift_patterns.add_pattern(
            ActivityShiftPattern(
                shift_pattern_id = 3,
                shift_pattern_code = "N7D7",
                shift_pattern_description = "First 7 nightshift, then 7 dayshift. 6 hours on mobilization day, then 12 hours next shifts and 6 hours on demobilization day.",
                shift_pattern_days = 14,
                shift_pattern = "NNNNNNNDDDDDDD",
                mobilization_hours = 6.0,
                work_hours = 12.0,
                demobilization_hours = 6.0 ))

        propeople_activity_shift_pattern = propeople_activity_shift_patterns.get_shift_pattern_by_code(
            shift_pattern_code = "N7D7")

        assert propeople_activity_shift_pattern == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activity_shift_pattern.__repr__()}'"


    def test_ActivityShiftPatterns_populate(self):
        expected_repr = "Activity shift patterns 17"

        propeople_activity_shift_patterns = ActivityShiftPatterns()

        propeople_activity_shift_patterns.populate()

        assert propeople_activity_shift_patterns.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activity_shift_patterns.__repr__()}'"

        propeople_activity_shift_patterns.list_patterns()


# if __name__ == '__main__':
#     unittest.main()

tests = ProPeopleActivityShiftPatternsTestCase()
# tests.test_ActivityShiftPatterns_init()
# tests.test_ActivityShiftPatterns_repr()
# tests.test_ActivityShiftPatterns_add_pattern()
# tests.test_ActivityShiftPatterns_get_pattern_by_id()
tests.test_ActivityShiftPatterns_get_pattern_by_code()
# tests.test_ActivityShiftPatterns_populate()
