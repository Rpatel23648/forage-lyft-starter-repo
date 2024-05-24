import unittest
from engines.WilloughbyEngine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def engine_needs_service(self):
        current_mileage = 70,000
        last_service_mileage = 0
        willoughbyEngine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(willoughbyEngine.needs_service())

    def engine_does_not_need_service(self):
        current_mileage = 0
        last_service_mileage = 0
        WilloughbyEngine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(WilloughbyEngine.needs_service())

if __name__ == "__main__":
    unittest.main()