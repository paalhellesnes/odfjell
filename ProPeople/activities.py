
#     *****    ******    *******   **         **
#    **   **   **   **   **         **   *   **
#    **        ******    *****       ** *** **
#    **   **   ** **     **           *** ***
#     *****    **   **   *******       *   *

"""
A class representing a table of activities.
Each activity contains properties for crew activities planned in ProPeople.
This data is gathered from the ProPeople API.
"""

import pandas as pd
from datetime import date, datetime
import exception
from activity import Activity


class Activities:
    """
    A class representing a table of activities for the ProPeople shift types for crew activities.
    """

    ###########################
    #    I N I T I A L I Z E
    ###########################

    def __init__(self):
        """
        Initializing the activity table class.
        """
        
        self.activities_df = pd.DataFrame(columns=[
            "ID", 
            "ActivityID",
            "FromDate",
            "ToDate",
            "OriginalFromDate",
            "OriginalToDate",
            "ShiftPatternID",
            "ShiftPatternCode",
            "RotationGroup",
            "RotationPattern",
            "PersonID",
            "Person_PropeopleID",
            "Person_FirstName",
            "PersonLastName",
            "InternalOrExternal",
            "JobID",
            "Job_Description",
            "Discipline",
            "JobSort",
            "JobEmergencyDescription",
            "ProjectBusinessUnitReportDescription",
            "RigSite",
            "Cabin",
            "Status",
            "Comment",
            "LastUpdatedDatetime",
            "Person",
            "OriginalShiftPattern",
            "OriginalShiftPatternDays",
            "DurationInDays",
            "ShiftPattern",
            "DayPattern"
            ])


    def __repr__(self) -> str:
        count = len(self.activities_df)
        return f"Activities {count}"


    ############################
    #    P R O P E R T I E S
    ############################


    # ######################
    # #    M E T H O D S
    # ######################

    def add_activity(self, activity):
        """
        Add a activity object to the table.

        Parameters:
        - activity (Activity): A activity object to be added to the table.
        """
        activity_id = len(self.activities_df) + 1
        activity_dict = {
            "ID": activity_id,
            "ActivityID": activity.activity_id,
            "FromDate": activity.from_date,
            "ToDate": activity.to_date,
            "OriginalFromDate": activity.original_from_date,
            "OriginalToDate": activity.original_to_date,
            "ShiftPatternID": activity.shift_pattern_id,
            "ShiftPatternCode": activity.shift_pattern_code,
            "RotationGroup": activity.rotation_group,
            "RotationPattern": activity.rotation_pattern,
            "PersonID": activity.person_id,
            "Person_PropeopleID": activity.person_propeople_id,
            "Person_FirstName": activity.person_first_name,
            "PersonLastName": activity.person_last_name,
            "InternalOrExternal": activity.internal_or_external,
            "JobID": activity.job_id,
            "Job_Description": activity.job_description,
            "Discipline": activity.discipline,
            "JobSort": activity.job_sort,
            "JobEmergencyDescription": activity.job_emergency_description,
            "ProjectBusinessUnitReportDescription": activity.project_business_unit_report_description,
            "RigSite": activity.rig_site,
            "Cabin": activity.cabin,
            "Status": activity.status,
            "Comment": activity.comment,
            "LastUpdatedDatetime": activity.last_updated_datetime,
            "Person": activity.person,
            "OriginalShiftPattern": activity.original_shift_pattern,
            "OriginalShiftPatternDays": activity.original_shift_pattern_days,
            "DurationInDays": activity.duration_in_days,
            "ShiftPattern": activity.shift_pattern,
            "DayPattern": activity.day_pattern
        }
        self.activities_df = self.activities_df.append(activity_dict, ignore_index=True)


    def list_patterns(self):
        """
        Iterate over all activities in the table and print their information.
        """
        if self.activities_df.empty:
            print("No activities in the table.")
        else:
            print("List of activities:")
            print(self.activities_df)


    def populate(self):
        """
        Fills the table with activities for the ProPeople shift types for crew activities.
        """
        self.patterns = []
        self.add_activity(
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
        self.add_activity(
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

