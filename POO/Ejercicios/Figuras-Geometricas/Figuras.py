"""
    Realizar un programa que me permita calcular áreas y perímetros de figuras geométricas
    aplicando POO.
"""

from abc import ABC, abstractmethod
from math import pi

from numpy import percentile 

class Figuras(ABC):
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Cuadrado(Figuras):
    def __init__(self, lado: float):
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2

class Circulo(Figuras):
    def __init__(self, radio: float):
        self.radio = radio

    def perimetro(self):
        return 2 * self.radio * pi

    def area(self):
        return pi * (self.radio ** 2)