from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area():
        pass

class Rectanguler(Shape):
    @staticmethod
    def area(l, b, h):
        return l * b * h

rec = Rectanguler()
print(rec.area(1, 2, 3))