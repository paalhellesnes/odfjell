
#     *****    ******    *******   **         **
#    **   **   **   **   **         **   *   **
#    **        ******    *****       ** *** **
#    **   **   ** **     **           *** ***
#     *****    **   **   *******       *   *

"""
The main library for creating the activity shift pattern date table for the ProPeople shift types for crew activities.
"""

import pandas as pd
from datetime import date, datetime, timedelta
import exception
from activity import Activity
from activities import Activities
from activity_date import ActivityDate
from activity_dates import ActivityDates
from activity_shift_pattern import ActivityShiftPattern
from activity_shift_patterns import ActivityShiftPatterns


################
#    M A I N
################



##########################
#    F U N C T I O N S
##########################


def create_activity_date_table(
    activities: Activities
) -> pd.DataFrame:
    """
    Generates an activity dates table from a given activities table.

    Args:
        activities (Activities): Input activities table as a Pandas DataFrame.

    Returns:
        The resulting activity dates table as a Pandas DataFrame.

    Raises:
        InvalidArgumentTypeError: One or more parameters have invalid type.
        InvalidArgumentValueError: One or more parameters have invalid value.
    """
    if not isinstance(activities, Activities):
        raise exception.InvalidArgumentTypeError(f"The activities parameter must be a Activities value type, the given value '{activities}' is of type {type(activities)}")

    activity_shift_patterns = ActivityShiftPatterns()
    activity_shift_patterns.populate()

    activity_dates = ActivityDates()

    if not activities.activities_df.empty:

        for index, row in activities.activities_df.iterrows():

            activity = Activity(
                activity_id = row['ActivityID'],
                from_date = row['FromDate'],
                to_date = row['ToDate'],
                original_from_date = row['OriginalFromDate'],
                original_to_date = row['OriginalToDate'],
                shift_pattern_id = row['ShiftPatternID'],
                shift_pattern_code = row['ShiftPatternCode'],
                rotation_group = row['RotationGroup'],
                rotation_pattern = row['RotationPattern'],
                person_id = row['PersonID'],
                person_propeople_id = row['PersonPropeopleID'],
                person_first_name = row['PersonFirstName'],
                person_last_name = row['PersonLastName'],
                internal_or_external = row['InternalOrExternal'],
                job_id = row['JobID'],
                job_description = row['JobDescription'],
                discipline = row['Discipline'],
                job_sort = row['JobSort'],
                job_emergency_description = row['JobEmergencyDescription'],
                project_business_unit_report_description = row['ProjectBusinessUnitReportDescription'],
                rig_site = row['RigSite'],
                cabin = row['Cabin'],
                status = row['Status'],
                comment = row['Comment'],
                last_updated_datetime = row['LastUpdatedDatetime'])

            mobilization_hours = activity_shift_patterns.get_mobilization_hours_by_code(activity.shift_pattern_code)
            work_hours = activity_shift_patterns.get_work_hours_by_code(activity.shift_pattern_code)
            demobilization_hours = activity_shift_patterns.get_demobilization_hours_by_code(activity.shift_pattern_code)

            for day in range(activity.duration_in_days):
                shift_code_according_to_shift_pattern = activity.shift_pattern[day]
                day_code_according_to_day_pattern = activity.day_pattern[day]
                if day_code_according_to_day_pattern == "M":
                    hours_according_to_shift_pattern = mobilization_hours
                elif day_code_according_to_day_pattern == "D":
                    hours_according_to_shift_pattern = demobilization_hours
                else:
                    hours_according_to_shift_pattern = work_hours
                activity_dates.add_activity_date(
                    ActivityDate(
                        activity_id = activity.activity_id,
                        activity_date = activity.from_date + timedelta(days=day),
                        person_id = activity.person_id,
                        from_date = activity.from_date,
                        to_date = activity.to_date,
                        duration_in_days = activity.duration_in_days,
                        shift_pattern = activity.shift_pattern,
                        shift_code = shift_code_according_to_shift_pattern,
                        day_code = day_code_according_to_day_pattern,
                        hours = hours_according_to_shift_pattern,
                        original_from_date = activity.original_from_date,
                        original_to_date = activity.original_to_date,
                        original_shift_pattern = activity.original_shift_pattern ))

    return activity_dates

