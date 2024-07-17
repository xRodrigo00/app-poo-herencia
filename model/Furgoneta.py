from model.Vehiculo import Vehiculo

class Furgoneta(Vehiculo):
    def __init__(self, marca, modelo, anio, volumen_carga):
        super().__init__(marca, modelo, anio)
        self.volumen_carga = volumen_carga
    
    def descripcion(self):
        return f"{super().descripcion()}, Volumen de carga: {self.volumen_carga}"