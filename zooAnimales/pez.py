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
    def crearSalmon(self,nombre,edad,sexo):
        self.salmon+=1
        return Pez(nombre,edad,"oceano",sexo,"rojo",6)
    def crearBacalao(self,nombre,edad,sexo):
        self.bacalao+=1
        return Pez(nombre,edad,"oceano",sexo,"gris",6)
    def movimiento(self):
        return "nadar"
    def getColorEscamas(self):
        return self.colorEscamas
    def getCantidadAletas(self):
        return self.cantidadAletas