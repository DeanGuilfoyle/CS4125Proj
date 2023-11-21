# observer/subject.py

from abc import ABC, abstractmethod

# Subject
class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self, message: str):
        pass

# Concrete Subject
class PromotionService(Subject):
    def __init__(self):
        self.observers = set()

    def attach(self, observer):
        self.observers.add(observer)

    # no implementation for detach
    def detach(self, observer):
        self.observers.discard(observer)

    def notify(self, message: str):
        for observer in self.observers:
            observer.update(message)
