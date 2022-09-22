from zooAnimales.animal import Animal
class Anfibio(Animal):
    listado=[]
    ranas=0
    salamandras=0
    def __init__(self, nombre, edad, habitat, genero,colorPiel,venenoso):
        super().__init__(nombre, edad, habitat, genero)
        Animal.anfibio+=1
        self.colorPiel=colorPiel
        self.venenoso=venenoso
        self.listado.append(self)
    def cantidadAnfibios(self):
        return len(self.listado)
    def crearRana(self,nombre,edad,sexo):
        self.ranas+=1
        return Anfibio(nombre,edad,"selva",sexo,"rojo",True)
    def crearSalamandra(self,nombre,edad,sexo):
        self.salamandras+=1
        return Anfibio(nombre,edad,"selva",sexo,"negro y amarillo",False)
    def movimiento(self):
        return "saltar"
    def getColorPiel(self):
        return self.colorPiel
    def isVenenoso(self):
        return self.venenoso