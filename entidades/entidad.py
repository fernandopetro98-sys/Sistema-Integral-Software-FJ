# Clase general para representar las entidades del sistema.

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general
    dentro del sistema Software FJ.
    """

    def __init__(self, identificador):
        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def describir(self):
        """
        Método que deberán implementar las clases hijas.
        """
        pass