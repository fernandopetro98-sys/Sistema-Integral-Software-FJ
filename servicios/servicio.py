# Clase abstracta Servicio para el sistema Software FJ.

from abc import ABC, abstractmethod


def es_numero(valor):
    """True si el valor es int o float, excluyendo booleanos."""
    return isinstance(valor, (int, float)) and not isinstance(valor, bool)


def es_entero_positivo(valor):
    """True si el valor es un entero mayor que cero, excluyendo booleanos."""
    return isinstance(valor, int) and not isinstance(valor, bool) and valor > 0


class Servicio(ABC):
    """Clase base de los servicios ofrecidos por Software FJ."""

    def __init__(self, codigo, nombre, tarifa):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código del servicio no puede estar vacío.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio no puede estar vacío.")

        if not es_numero(tarifa) or tarifa <= 0:
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

    def validar_parametros(self, duracion):
        """Valida la duración del servicio."""
        if not es_numero(duracion) or duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero.")
        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """Calcula el costo del servicio con impuesto y descuento opcionales."""
        self.validar_parametros(duracion)

        if not es_numero(impuesto) or not 0 <= impuesto <= 1:
            raise ValueError("El impuesto debe estar entre 0 y 1.")

        if not es_numero(descuento) or not 0 <= descuento <= 1:
            raise ValueError("El descuento debe estar entre 0 y 1.")

        subtotal = self.tarifa * duracion
        total = subtotal + (subtotal * impuesto)
        total = total - (total * descuento)

        return round(total, 2)

    @abstractmethod
    def describir(self):
        """Describe las características del servicio."""
        pass
