#Variables
shipping_cost_per_kg = 1.20
customer_basket_cost = 34
customer_basket_weight = 44
#problema: si el consumidor gasta 100 euros o más, el envío es gratis.
# si el envío es inferior a 100, el gasto de envío son 1.20 euros/kg
if 100 <= customer_basket_cost:
    shipping_cost_per_kg = 0
    print ("Coste del envío:"+ str (shipping_cost_per_kg))
    print("Coste total:" + str(customer_basket_cost + shipping_cost_per_kg) )
else:
    shipping_cost_per_kg = customer_basket_weight * shipping_cost_per_kg
    print("Coste del envío:" + str(shipping_cost_per_kg))
    print("Coste total:" + str(customer_basket_cost + shipping_cost_per_kg) )
print(" ")
#hacemos el problema sustituyendo la variable customer_basket_cost por 101
#Variables
shipping_cost_per_kg = 1.20
customer_basket_cost = 101
customer_basket_weight = 44
if 100 <= customer_basket_cost:
    shipping_cost_per_kg = 0
    print("Coste del envío:" + str(shipping_cost_per_kg))
    print("Coste total:" + str(customer_basket_cost + shipping_cost_per_kg) )
else:
    shipping_cost_per_kg = customer_basket_weight * shipping_cost_per_kg
    print("Coste del envío:" + str(shipping_cost_per_kg))
    print("Coste total:" + str(customer_basket_cost + shipping_cost_per_kg) )
print()