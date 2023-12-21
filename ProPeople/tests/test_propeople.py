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
from activity_date import ActivityDate
from activity_dates import ActivityDates
import propeople


class ProPeopleTestCase(unittest.TestCase):

    def test_propeople_create_activity_date_table(self):

        activities = Activities()
        activities.populate()
        activities.list_activities()

        activity_dates = propeople.create_activity_date_table(activities)
        activity_dates.list_activity_dates()

        activities.activities_df.to_csv('activities.csv', index=False)
        activity_dates.activity_dates_df.to_csv('activity_dates.csv', index=False)


# if __name__ == '__main__':
#     unittest.main()

tests = ProPeopleTestCase()
tests.test_propeople_create_activity_date_table()
