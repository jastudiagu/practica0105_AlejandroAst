cantidad = int(input('Indica la cantidad a invertir: '))
ia = float(input('Indica el interés anual (en %): '))
na = int(input('Indica el número de años: '))


operacion = (cantidad * ia / 100) * na
resultado = cantidad + operacion


print('El capital que obtendras será: ', resultado, '€')