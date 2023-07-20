import time

palabra = input("Introduce tu estado (bien o mal):")
time.sleep(1)
print("Lo primero que tengo que decir es que soy una versión de prueba, por lo tanto puedo cometer errores")
time.sleep(2.5)
if "bien" in palabra :
    print("Me alegro")
elif "mal" in palabra:
    print("Qué pena, ¿por qué?")
else:
    respuesta1 = input("No entendí, podrías repetir?:")
    if respuesta1 == "bien":
        print("Me alegro")
    elif respuesta1 == "mal":
        print("Qué pena, ¿por qué?")
    else:
        respuesta2 = input("No entendí, podrías repetir?:")
        if respuesta2 == "bien":
            print("Me alegro")
        elif respuesta2 == "mal":
            print("Qué pena, ¿por qué?")
        else:
            print("No entendí la respuesta. Lo siento.")
time.sleep(0.8)
print ("has llegado al final de la simulación")
time.sleep(0.8)
print ("""gracias por ver, han sido 31 lineas de código""")
time.sleep(0.8)
print ("""y mucho trabajo :D""")