import MetricDisplay
from Measurements import TemperatureMetric, UsageMetric, TemperatureUnit

class TemperatureDisplay(MetricDisplay.Display):
    
    def __init__(self, performanceMetric, temperatureUnit=TemperatureUnit.CELSIUS):
        """initializes an TemperatureDisplay instance
        argument performanceMetric: a Metric enum to use. Must be a temperature type.
        argument temperatureUnit: the temperature unit to use. Defaults to Celsius, but can be Fahrenheit. """

        super().__init__(self, performanceMetric)
        self._temperatureUnit = temperatureUnit


    #getters and setters
    def getPerformanceMetric(self):
        """returns the performance metric being monitored by the Display object
        return: Metric enum"""

        return self._performanceMetric

    def setPerformanceMetric(self, performanceMetric):
        """sets the performance metric to monitor"""

        #throw ValueError if not a temperature
        if isinstance(performanceMetric, TemperatureMetric):
            self._performanceMetric = performanceMetric
        else:
            raise ValueError("Metric arg not a temperature. performanceMetric.value must be >= 100 and < 200")

    def getTemperatureUnit(self):
        """returns the temperature unit to use
        return: a TemperatureUnit metric"""

        return self._temperatureUnit
    
    def setTemperatureUnit(self, temperatureUnit):
        """sets the temperature unit to use"""
        if isinstance(temperatureUnit, temperatureUnit):
            self._temperatureUnit = temperatureUnit
        else:
            raise ValueError("Passed enum MUST be a TemperatureUnit")

    temperatureUnit = property(getTemperatureUnit, setTemperatureUnit)
    performanceMetric = property(getPerformanceMetric, setPerformanceMetric)