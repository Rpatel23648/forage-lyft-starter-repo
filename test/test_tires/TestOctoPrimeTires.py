import unittest
from tires.OctoprimeTires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def tires_need_service(self):
        wearlevel = [.9, .8, .3, 1]
        octoprimeTires = OctoprimeTires(wearlevel)
        self.assertTrue(octoprimeTires.needs_service())

    def tires_not_need_service(self):
        wearlevel = [.1, .2, .3, .4]
        octoprimeTires = OctoprimeTires(wearlevel)
        self.assertTrue(octoprimeTires.needs_service())

if __name__ == "__main__":
    unittest.main()