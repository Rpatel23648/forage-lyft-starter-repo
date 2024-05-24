import unittest
from engines.CapuletEngine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def engine_needs_service(self):
        current_mileage = 40,000
        last_service_mileage = 0
        capuletEngine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(capuletEngine.needs_service())

    def engine_does_not_need_service(self):
        current_mileage = 0
        last_service_mileage = 0
        capuletEngine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(capuletEngine.needs_service())

if __name__ == "__main__":
    unittest.main()