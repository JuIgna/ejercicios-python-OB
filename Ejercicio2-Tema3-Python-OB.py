#Ejercicio 2 del tema 3 del Cursod de Python -- OpenBootcamp
peso = float (input ("Ingrese peso en kg"))
estatura = float (input ("Ingrese estatura en metros"))
indice_masa_corporal = peso/(estatura*estatura)

print ("El Indice de Masa Corporal es: " + str (round(indice_masa_corporal,2)))
input ()