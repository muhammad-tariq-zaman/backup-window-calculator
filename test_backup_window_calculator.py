import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import window_hours, per_week


class TestRpo(unittest.TestCase):
    def test_daily_window(self):
        self.assertEqual(window_hours(24), 24)

    def test_daily_per_week(self):
        self.assertEqual(per_week(24), 7)

    def test_hourly_per_week(self):
        self.assertEqual(per_week(1), 168)
