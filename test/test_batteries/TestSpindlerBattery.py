import unittest
from datetime import datetime
from batteries.SpindlerBattery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def spindler_needs_service(self):
        current_date = self.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spindler_battery.needs_service())

    def spindler_does_not_need_service(self):
        current_date = self.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spindler_battery.needs_service())

    if __name__ == "__main__":
        unittest.main()