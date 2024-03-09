class Sensor:
    """Base class for glove sensors"""

    def get_value(
        self, order: list | tuple = []
    ) -> tuple[int | float | list, list]:
        """Get the value of the sensor"""
        raise NotImplementedError