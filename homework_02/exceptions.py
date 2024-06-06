"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    print('Exception! Low fuel!')


class NotEnoughFuel(Exception):
    print('Exception! Not enough fuel!')


class CargoOverload(Exception):
    print('Exception! Cargo overload!')
