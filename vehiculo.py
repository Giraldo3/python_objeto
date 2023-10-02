class vehiculo:
    def __init__(self, velocidad_max, marca):
        self.velocidad = 0
        self.velocidad_max = velocidad_max
        self.marca = marca

    def setvelocidad(self, cant):
        if self.velocidad + cant > self.velocidad_max:
            self.velocidad = self.velocidad_max
        else:
            self.velocidad += cant
        if self.velocidad < 0:
            self.velocidad = 0

    def getvelocidad(self):
        return self.velocidad



Autos = {}
while True:
    Marca = input("Ingresa la marca del auto o 'n' para terminar: ")
    if Marca.lower() == 'n':
        break
    Velocidad = float(input("Ingresa la velocidad máxima del auto: "))
    
    Autos[Marca] = Velocidad

marca_buscar = input("Ingresa la marca del auto: ")
if marca_buscar in Autos:
   vl = Autos[marca_buscar]
else:
    print(f"No se encontró información para la marca {marca_buscar}")

g = vehiculo(vl, marca_buscar)  

opc = 0
while opc != 5:
    opc = int(input("1.Acelerar, 2.Mostrar, 3.Dejar de acelerar, 5.Salir: "))
    if opc == 1:
        g.setvelocidad(15)
    elif opc == 2:
        vel = g.getvelocidad()
        print(f"El vehículo de la marca {g.marca} va a una velocidad de {vel} KM/h")
    elif opc == 3:
        g.setvelocidad(-15)
