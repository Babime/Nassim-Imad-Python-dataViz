from .enums import Division, Tier

class Rank():
    def __init__(self, tier : Tier = None, division : Division = None):
        self.tier = tier
        self.division = division

    def __str__(self):
        return f'{self.tier.name} {self.division.name}'
    
    def __eq__(self, other):
        return self.tier == other.tier and self.division == other.division
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        if self.tier == other.tier:
            return self.division < other.division
        return self.tier < other.tier
    
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        if self.tier == other.tier:
            return self.division > other.division
        return self.tier > other.tier
    
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)
    
    