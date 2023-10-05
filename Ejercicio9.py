cantidad = int(input('Indica la cantidad a invertir: '))
ia = float(input('Indica el interés anual (en %): '))
na = int(input('Indica el número de años: '))

for i in range(na):
    cantidad = cantidad + cantidad * (ia/100)

print('El capital que obtendras será: ', cantidad, '€')