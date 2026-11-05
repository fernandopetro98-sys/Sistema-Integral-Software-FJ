
# Clase abstracta Servicio para Software FJ.

from abc import ABC, abstractmethod


class Servicio(ABC):
    """
    Clase abstracta que representa los servicios
    ofrecidos por la empresa Software FJ.
    """

    def __init__(self, codigo, nombre, tarifa):

        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código del servicio no puede estar vacío.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio no puede estar vacío.")

        if (
            not isinstance(tarifa, (int, float))
            or isinstance(tarifa, bool)
            or tarifa <= 0
        ):
            raise ValueError("La tarifa debe ser un número mayor que cero.")

        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._tarifa = tarifa

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def tarifa(self):
        return self._tarifa

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """Calcula el costo del servicio."""
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        """Valida los parámetros necesarios para utilizar el servicio."""
        pass

    @abstractmethod
    def describir(self):
        """Devuelve una descripción del servicio."""
        pass
