#Queremos crear un programa que nos avise cuando el valo de nuestras bitcoin caiga por debajo de 30000.
def bitcoinToEuros (bitcoin_amount, bitcoin_value_euros):
    return bitcoin_amount * bitcoin_value_euros

investment_in_bitcoin = 1.2
bitcoin_to_eur = 40000

money = bitcoinToEuros (investment_in_bitcoin,bitcoin_to_eur)

if money < 30000:
    print ("Te estás quedando pobre")
else:
    print ("Tu dinero está a salvo")

bitcoin_to_eur = 25000
money = bitcoinToEuros (investment_in_bitcoin,bitcoin_to_eur)

if money < 30000:
    print ("Te estás quedando pobre")
else:
    print ("Tu dinero está a salvo")