import unittest
from Date import Date


class TestDate(unittest.TestCase):
    def setUp(self) -> None:
        self.dt = Date(2019, 9, 15)

    def test_is_leap_year(self):
        self.dt = Date(2019, 9, 1)
        self.assertTrue(self.dt.is_leap_year(2020))
        self.assertTrue(self.dt.is_leap_year(2000))
        self.assertFalse(self.dt.is_leap_year(2019))
        self.assertFalse(self.dt.is_leap_year(2100))

    def test_get_max_day(self):
        self.assertEqual(self.dt.get_max_day(2020, 2), 29)
        self.assertEqual(self.dt.get_max_day(2019, 2), 28)
        self.assertEqual(self.dt.get_max_day(2020, 1), 31)
        self.assertEqual(self.dt.get_max_day(2020, 11), 30)
        self.assertEqual(self.dt.get_max_day(2020, 12), 31)

    def test_add_year(self):
        self.dt.add_year(1)
        self.assertEqual(repr(self.dt), 'Date(2020, 9, 15)')
        self.dt.add_year(11)
        self.assertEqual(repr(self.dt), 'Date(2031, 9, 15)')

    def test_add_month(self):
        self.dt.add_month(3)
        self.assertEqual(repr(self.dt), 'Date(2019, 12, 15)')
        self.dt.add_month(5)
        self.assertEqual(repr(self.dt), 'Date(2020, 5, 15)')

    def test_add_day(self):
        self.dt.add_day(5)
        self.assertEqual(repr(self.dt), 'Date(2019, 9, 20)')
        # self.dt.add_day(20)
        # self.assertEqual(repr(self.dt), 'Date(2019, 10, 10)')
        # self.dt.add_day(30)
        # self.assertEqual(repr(self.dt), 'Date(2019, 11, 9)')
        # self.dt.add_day(61)
        # self.assertEqual(repr(self.dt), 'Date(2020, 1, 9)')

    def test_date2_date1(self):
        pass
