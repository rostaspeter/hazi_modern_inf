import math
import unittest

class Haromszog:
    def __init__(self, a:float, b:float, c:float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def Kerulet(self) -> float:
        return self.a + self.b + self.c
    
    def Terulet(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def __Szerkesztheto(self) -> bool:
        return self.a + self.b > self.c and self.c + self.b > self.a and self.a + self.c > self.b
    
    def SetA(self, a) -> None:
        eredeti = self.a
        self.a = a
        if not self.__Szerkesztheto():
            self.a = eredeti
            raise NemSzerkesztheto()

    def SetB(self, b) -> None:
        eredeti = self.b
        self.b = b
        if not self.__Szerkesztheto():
            self.b = eredeti
            raise NemSzerkesztheto()

    def SetC(self, c) -> None:
        eredeti = self.c
        self.c = c
        if not self.__Szerkesztheto():
            self.c = eredeti
            raise NemSzerkesztheto()
        
class NemSzerkesztheto(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
