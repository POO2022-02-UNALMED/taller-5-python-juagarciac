from zooAnimales.animal import Animal
class Reptil(Animal):
    listado=[]
    iguanas=0
    serpientes=0
    def __init__(self, nombre, edad, habitat, genero,colorEscamas,largoCola):
        super().__init__(nombre, edad, habitat, genero)
        Animal.reptil+=1
        self.colorEscamas=colorEscamas
        self.largoCola=largoCola
        self.listado.append(self)
    def cantidadReptiles(self):
        return len(self.listado)
    def crearIguana(nombre,edad,sexo):
        Reptil.iguanas+=1
        return Reptil(nombre,edad,"humedal",sexo,"verde",3)
    def crearSerpiente(nombre,edad,sexo):
        Reptil.serpientes+=1
        return Reptil(nombre,edad,"humedal",sexo,"blanco",1)
    def movimiento(self):
        return "reptar"
    def getColorEscamas(self):
        return self.colorEscamas
    def getLargoCola(self):
        return self.largoCola