#Queremos crear un progrma que nos permita comer helados hasta saciar nuestra hambre o hasta quedarnos sin dinero:
#Partimos de:
    #Tenemos 2000 euros inicialmente.
    #El precio del helado es 100, pero se incrementa un 20% después de cada compra
    #Incialmente estamos tan saciados como nuestra edad nos lo indica, cada vez que tomamos un helado nos saciamos lo que indica nuestra edad.
    #Paraestar satisfechos nuestra saciedad tiene que estar en un rango ente 85 y 100.
print("Hello, World!")
edad=18
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
   
