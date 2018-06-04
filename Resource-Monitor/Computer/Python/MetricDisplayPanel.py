
class DisplayPanel():

    def __init__(self, displayPanels = []):
        
        self.displayPanels = displayPanels

    def printMetrics(self):
        """prints the metric that each panel in the display measures"""
        for panel in self.displayPanels:
            print(panel.getPerformanceMetric())