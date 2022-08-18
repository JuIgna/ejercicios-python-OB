# Numeros Impares desde un rango

nro_inicio = int (input ("Ingrese el numero de inicio"))
nro_final = int (input ("Ingrese el numero final"))

for nro in range (nro_inicio, nro_final):
    if (nro % 2 != 0):
        print ("El numero es impar: ", nro)


input ()