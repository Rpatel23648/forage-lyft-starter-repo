from tires.tire import Tires


class OctoprimeTires(Tires):
    def __init__(self, wearLevel):
        self.wearLevel = wearLevel

    def needs_service(self):
        for level in self.wearLevel:
            totalLevel += level
        if totalLevel >= 3:
            return True
        else: 
            return False