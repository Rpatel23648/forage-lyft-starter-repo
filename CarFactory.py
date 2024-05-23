from car import Car
from engines.CapuletEngine import CapuletEngine
from engines.SternmanEngine import SternmanEngine
from engines.WilloughbyEngine import WilloughbyEngine
from batteries.SpindlerBattery import SpindlerBattery
from batteries.NubbinBattery import NubbinBattery


class CarFactory:
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        calliope_car = Car(capulet_engine, spindler_battery)
        return calliope_car

    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        glissade_car = Car(willoughby_engine, spindler_battery)
        return glissade_car

    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        palindrome_car = Car(sternman_engine, spindler_battery)
        return palindrome_car

    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        rorschach_car = Car(willoughby_engine, nubbin_battery)
        return rorschach_car

    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        thorvex_car = Car(capulet_engine, nubbin_battery)
        return thorvex_car