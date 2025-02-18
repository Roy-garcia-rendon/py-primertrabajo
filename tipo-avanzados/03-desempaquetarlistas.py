numeros = [1, 2, 3]


# feo
# primero = numeros[0]
# primero = numeros[1]
# primero = numeros[2]

primero, segundo, tercero = numeros
primero, *otros = numeros

print(*numeros)
print(primero, segundo, otros)
print(primero, segundo, tercero)
