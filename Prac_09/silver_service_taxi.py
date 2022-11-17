"""
CP1404/CP5632 Practical - Silver Service Taxi - Wesley Gilsenan

"""

from Prac_09.Taxi import Taxi


class SilverServiceTaxi(Taxi):

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

