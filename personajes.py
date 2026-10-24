from abc import ABC, abstractmethod
import math

class Personaje(ABC):
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, v):
        if not isinstance(v, str) or not v.strip():
            raise ValueError("Nombre vacío")
        self.__nombre = v.strip()

    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self, v):
        if not isinstance(v, int) or v < 0 or v > 100:
            raise ValueError("Vida debe ser 0-100")
        self.__vida = v

    @property
    def ataque(self):
        return self.__ataque
    @ataque.setter
    def ataque(self, v):
        if not isinstance(v, int) or v <= 0:
            raise ValueError("Ataque debe ser > 0")
        self.__ataque = v

    @property
    def defensa(self):
        return self.__defensa
    @defensa.setter
    def defensa(self, v):
        if not isinstance(v, int) or v < 0:
            raise ValueError("Defensa debe ser >= 0")
        self.__defensa = v

    def recibir_danio(self, cantidad):
        if cantidad < 0:
            raise ValueError("Daño no puede ser negativo")
        efectivo = min(cantidad, self.__vida)
        self.__vida = max(0, self.__vida - cantidad)
        return efectivo

    def esta_vivo(self):
        return self.__vida > 0

    def mostrar_estado(self):
        return f"{self.__class__.__name__} {self.nombre} | Vida:{self.vida} Atq:{self.ataque} Def:{self.defensa}"

    @abstractmethod
    def atacar(self, objetivo):
        pass

    def _validar_ataque(self, objetivo):
        if not isinstance(objetivo, Personaje):
            raise TypeError("Objetivo debe ser
