edad_minima = 18
edad_maxima = 50
pregunta = "dime tu edad "
edad = int(input(pregunta))

if (edad >= edad_minima and edad <= edad_maxima):
    print("edad >= edad_minima --> " +str(edad >= edad_minima))
    print("edad <= edad_maxima --> " +str(edad <= edad_maxima))
    print("edad >= edad_minima and edad <= edad_maxima " + str(edad >= edad_minima and edad <= edad_maxima))
    print("entras")
elif(edad >= edad_maxima):
    print("no entras por mayor")
else:
    print("no entras niñato")
