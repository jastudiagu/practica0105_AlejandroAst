di = float(input('Introduce la cantidad de dinero a ingresar: '))

gen1año = di * 0.04

din1año = di + gen1año

din2año = din1año + din1año * 0.04
din3año = din2año + din2año * 0.04

print ('La cantidad de ahorros en el primer años será:', round(din1año, 2), 'en el segundo año', round(din2año, 2), 'y en tercer año', round(din3año,2))