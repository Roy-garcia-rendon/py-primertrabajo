n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
mul = n1 * n2
res = n1 % n2
div = n1 / n2
po = suma ** 2

mensaje = f"""PARA LOS NUMEROS {n1} y {n2},
La suma es: {suma},
La resta es: {resta},
La multiplicación es: {mul},
El residuo es: {res},
La división es: {div},
La potencia al cuadrado es: {po}."""

print(mensaje)
