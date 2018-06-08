from enum import Enum, auto, unique

@unique
class TemperatureMetric(Enum):
    """This enum is used for Temperature metrics"""
    CPU_PACKAGE_TEMPERATURE = auto()
    CPU_CORE_AVERAGE_TEMPERATURE = auto()
    GPU_TEMPERATURE = auto()
    MOTHERBOARD_TEMPERATURE = auto()
    
@unique
class UsageMetric(Enum):
    """This enum is used for Usage metrics"""
    CPU_USAGE_PERCENT = auto()
    GPU_USAGE_PERCENT = auto()
    RAM_USAGE_PERCENT = auto()
    NETWORK_THROUGHPUT = auto()
    DISK_USAGE_PERCENT = auto()

@unique
class TemperatureUnit(Enum):
    """This enum is used for determining the temperature unit (Fahrenheit or Celsius) to use"""
    CELSIUS = auto()
    FAHRENHEIT = auto()