# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

tem_1 = int(input('Ingresar la temperatura dia 1: '))
tem_2 = int(input('Ingresar la temperatura dia 2: '))
tem_3 = int(input('Ingresar la temperatura dia 3: '))

if tem_1 > tem_2 and tem_1 > tem_3:
    print('La temperatura mayor es:',tem_1)
elif tem_2 > tem_1 and tem_2 > tem_3:
    print('La temperatura mayor es:',tem_2)
elif tem_3 > tem_1 and tem_3 > tem_2:
    print('La temperatura mayor es:',tem_3)
else:
    print('La temperatura mayor es:',tem_1)

if tem_1 < tem_2 and tem_1 < tem_3:
    print('La temperatura menor es:',tem_1)
elif tem_2 < tem_1 and tem_2 < tem_3:
    print('La temperatura menor es:',tem_2)
elif tem_3 < tem_1 and tem_3 < tem_2:
    print('La temperatura menor es:',tem_3)
else:
    print('La temperatura menor es:',tem_1)

promedio = (tem_1 + tem_2 + tem_3) // (3)
print('Promedio de temperatura:',promedio)