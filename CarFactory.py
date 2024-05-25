from car import Car
from engines.CapuletEngine import CapuletEngine
from engines.SternmanEngine import SternmanEngine
from engines.WilloughbyEngine import WilloughbyEngine
from batteries.SpindlerBattery import SpindlerBattery
from batteries.NubbinBattery import NubbinBattery
from tires.OctoprimeTires import OctoprimeTires
from tires.CarriganTires import CarriganTires


class CarFactory:
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_level):
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        carrigan_tires = CarriganTires(tire_wear_level)
        calliope_car = Car(capulet_engine, spindler_battery, carrigan_tires)
        return calliope_car

    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_level):
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        octoprime_tires = OctoprimeTires(tire_wear_level)
        glissade_car = Car(willoughby_engine, spindler_battery, octoprime_tires)
        return glissade_car

    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_on, tire_wear_level):
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        carrigan_tires = CarriganTires(tire_wear_level)
        palindrome_car = Car(sternman_engine, spindler_battery)
        return palindrome_car

    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_level):
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        octoprime_tires = OctoprimeTires(tire_wear_level)
        rorschach_car = Car(willoughby_engine, nubbin_battery, octoprime_tires)
        return rorschach_car

    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_level):
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        carrigan_tires = CarriganTires(tire_wear_level)
        thorvex_car = Car(capulet_engine, nubbin_battery)
        return thorvex_car