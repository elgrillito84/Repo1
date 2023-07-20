import time
print ("--------------------------------------------")
print ("Tu programa personal pera asistencia laboral")
print ("--------------------------------------------")
n= input ("¿Cuál es tu nombre?")
c= int(input ("¿Cuál es tu clave?"))
a=int(input("¿Y tu antiguedad?"))
print("entendido procesando los datos...")
time.sleep (0.7)
print ("su nombre es:", n)
time.sleep (0.7)
if c==1:
    print("Departamento Atención al cliente")
elif c==2:
    print ("Departamento Gerencia")
elif c==3:
    print ("Departamento EL PEPE")
else:
    print("Tu clave de departamento no se ha podido identificar, intentelo de nuevo")
if c==1:
   clave1="Usted es del departamento Atención al cliente, y por tanto tiene derecho a"
   if a==1:
         print (clave1, "5 días de vacaciones")
   elif a>=2 and a<=5:
        print (clave1, "10 días de vacaciones")   
   elif a>=6:
        print (clave1, "20 días de vacaciones")   
   else:
        print ("Disculpa, ha haido un error intentelo de nuevo")
elif c==2:
     clave1="Usted es del departamento Gerencia, y por tanto tiene derecho a"
     if a==1:
       print (clave1, "10 días de vacaciones")
     elif a>=2 and a<=5:
        print (clave1, "15 días de vacaciones")   
     elif a>=6:
        print (clave1, "30 días de vacaciones")   
     else:
        print ("Disculpa, ha habido un error intentelo de nuevo")
elif c==3:
     clave1="Usted es del departamento EL PEPE, y por tanto tiene derecho a"
     if a==1:
       print (clave1, "15 días de vacaciones")
     elif a>=2 and a<=5:
        print (clave1, "18 días de vacaciones")   
     elif a>=6:
        print (clave1, "33 días de vacaciones")   
     else:
        print ("Disculpa, ha habido un error intentelo de nuevo")
if a<1:
    print ("Disculpa, parece ser que su antiguedad genera algún error, por favor, vuelva a introducir los datos")
time.sleep (0.7)
print ("Gracias por utilizar este programa, no dude en contactarnos si hay algún problema")