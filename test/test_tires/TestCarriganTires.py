import unittest
from tires.CarriganTires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def tires_need_service(self):
        wearlevel = [0.1, 0.2, 0.3, 1]
        carriganTires = CarriganTires(wearlevel)
        self.assertTrue(carriganTires.needs_service())

    def tires_not_need_service(self):
        wearlevel = [.1, .2, .3, .4]
        carriganTires = CarriganTires(wearlevel)
        self.assertTrue(carriganTires.needs_service())

if __name__ == "__main__":
    unittest.main()