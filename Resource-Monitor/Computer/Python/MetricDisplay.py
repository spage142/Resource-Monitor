from abc import ABC, abstractmethod

class Display(ABC):
    """Display class"""
    
    def __init__(self, performanceMetric):
        self.performanceMetric = performanceMetric

    @abstractmethod
    def setPerformanceMetric(self, performanceMetric):
        self.performanceMetric = performanceMetric
    
    @abstractmethod
    def getPerformanceMetric(self):
        return self.performanceMetric