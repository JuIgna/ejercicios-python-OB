class Vehiculo:
    color = "rojo"
    ruedas = 4
    puerta = 4
class Coche (Vehiculo):
    velocidad = 180
    cilindrdada = 4

coche = Coche ()
print ("Color: ", coche.color)
print ("Ruedas: ", coche.ruedas)
print  ("Puertas: ", coche.puerta)
print ("Velocidad: ", coche.velocidad)
print ("Cilindrada: ", coche.cilindrdada)

