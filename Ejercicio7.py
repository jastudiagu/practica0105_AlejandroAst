peso = float(input('Escribe tu peso en kg'))
estatura = float(input('Escribe tu estatura en metros'))
imc = peso/(estatura**2)
print('Tu índice de masa corporal es:', round(imc, 2))