__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

class camion:
    def__init__(self,matricula,capacidad:int, consumo: float):

    self.__matricula = matricula
    self.__capacidad = capacidad
    self.__consumo = consumo
    self.__cargaActual = 0

    def darCapacidad(self):
        return self.__capacidad

    def darConsumo(self):
        return self.__consumo

    def darMatricula(self):
        return self.__matricula

    def darCargaActual(self):
        return self.__cargaActual
    def cargar(self,carga):
        if (carga > 0 & carga <= self.darCapacidad()-self.darCargaActual()):
            self.__cargaActual-carga