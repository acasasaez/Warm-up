# Crear un for loop que muestre los números [0-50]
for i in range(51):
    print(i)
# Generador de números aleatoreos:
import random
a= 0
b= 50
edad= random.randrange(a,b)
hambre=edad
dinero =2000
helados_consumidos = 0
precio_helado =100
while (hambre) < 85 and (dinero-precio_helado) > 0 :
    dinero = dinero - precio_helado
    precio_helado = precio_helado + (precio_helado *0.2)
    helados_consumidos = helados_consumidos + 1
    hambre = hambre + edad
    if (hambre + edad) >= 100:
    	break
print ("Helados consumidos:" +str(helados_consumidos) )
print("Dinero restante:" + str(dinero))
print("Nivel de saciedad:" +str(hambre))
   

