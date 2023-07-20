import time

print("=====================")
print("Comparador de números")
print("=====================")
print("  ")

primero = input("Cuál es su primer número? ")
segundo = input("Ok, y su segundo? ")

if primero == str:
    primero1 = input("Disculpa, pero podría repetir?")

elif segundo == str:
    segundo1 = input("Disculpa, pero podría repetir?")
else:
    if primero == segundo:
        print("Sus números son iguales")
    else:
        print("Sus números son diferentes")
    if primero > segundo:
        print("Su primer número,", primero, "es mayor que el segundo,", segundo)
    elif segundo > primero:
        print("Su segundo número,", segundo, "es mayor que el primer número,", primero)

    operacion = input("Desea realizar una operación con los números? ")
    if operacion.lower() == "si" or operacion.lower() == "por supuesto":
        operacion1 = input("Qué tipo de operación desea realizar? ")
        if operacion1.lower() == "suma":
            print(primero + segundo)
        elif operacion1.lower() == "resta":
            print(primero - segundo)
        elif operacion1.lower() == "multiplicación":
            print(primero * segundo)
        elif operacion1.lower() == "división":
            print(primero / segundo)
        else:
            print("Gracias por utilizar esto")
