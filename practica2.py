import math

print("\nDatos  para la primera opcion")
valor1 = float(input("Cantidad a ganar:\t"))
pbd1 = float(input("Probabilidad de ganar:\t"))
valor2 = float(input("Cantidad a perder:\t"))
pbd2 = float(input("Probabilidad de perder:\t"))

print("\nDatos para la segunda opcion\n")
valorA = float(input("Cantidad a ganar:\t"))
pbdA = float(input("Probabilidad de ganar:\t"))
valorB = float(input("Cantidad a perder:\t"))
pbdB = float(input("Probabilidad de perder:\t"))

print("\nLa primera opcion es:\nGanar ", valor1," con ", pbd1, " de probabilidad o perder ", valor2, " con ", pbd2, " de probabilidad \n")
print("\nLa segunda opcion es:\nGanar ", valorA," con ", pbdA, " de probabilidad o perder ", valorB, " con ", pbdB, " de probabilidad \n")

rzc = (valor1**2)
rzc1 =(valor2**2)
UE1 = round( ((pbd1)*(pow (rzc,1/3))) + ((pbd2)*(pow (rzc1,1/3))) , 3)
print("El resultado de la utilidad esperada de la opcion uno es:",UE1)


raizc= (valorA**2)
raizc1 =(valorB**2)
UE2 = round(((pbdA)*(pow (raizc,1/3))) + ((pbdB)*(pow (raizc1,1/3))),3)
print("El resultado de utilidad esperada de la opcion dos es: ", UE2)
round (UE2,2)

if(UE1>UE2):
	print("\n Mejor resultado con gran utilidad es:-> PRIMERA OPCION")
else:
	print("\n Mejor resultado con gran utilidad es:-> SEGUNDA OPCION")
