import unittest
from engines.SternmanEngine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def engine_needs_service(self):
        warning_light_on = True
        sternmanEngine = SternmanEngine(warning_light_on)
        self.assertTrue(sternmanEngine.needs_service())

    def engine_does_not_need_service(self):
        warning_light_on = False
        sternmanEngine = SternmanEngine(warning_light_on)
        self.assertTrue(sternmanEngine.needs_service())

if __name__ == "__main__":
    unittest.main()