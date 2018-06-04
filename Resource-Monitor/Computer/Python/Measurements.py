from enum import Enum, auto, unique

@unique
class Metric(Enum):
    """This enum determines which performance metric for each instance of a Display to use"""
    
    #TODO allow for temperature measurements to be differentiated
    #temperatures: 1xx
    #usage: 2xx
    #others: 9xx

    CPU_PACKAGE_TEMPERATURE = 100
    CPU_CORE_AVERAGE_TEMPERATURE = 101
    CPU_USAGE_PERCENT = 200
    GPU_USAGE_PERCENT = 201
    GPU_TEMPERATURE = 102
    RAM_USAGE_PERCENT = 202
    NETWORK_THROUGHPUT = 203
    DISK_USAGE_PERCENT = 204

    MOTHERBOARD_TEMPERATURE = 103

class TemperatureUnit(Enum):
    CELSIUS = auto()
    FAHRENHEIT = auto()