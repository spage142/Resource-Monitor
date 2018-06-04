import SingleTemperatureDisplay as TempDisplay
import Measurements
import MetricDisplayPanel

display1 = TempDisplay.TemperatureDisplay(Measurements.Metric.CPU_PACKAGE_TEMPERATURE)
display2 = TempDisplay.TemperatureDisplay(Measurements.Metric.GPU_TEMPERATURE)

metricPanel = MetricDisplayPanel.DisplayPanel([display1, display2])
metricPanel.printMetrics()