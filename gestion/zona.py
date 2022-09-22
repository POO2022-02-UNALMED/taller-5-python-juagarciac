class Zona:
    numero=0
    def __init__(self,nombre,zoo=None):
        self.nombre=nombre
        self.zoo=zoo
        self.animales=[]
        self.zoo=zoo
    def getZoo(self):
        return self.zoo
    def agregarZoo(self,zoo):
        self.zoo=zoo
    def agregarAnimales(self,animales):
        self.numero+=1
        self.animales+=animales
    def cantidadAnimales(self):
        return self.numero
    def getNombre(self):
        return self.nombre
    
