from zooAnimales.animal import Animal
class Ave(Animal):
    listado=[]
    halcones=0
    aguilas=0
    def __init__(self, nombre, edad, habitat, genero,colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        Animal.ave+=1
        self.colorPlumas=colorPlumas
        self.listado.append(self)
    def cantidadAves(self):
        return len(self.listado)
    def crearHalcon(nombre,edad,sexo):
        Ave.halcones+=1
        return Ave(nombre,edad,"montanas",sexo,"cafe glorioso")
    def crearAguilas(nombre,edad,sexo):
        Ave.aguilas+=1
        return Ave(nombre,edad,"montanas",sexo,"blanco y amarillo")
    def movimiento(self):
        return "volar"
    def getColorPlumas(self):
        return self.colorPlumas