import time
#ejercicio2.py
print ("++++++++++++++++++++++++++++")
time.sleep (0.5)
print ("¿Cuál es el numero más alto?")
time.sleep (0.5)
print ("""++++++++++++++++++++++++++++
       """)
time.sleep (0.5)
primer= int(input("¿Cuál es su primer numero?"))
segundo= int(input("¿Cuál es su segundo numero?"))
tercero= int(input("¿Cuál es su tercero numero?"))
r= "El numero más grande es:"
if primer>segundo and primer>tercero:
    print (r,primer)
elif segundo>primer and segundo>tercero:
    print (r,segundo)
elif tercero>primer and tercero>segundo:
    print (r,tercero)
else:
    print ("Error, en sus numeros hay dos o más iguales, intentelo de nuevo")
