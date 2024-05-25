from tires.tire import Tires


class CarriganTires(Tires):
    def __init__(self, wearLevel):
        self.wearLevel = wearLevel
    
    def needs_service(self):
        return any(wear >= 0.9 for wear in self.wearLevel)