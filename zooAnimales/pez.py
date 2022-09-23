from zooAnimales import animal
from zooAnimales.animal import Animal
class Pez(Animal):
    listado=[]
    salmones=0
    bacalaos=0
    def __init__(self, nombre, edad, habitat, genero,colorEscamas,cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        Animal.pez+=1
        self.colorEscamas=colorEscamas
        self.cantidadAletas=cantidadAletas
        self.listado.append(self)
    def cantidadPeces(self):
        return len(self.listado)
    def crearSalmon(nombre,edad,sexo):
        Pez.salmones+=1
        return Pez(nombre,edad,"oceano",sexo,"rojo",6)
    def crearBacalao(nombre,edad,sexo):
        Pez.bacalaos+=1
        return Pez(nombre,edad,"oceano",sexo,"gris",6)
    def movimiento(self):
        return "nadar"
    def getColorEscamas(self):
        return self.colorEscamas
    def getCantidadAletas(self):
        return self.cantidadAletas