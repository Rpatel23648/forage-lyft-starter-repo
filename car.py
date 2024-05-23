from engines.engine import Engine
from batteries.battery import Battery
from Serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        if self.battery.needs_service() and self.engine.needs_service():
            return True
        else:
            return False
