# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda


# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print('El texto mayor es: ',texto_1)
elif texto_2 > texto_1:
    print('El texto mayor es: ',texto_2)
else:
    print('Son iguales')

cant_1 = len(texto_1)
cant_2 = len(texto_2)
if cant_1 > cant_2:
    print('La palabra mas grande es: ',cant_1)
elif cant_2 > cant_1:
    print('La palabra mas grande es: ',cant_2)
else:
    print('Son igual de largas las dos palabras')

prime_1 = texto_1[-1]
prime_2 = texto_2[-1]
if prime_1 > prime_2:
    print('De la letra ',prime_1,'y',prime_2,'el mayor es',prime_1)
elif prime_2 > prime_1:
    print('De la letra',prime_1,'y',prime_2,'el mayor es',prime_2)
else:
    print('la letra',prime_1,'y',prime_2,'son iguaes')

if copia_texto_1 == texto_1:
    print('Copia_texto1 y texto1 Son iguales')
else:
    print('Copia_texto1 y texto1 No son iguales')