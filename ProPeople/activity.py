
#     *****    ******    *******   **         **
#    **   **   **   **   **         **   *   **
#    **        ******    *****       ** *** **
#    **   **   ** **     **           *** ***
#     *****    **   **   *******       *   *

"""
The activity class contains properties for crew activities planned in ProPeople.
This data is gathered from the ProPeople API.
"""

import pandas as pd
from datetime import date, datetime
import exception
from activity_shift_patterns import ActivityShiftPatterns

class Activity:
    """
    The activity class contains properties for crew activities planned in ProPeople.
    """

    ###########################
    #    I N I T I A L I Z E
    ###########################

    def __init__(self,
        activity_id: int,
        from_date: date,
        to_date: date,
        original_from_date: date,
        original_to_date: date,
        shift_pattern_id: int,
        shift_pattern_code: str,
        rotation_group: str,
        rotation_pattern: str,
        person_id: str,
        person_propeople_id: int,
        person_first_name: str,
        person_last_name: str,
        internal_or_external: str,
        job_id: str,
        job_description: str,
        discipline: str,
        job_sort: str,
        job_emergency_description: str,
        project_business_unit_report_description: str,
        rig_site: str,
        cabin: str,
        status: str,
        comment: str,
        last_updated_datetime: datetime
    ):
        """
        Initializing the activity class.

        Args:
            activity_id (int, mandatory): Unique identification number for a given person in the ProPeople database.
            from_date (date): The actuall start date for this activity.
            to_date (date): The actuall end date for this activity.
            original_from_date (date): The start date originally planned for this activity.
            original_to_date (date): The end date originally planned for this activity.
            shift_pattern_id (int): Unique ProPeople identification number for the shift pattern for this activity.
            shift_pattern_code (str): Shift code to identify if it is a D (dayshift) or a N (night shift).
            rotation_group (str): The rotation group that decide the shift pattern in Propeople (not Crew).
            rotation_pattern (str): Rotation pattern code.
            person_id (str): The person's unique Person id.
            person_propeople_id (int): Unique identification number for a given person in the ProPeople database.
            person_first_name (str): First name of the person which actually worked on this activity.
            person_last_name (str): Last name of the person which actually worked on this activity.
            internal_or_external (str): Identify if the person is internal (employee) or external (hired).
            job_id (str): Different types such as Courses, Rig site jobs, Vacation, Sickness, Leave, Osnhore, Offshore, Laid off.
            job_description (str): Description of the job.
            discipline (str): Values found: "Replacement", "Projects", "Ekstra".
            job_sort (str): ???
            job_emergency_description (str): Job Emergency Description from IFS.
            project_business_unit_report_description (str): ???
            rig_site (str): Name of the location where this activity takes place.
            cabin (str): Cabin number reserved for the person on site for this activity.
            status (str): Status description (name) of this activity.
            comment (str): Remarks regarding this activity.
            last_updated_datetime (datetime): Date and time for when information about this activity was changed. This value is also set when the activity was created.

        Raises:
            InvalidArgumentTypeError: One or more of the passed parameter vales have invalid type.
            InvalidArgumentValueError: One or more of the passed parameter vales are invalid.
        """
        if not isinstance(activity_id, int):
            raise exception.InvalidArgumentTypeError("The activity_id parameter must be an integer value!")
        if activity_id is None:
            raise exception.InvalidArgumentTypeError("The activity_id parameter must have a value!")
        if not isinstance(from_date, date):
            raise exception.InvalidArgumentTypeError("The from_date parameter must be a date value!")
        if not isinstance(to_date, date):
            raise exception.InvalidArgumentTypeError("The to_date parameter must be a date value!")
        if not isinstance(original_from_date, date):
            raise exception.InvalidArgumentTypeError("The original_from_date parameter must be a date value!")
        if not isinstance(original_to_date, date):
            raise exception.InvalidArgumentTypeError("The original_to_date parameter must be a date value!")
        if not isinstance(shift_pattern_id, int):
            raise exception.InvalidArgumentTypeError("The shift_pattern_id parameter must be a int value!")
        if not isinstance(shift_pattern_code, str):
            raise exception.InvalidArgumentTypeError("The shift_pattern_code parameter must be a string value!")
        if not isinstance(rotation_group, str):
            raise exception.InvalidArgumentTypeError("The rotation_group parameter must be a string value!")
        if not isinstance(rotation_pattern, str):
            raise exception.InvalidArgumentTypeError("The rotation_pattern parameter must be a string value!")
        if not isinstance(person_id, str):
            raise exception.InvalidArgumentTypeError("The person_id parameter must be a string value!")
        if not isinstance(person_propeople_id, int):
            raise exception.InvalidArgumentTypeError("The person_propeople_id parameter must be a int value!")
        if not isinstance(person_first_name, str):
            raise exception.InvalidArgumentTypeError("The person_first_name parameter must be a string value!")
        if not isinstance(person_last_name, str):
            raise exception.InvalidArgumentTypeError("The person_last_name parameter must be a string value!")
        if not isinstance(internal_or_external, str):
            raise exception.InvalidArgumentTypeError("The internal_or_external parameter must be a string value!")
        if not isinstance(job_id, str):
            raise exception.InvalidArgumentTypeError("The job_id parameter must be a string value!")
        if not isinstance(job_description, str):
            raise exception.InvalidArgumentTypeError("The job_description parameter must be a string value!")
        if not isinstance(discipline, str):
            raise exception.InvalidArgumentTypeError("The discipline parameter must be a string value!")
        if not isinstance(job_sort, str):
            raise exception.InvalidArgumentTypeError("The job_sort parameter must be a string value!")
        if not isinstance(job_emergency_description, str):
            raise exception.InvalidArgumentTypeError("The job_emergency_description parameter must be a string value!")
        if not isinstance(project_business_unit_report_description, str):
            raise exception.InvalidArgumentTypeError("The project_business_unit_report_description parameter must be a string value!")
        if not isinstance(rig_site, str):
            raise exception.InvalidArgumentTypeError("The rig_site parameter must be a string value!")
        if not isinstance(cabin, str):
            raise exception.InvalidArgumentTypeError("The cabin parameter must be a string value!")
        if not isinstance(status, str):
            raise exception.InvalidArgumentTypeError("The status parameter must be a string value!")
        if not isinstance(comment, str):
            raise exception.InvalidArgumentTypeError("The comment parameter must be a string value!")
        if not isinstance(last_updated_datetime, datetime):
            raise exception.InvalidArgumentTypeError("The last_updated_datetime parameter must be a datetime value!")
        
        self.activity_id = activity_id
        self.from_date = from_date
        self.to_date = to_date
        self.original_from_date = original_from_date
        self.original_to_date = original_to_date
        self.shift_pattern_id = shift_pattern_id
        self.shift_pattern_code = shift_pattern_code
        self.rotation_group = rotation_group
        self.rotation_pattern = rotation_pattern
        self.person_id = person_id
        self.person_propeople_id = person_propeople_id
        self.person_first_name = person_first_name
        self.person_last_name = person_last_name
        self.internal_or_external = internal_or_external
        self.job_id = job_id
        self.job_description = job_description
        self.discipline = discipline
        self.job_sort = job_sort
        self.job_emergency_description = job_emergency_description
        self.project_business_unit_report_description = project_business_unit_report_description
        self.rig_site = rig_site
        self.cabin = cabin
        self.status = status
        self.comment = comment
        self.last_updated_datetime = last_updated_datetime

        self.person = f"{self.person_last_name} {self.person_first_name}"

        self.original_shift_pattern = self.get_original_shift_pattern(
            shift_pattern_id = self.shift_pattern_id,
            shift_pattern_code = self.shift_pattern_code
        )
        if self.original_shift_pattern is None:
            self.shift_pattern_days = 0
        else:
            self.shift_pattern_days = len(self.original_shift_pattern)

        self.duration_in_days = self.calculate_duration_in_days(
            from_date = self.from_date,
            to_date = self.to_date
        )

        self.shift_pattern = self.calculate_shift_pattern(
            original_shift_pattern = self.original_shift_pattern,
            original_from_date = self.original_from_date,
            from_date = self.from_date,
            duration_in_days = self.duration_in_days
        )


    def __repr__(self) -> str:
        return f"{self.person} - {self.rig_site} - {self.from_date}-{self.to_date}"


    ############################
    #    P R O P E R T I E S
    ############################


    # ######################
    # #    M E T H O D S
    # ######################

    def get_original_shift_pattern(self,
        shift_pattern_id: int,
        shift_pattern_code: str
    ) -> str:
        """
        Returns the activity's original shift pattern as a string.
        """
        activity_shift_patterns = ActivityShiftPatterns()
        activity_shift_patterns.populate()

        if shift_pattern_id is not None:
            shift_pattern = activity_shift_patterns.get_shift_pattern_by_id(shift_pattern_id)
        elif shift_pattern_code is not None:
            shift_pattern = activity_shift_patterns.get_shift_pattern_by_code(shift_pattern_code)
        else:
            shift_pattern = None

        return shift_pattern


    def calculate_duration_in_days(self,
        from_date: date,
        to_date: date
    ) -> int:
        """
        Returns the actual activity's duration in number of days.
        """
        try:
            # from_date = datetime.strptime(self.from_date, "%Y-%m-%d")
            # to_date = datetime.strptime(self.to_date, "%Y-%m-%d")
            duration = (to_date - from_date).days + 1
            return duration
        except ValueError:
            print("Invalid date format. Unable to calculate duration.")
            return None


    def calculate_shift_pattern(self,
        original_shift_pattern: str,
        original_from_date: date,
        from_date: date,
        duration_in_days: int
    ) -> str:
        """
        Returns the activity's actual shift pattern as a string.
        """
        if original_shift_pattern is None:
            return None
        
        original_pattern_length = len(original_shift_pattern)
        diff_in_days = (from_date - original_from_date).days

        shift_pattern = ""
        for day in range(0, duration_in_days):
            day_number = day + diff_in_days
            day_index = day_number % original_pattern_length
            shift = original_shift_pattern[day_index]
            shift_pattern = shift_pattern + shift
            # print(f"day[{day}] : number={day_number} index={day_index} shift={shift} pattern={shift_pattern}")

        return shift_pattern


    def to_dataframe_row(self) -> pd.DataFrame:
        """
        Returns the activity's properties as a Pandas DataFrame row.
        """
        data = {
            "ActivityID": [self.activity_id],
            "FromDate": [self.from_date],
            "ToDate": [self.to_date],
            "OriginalFromDate": [self.original_from_date],
            "OriginalToDate": [self.original_to_date],
            "ShiftPatternID": [self.shift_pattern_id],
            "ShiftPatternCode": [self.shift_pattern_code],
            "RotationGroup": [self.rotation_group],
            "RotationPattern": [self.rotation_pattern],
            "PersonID": [self.person_id],
            "Person_PropeopleID": [self.person_propeople_id],
            "Person_FirstName": [self.person_first_name],
            "PersonLastName": [self.person_last_name],
            "InternalOrExternal": [self.internal_or_external],
            "JobID": [self.job_id],
            "Job_Description": [self.job_description],
            "Discipline": [self.discipline],
            "JobSort": [self.job_sort],
            "JobEmergencyDescription": [self.job_emergency_description],
            "ProjectBusinessUnitReportDescription": [self.project_business_unit_report_description],
            "RigSite": [self.rig_site],
            "Cabin": [self.cabin],
            "Status": [self.status],
            "Comment": [self.comment],
            "LastUpdatedDatetime": [self.last_updated_datetime],
            "Person": [self.person],
            "ShiftPattern": [self.shift_pattern],
            "OriginalShiftPattern": [self.original_shift_pattern],
        }
        return pd.DataFrame(data)
