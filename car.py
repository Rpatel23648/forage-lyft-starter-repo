from engines.engine import Engine
from batteries.battery import Battery
from tires.tire import Tires
from Serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tires: Tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        if self.battery.needs_service() and self.engine.needs_service() and self.tires.needs_service():
            return True
        else:
            return False
