print("============================")
print("Conversor de texto a número")
print("============================")
print("   ")
print("Si desea cambiar un número escrito pulse 1")
print("Si desea cambiar un número pulse 2")
opcion = input("¿Qué desea hacer? ")
if opcion == "1" or opcion == " 1":
    numero = int(input("¿Qué número? "))
    if numero == 1:
        print("Su número es: UNO")
    elif numero == 2:
        print("Su número es DOS")
    elif numero == 3:
        print("Su número es TRES")
    else:
        print("No reconozco ese número")

elif opcion == "2" or opcion == " 2":
    palabra = input("¿Qué palabra? ")
    if palabra.lower() == "uno":
        print("Su palabra es un 1")
    elif palabra.lower() == "dos":
        print("Su palabra es un 2")
    elif palabra.lower() == "tres":
        print("Su palabra es un 3")
    else:
        print("No reconozco esa palabra")

else:
    opcion1 = input("Disculpa, no entendí. ¿Podría repetir? ")
    if opcion1 == "1" or opcion1 == " 1":
        numero1 = input("¿Qué número? ")
        if numero1 == "1":
            print("Su número es: UNO")
        elif numero1 == "2":
            print("Su número es DOS")
        elif numero1 == "3":
            print("Su número es TRES")
        else:
            print("No reconozco ese número")

    elif opcion1 == "2" or opcion1 == " 2":
        palabra1 = input("¿Qué palabra? ")
        if palabra1.lower() == "uno":
            print("Su palabra es un 1")
        elif palabra1.lower() == "dos":
            print("Su palabra es un 2")
        elif palabra1.lower() == "tres":
            print("Su palabra es un 3")
        else:
            print("No reconozco esa palabra")

    else:
        print("No entiendo esa opción")

