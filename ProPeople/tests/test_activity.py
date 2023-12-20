import unittest
import pandas as pd
from datetime import date, datetime

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from activity import Activity


class ProPeopleActivityTestCase(unittest.TestCase):


    def test_Activity_init(self):

        activity_id = 1
        from_date = date(2023, 11, 1)
        to_date = date(2023, 11, 13)
        original_from_date = date(2023, 11, 3)
        original_to_date = date(2023, 11, 15)
        shift_pattern_id = 3
        shift_pattern_code = "N7D7"
        rotation_group = "BraeAlphaB5"
        rotation_pattern = "21-21"
        person_id = "KIMO"
        person_propeople_id = 36766
        person_first_name = "Kim"
        person_last_name = "Olsen"
        internal_or_external = "Internal"
        job_id = "BU1128DAB"
        job_description = "Crane Operator - DAB"
        discipline = "Replacement"
        job_sort = "2100"
        job_emergency_description = "Firefighter & HLO & Fast Rescue Boat"
        project_business_unit_report_description = "Deepsea Aberdeen"
        rig_site = "Deepsea Aberdeen"
        cabin = "106B"
        status = ""
        comment = "For Hallvar Koløy"
        last_updated_datetime = datetime(2023, 11, 28, 17, 32, 50)

        expected_person = "Olsen Kim"
        expected_original_shift_pattern = "NNNNNNNDDDDDDD"
        expected_shift_pattern = "DDNNNNNNNDDDD"
        expected_day_pattern = "MWWWWWWWWWWWD"

        propeople_activity = Activity(
            activity_id = activity_id,
            from_date = from_date,
            to_date = to_date,
            original_from_date = original_from_date,
            original_to_date = original_to_date,
            shift_pattern_id = shift_pattern_id,
            shift_pattern_code = shift_pattern_code,
            rotation_group = rotation_group,
            rotation_pattern = rotation_pattern,
            person_id = person_id,
            person_propeople_id = person_propeople_id,
            person_first_name = person_first_name,
            person_last_name = person_last_name,
            internal_or_external = internal_or_external,
            job_id = job_id,
            job_description = job_description,
            discipline = discipline,
            job_sort = job_sort,
            job_emergency_description = job_emergency_description,
            project_business_unit_report_description = project_business_unit_report_description,
            rig_site = rig_site,
            cabin = cabin,
            status = status,
            comment = comment,
            last_updated_datetime = last_updated_datetime
        )

        assert isinstance(propeople_activity, Activity), f"The ProPeople activity object is expected to be of class Activity and not '{type(Activity).__name__}'"
        assert propeople_activity.activity_id == activity_id, f"The expected value of the activity activity ID is '{activity_id}' and not '{propeople_activity.activity_id}'"
        assert propeople_activity.from_date == from_date, f"The expected value of the activity from_date is '{from_date}' and not '{propeople_activity.from_date}'"
        assert propeople_activity.to_date == to_date, f"The expected value of the activity to_date is '{to_date}' and not '{propeople_activity.to_date}'"
        assert propeople_activity.original_from_date == original_from_date, f"The expected value of the activity original_from_date is '{original_from_date}' and not '{propeople_activity.original_from_date}'"
        assert propeople_activity.original_to_date == original_to_date, f"The expected value of the activity original_to_date is '{original_to_date}' and not '{propeople_activity.original_to_date}'"
        assert propeople_activity.shift_pattern_id == shift_pattern_id, f"The expected value of the activity shift pattern_id is '{shift_pattern_id}' and not '{propeople_activity.shift_pattern_id}'"
        assert propeople_activity.shift_pattern_code == shift_pattern_code, f"The expected value of the activity shift pattern code is '{shift_pattern_code}' and not '{propeople_activity.shift_pattern_code}'"
        assert propeople_activity.rotation_group == rotation_group, f"The expected value of the activity rotation group is '{rotation_group}' and not '{propeople_activity.rotation_group}'"
        assert propeople_activity.rotation_pattern == rotation_pattern, f"The expected value of the activity rotation pattern is '{rotation_pattern}' and not '{propeople_activity.rotation_pattern}'"
        assert propeople_activity.person_id == person_id, f"The expected value of the activity person ID is '{person_id}' and not '{propeople_activity.person_id}'"
        assert propeople_activity.person_propeople_id == person_propeople_id, f"The expected value of the activity person ProPeople ID is '{person_propeople_id}' and not '{propeople_activity.person_propeople_id}'"
        assert propeople_activity.person_first_name == person_first_name, f"The expected value of the activity person first name is '{person_first_name}' and not '{propeople_activity.person_first_name}'"
        assert propeople_activity.person_last_name == person_last_name, f"The expected value of the activity person last name is '{person_last_name}' and not '{propeople_activity.person_last_name}'"
        assert propeople_activity.internal_or_external == internal_or_external, f"The expected value of the activity internal/external is '{internal_or_external}' and not '{propeople_activity.internal_or_external}'"
        assert propeople_activity.job_id == job_id, f"The expected value of the activity job ID is '{job_id}' and not '{propeople_activity.job_id}'"
        assert propeople_activity.job_description == job_description, f"The expected value of the activity job description is '{job_description}' and not '{propeople_activity.job_description}'"
        assert propeople_activity.discipline == discipline, f"The expected value of the activity discipline is '{discipline}' and not '{propeople_activity.discipline}'"
        assert propeople_activity.job_sort == job_sort, f"The expected value of the activity job sort is '{job_sort}' and not '{propeople_activity.job_sort}'"
        assert propeople_activity.job_emergency_description == job_emergency_description, f"The expected value of the activity job emergency description is '{job_emergency_description}' and not '{propeople_activity.job_emergency_description}'"
        assert propeople_activity.project_business_unit_report_description == project_business_unit_report_description, f"The expected value of the activity project business unit report description is '{project_business_unit_report_description}' and not '{propeople_activity.project_business_unit_report_description}'"
        assert propeople_activity.rig_site == rig_site, f"The expected value of the activity rig site is '{rig_site}' and not '{propeople_activity.rig_site}'"
        assert propeople_activity.cabin == cabin, f"The expected value of the activity cabin is '{cabin}' and not '{propeople_activity.cabin}'"
        assert propeople_activity.status == status, f"The expected value of the activity status is '{status}' and not '{propeople_activity.status}'"
        assert propeople_activity.comment == comment, f"The expected value of the activity comment is '{comment}' and not '{propeople_activity.comment}'"
        assert propeople_activity.last_updated_datetime == last_updated_datetime, f"The expected value of the activity last updated datetime is '{last_updated_datetime}' and not '{propeople_activity.last_updated_datetime}'"
        assert propeople_activity.person == expected_person, f"The expected value of the activity person is '{expected_person}' and not '{propeople_activity.person}'"
        assert propeople_activity.original_shift_pattern == expected_original_shift_pattern, f"The expected value of the activity original shift pattern is '{expected_original_shift_pattern}' and not '{propeople_activity.original_shift_pattern}'"
        assert propeople_activity.shift_pattern == expected_shift_pattern, f"The expected value of the activity actual shift pattern is '{expected_shift_pattern}' and not '{propeople_activity.shift_pattern}'"
        assert propeople_activity.day_pattern == expected_day_pattern, f"The expected value of the activity actual day pattern is '{expected_day_pattern}' and not '{propeople_activity.day_pattern}'"


    def test_Activity_repr(self):
        activity_id = 1
        from_date = date(2023, 11, 1)
        to_date = date(2023, 11, 13)
        original_from_date = date(2023, 11, 3)
        original_to_date = date(2023, 11, 15)
        shift_pattern_id = 3
        shift_pattern_code = "N7D7"
        rotation_group = "BraeAlphaB5"
        rotation_pattern = "21-21"
        person_id = "KIMO"
        person_propeople_id = 36766
        person_first_name = "Kim"
        person_last_name = "Olsen"
        internal_or_external = "Internal"
        job_id = "BU1128DAB"
        job_description = "Crane Operator - DAB"
        discipline = "Replacement"
        job_sort = "2100"
        job_emergency_description = "Firefighter & HLO & Fast Rescue Boat"
        project_business_unit_report_description = "Deepsea Aberdeen"
        rig_site = "Deepsea Aberdeen"
        cabin = "106B"
        status = ""
        comment = "For Hallvar Koløy"
        last_updated_datetime = datetime(2023, 11, 28, 17, 32, 50)

        expected_repr = "Olsen Kim - Deepsea Aberdeen - 2023-11-01-2023-11-13"

        propeople_activity = Activity(
            activity_id = activity_id,
            from_date = from_date,
            to_date = to_date,
            original_from_date = original_from_date,
            original_to_date = original_to_date,
            shift_pattern_id = shift_pattern_id,
            shift_pattern_code = shift_pattern_code,
            rotation_group = rotation_group,
            rotation_pattern = rotation_pattern,
            person_id = person_id,
            person_propeople_id = person_propeople_id,
            person_first_name = person_first_name,
            person_last_name = person_last_name,
            internal_or_external = internal_or_external,
            job_id = job_id,
            job_description = job_description,
            discipline = discipline,
            job_sort = job_sort,
            job_emergency_description = job_emergency_description,
            project_business_unit_report_description = project_business_unit_report_description,
            rig_site = rig_site,
            cabin = cabin,
            status = status,
            comment = comment,
            last_updated_datetime = last_updated_datetime
        )

        assert propeople_activity.__repr__() == expected_repr, f"The expected value of the class repr is '{expected_repr}' and not '{propeople_activity.__repr__()}'"


    def test_Activity_get_original_shift_pattern(self):
        propeople_activity = Activity(
            activity_id = 1,
            from_date = date(2023, 11, 1),
            to_date = date(2023, 11, 13),
            original_from_date = date(2023, 11, 3),
            original_to_date = date(2023, 11, 15),
            shift_pattern_id = 3,
            shift_pattern_code = "N7D7",
            rotation_group = "BraeAlphaB5",
            rotation_pattern = "21-21",
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
            last_updated_datetime = datetime(2023, 11, 28, 17, 32, 50),
        )

        expected_original_shift_pattern = "NNNNNNNDDDDDDD"
        original_shift_pattern = propeople_activity.get_original_shift_pattern(
            shift_pattern_id = 3,
            shift_pattern_code = "N7D7"
        )
        assert original_shift_pattern == expected_original_shift_pattern, f"The expected value of the original shift pattern is '{expected_original_shift_pattern}' and not '{original_shift_pattern}'"

        expected_original_shift_pattern = "NNNNNNNDDDDDDD"
        original_shift_pattern = propeople_activity.get_original_shift_pattern(
            shift_pattern_id = None,
            shift_pattern_code = "N7D7"
        )
        assert original_shift_pattern == expected_original_shift_pattern, f"The expected value of the original shift pattern is '{expected_original_shift_pattern}' and not '{original_shift_pattern}'"

        expected_original_shift_pattern = None
        original_shift_pattern = propeople_activity.get_original_shift_pattern(
            shift_pattern_id = None,
            shift_pattern_code = None
        )
        assert original_shift_pattern == expected_original_shift_pattern, f"The expected value of the original shift pattern is '{expected_original_shift_pattern}' and not '{original_shift_pattern}'"

        expected_original_shift_pattern = None
        original_shift_pattern = propeople_activity.get_original_shift_pattern(
            shift_pattern_id = None,
            shift_pattern_code = "THIS CODE DOES NOT EXIST"
        )
        assert original_shift_pattern == expected_original_shift_pattern, f"The expected value of the original shift pattern is '{expected_original_shift_pattern}' and not '{original_shift_pattern}'"


    def test_Activity_calculate_duration_in_days(self):
        propeople_activity = Activity(
            activity_id = 1,
            from_date = date(2023, 11, 1),
            to_date = date(2023, 11, 13),
            original_from_date = date(2023, 11, 3),
            original_to_date = date(2023, 11, 15),
            shift_pattern_id = 3,
            shift_pattern_code = "N7D7",
            rotation_group = "BraeAlphaB5",
            rotation_pattern = "21-21",
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
            last_updated_datetime = datetime(2023, 11, 28, 17, 32, 50),
        )

        expected_duration_in_days = 13
        duration_in_days = propeople_activity.calculate_duration_in_days(
            from_date = date(2023, 11, 1),
            to_date = date(2023, 11, 13)
        )
        assert duration_in_days == expected_duration_in_days, f"The expected value of the duration in days is '{expected_duration_in_days}' and not '{duration_in_days}'"

        expected_duration_in_days = 1
        duration_in_days = propeople_activity.calculate_duration_in_days(
            from_date = date(2023, 11, 13),
            to_date = date(2023, 11, 13)
        )
        assert duration_in_days == expected_duration_in_days, f"The expected value of the duration in days is '{expected_duration_in_days}' and not '{duration_in_days}'"

        expected_duration_in_days = 0
        duration_in_days = propeople_activity.calculate_duration_in_days(
            from_date = date(2023, 11, 14),
            to_date = date(2023, 11, 13)
        )
        assert duration_in_days == expected_duration_in_days, f"The expected value of the duration in days is '{expected_duration_in_days}' and not '{duration_in_days}'"


    def test_Activity_calculate_shift_pattern(self):
        propeople_activity = Activity(
            activity_id = 1,
            from_date = date(2023, 11, 1),
            to_date = date(2023, 11, 13),
            original_from_date = date(2023, 11, 3),
            original_to_date = date(2023, 11, 15),
            shift_pattern_id = 3,
            shift_pattern_code = "N7D7",
            rotation_group = "BraeAlphaB5",
            rotation_pattern = "21-21",
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
            last_updated_datetime = datetime(2023, 11, 28, 17, 32, 50),
        )

        expected_shift_pattern = "DDNNNNNNNDDDDDDDNNNNNNND"
        shift_pattern = propeople_activity.calculate_shift_pattern(
            original_shift_pattern = "NNNNNNNDDDDDDD",
            original_from_date = date(2023, 11, 3),
            from_date = date(2023, 11, 1),
            duration_in_days = 24
        )
        assert shift_pattern == expected_shift_pattern, f"The expected value of the actual shift pattern is '{expected_shift_pattern}' and not '{shift_pattern}'"


    def test_Activity_calculate_day_pattern(self):
        propeople_activity = Activity(
            activity_id = 1,
            from_date = date(2023, 11, 1),
            to_date = date(2023, 11, 13),
            original_from_date = date(2023, 11, 3),
            original_to_date = date(2023, 11, 15),
            shift_pattern_id = 3,
            shift_pattern_code = "N7D7",
            rotation_group = "BraeAlphaB5",
            rotation_pattern = "21-21",
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
            last_updated_datetime = datetime(2023, 11, 28, 17, 32, 50),
        )

        expected_day_pattern = "MWWWWWWWWWWWWWWWWWWWWWWD"
        day_pattern = propeople_activity.calculate_day_pattern(
            duration_in_days = 24
        )
        assert day_pattern == expected_day_pattern, f"The expected value of the actual day pattern is '{expected_day_pattern}' and not '{day_pattern}'"

        expected_day_pattern = ""
        day_pattern = propeople_activity.calculate_day_pattern(
            duration_in_days = -2
        )
        assert day_pattern == expected_day_pattern, f"The expected value of the actual day pattern is '{expected_day_pattern}' and not '{day_pattern}'"

        expected_day_pattern = ""
        day_pattern = propeople_activity.calculate_day_pattern(
            duration_in_days = 0
        )
        assert day_pattern == expected_day_pattern, f"The expected value of the actual day pattern is '{expected_day_pattern}' and not '{day_pattern}'"

        expected_day_pattern = "M"
        day_pattern = propeople_activity.calculate_day_pattern(
            duration_in_days = 1
        )
        assert day_pattern == expected_day_pattern, f"The expected value of the actual day pattern is '{expected_day_pattern}' and not '{day_pattern}'"

        expected_day_pattern = "MD"
        day_pattern = propeople_activity.calculate_day_pattern(
            duration_in_days = 2
        )
        assert day_pattern == expected_day_pattern, f"The expected value of the actual day pattern is '{expected_day_pattern}' and not '{day_pattern}'"



# if __name__ == '__main__':
#     unittest.main()

tests = ProPeopleActivityTestCase()
tests.test_Activity_init()
# tests.test_Activity_repr()
# tests.test_Activity_get_original_shift_pattern()
# tests.test_Activity_calculate_duration_in_days()
# tests.test_Activity_calculate_shift_pattern()
# tests.test_Activity_calculate_day_pattern()
