import unittest
import pandas as pd
from datetime import date, datetime

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from activity import Activity
from activities import Activities


class ProPeopleActivitiesTestCase(unittest.TestCase):


    def test_Activities_init(self):
        propeople_activities = Activities()

        assert isinstance(propeople_activities, Activities), f"The ProPeople activities table object is expected to be of class Activities and not '{type(Activities).__name__}'"


    def test_Activities_repr(self):
        expected_repr = "Activities 0"

        propeople_activities = Activities()

        assert propeople_activities.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activities.__repr__()}'"


    def test_Activities_add_activity(self):
        expected_repr = "Activities 2"

        propeople_activities = Activities()

        propeople_activities.add_activity(
            Activity(
                activity_id = 1,
                from_date = date(2023, 11, 1),
                to_date = date(2023, 11, 16),
                original_from_date = date(2023, 11, 3),
                original_to_date = date(2023, 11, 15),
                shift_pattern_id = 3,
                shift_pattern_code = "N7D7",
                rotation_group = "BraeAlphaB5",
                rotation_pattern =  "21-21",
                person_id = "KIMO",
                person_propeople_id = 36766,
                person_first_name = "Kim",
                person_last_name = "Olsen",
                internal_or_external = "Internal",
                job_id = "BU1128DAB",
                job_description = "Crane Operator - DAB",
                discipline = "Replacement",
                job_sort = "2100",
                job_emergency_description = "Firefighter & HLO & Fast Rescue Boat",
                project_business_unit_report_description = "Deepsea Aberdeen",
                rig_site = "Deepsea Aberdeen",
                cabin = "106B",
                status = "",
                comment = "For Hallvar Koløy",
                last_updated_datetime = datetime(2023, 11, 28, 17, 32, 50)))
        propeople_activities.add_activity(
            Activity(
                activity_id = 1,
                from_date = date(2023, 12, 1),
                to_date = date(2023, 12, 24),
                original_from_date = date(2023, 12, 1),
                original_to_date = date(2023, 12, 24),
                shift_pattern_id = 2,
                shift_pattern_code = "D7N7",
                rotation_group = "BraeAlphaB5",
                rotation_pattern =  "21-21",
                person_id = "PAHE",
                person_propeople_id = 36555,
                person_first_name = "Pål",
                person_last_name = "Hellesnes",
                internal_or_external = "External",
                job_id = "BU2023BI",
                job_description = "Business Intelligence Consultant - BI",
                discipline = "Replacement",
                job_sort = "2100",
                job_emergency_description = "Firefighter & HLO & Fast Rescue Boat",
                project_business_unit_report_description = "Deepsea Aberdeen",
                rig_site = "Deepsea Aberdeen",
                cabin = "106A",
                status = "",
                comment = "New Data Platform",
                last_updated_datetime = datetime(2023, 11, 28, 17, 32, 50)))

        assert propeople_activities.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activities.__repr__()}'"

        propeople_activities.list_patterns()


    def test_Activities_populate(self):
        expected_repr = "Activities 2"

        propeople_activities = Activities()

        propeople_activities.populate()

        assert propeople_activities.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activities.__repr__()}'"

        propeople_activities.list_patterns()


# if __name__ == '__main__':
#     unittest.main()

tests = ProPeopleActivitiesTestCase()
tests.test_Activities_init()
tests.test_Activities_repr()
tests.test_Activities_add_activity()
tests.test_Activities_populate()
