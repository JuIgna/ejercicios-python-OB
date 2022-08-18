def es_numeroPrimo (numero):
    if (numero==1):
        return False
    for modulo in range (2,10):
        if ((numero%modulo==0) and numero!=modulo ):
            return False

    return True


nro = int (input ("Ingrese numero: "))
if (es_numeroPrimo (nro) == True):
    print ("El numero es primo")
else:
    print ("El numero no es primo ")


