import MetricDisplay
from Measurements import TemperatureUnit as tempUnit

class TemperatureDisplay(MetricDisplay.Display):
    
    def __init__(self, performanceMetric, temperatureUnit=tempUnit.CELSIUS):
        """initializes an TemperatureDisplay instance
        argument performanceMetric: a Metric enum to use. Must be a temperature type.
        argument temperatureUnit: the temperature unit to use. Defaults to Celsius, but can be Fahrenheit. """

        super().__init__(self, performanceMetric)
        self.temperatureUnit = temperatureUnit


    #getters and setters
    def getPerformanceMetric(self):
        """returns the performance metric being monitored by the Display object
        return: Metric enum"""

        return self.performanceMetric

    def setPerformanceMetric(self, performanceMetric):
        """sets the performance metric to monitor"""

        #throw ValueError if not a temperature
        if performanceMetric.value >= 100 and performanceMetric.value < 200:
            self.performanceMetric = performanceMetric
        else:
            raise ValueError("Metric arg not a temperature. performanceMetric.value must be >= 100 and < 200")

    def getTemperatureUnit(self):
        """returns the temperature unit to use
        return: a TemperatureUnit metric"""

        return self.temperatureUnit
    
    def setTemperatureUnit(self, temperatureUnit):
        """sets the temperature unit to use"""

        self.temperatureUnit = temperatureUnit