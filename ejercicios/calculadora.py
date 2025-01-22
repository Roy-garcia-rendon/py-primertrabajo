print("bienvenidos a la calculadora")
print("ingrese 'salir' para terminar")
print("Las operaciones que se pueden realisar son, suma, resta, multiy div")

n1 = int(input("ingrese el primer numero:"))
ope = input("ingrese la operacion que desea realizar:")
n2 = int(input("ingrese el segundo numero:"))

if n1 == input(""):
    print("ingrese un numero")

else:
    if ope == "suma":
        resaltado = n1 + n2
        print("el resultado es:", resaltado)
    elif ope == "resta":
        resaltado = n1 - n2
        print("el resultado es:", resaltado)
    elif ope == "multi":
        resaltado = n1 * n2
        print("el resultado es:", resaltado)
    elif ope == "div":
        resaltado = n1 / n2
        print("el resultado es:", resaltado)

while True:
    ope = input("ingrese la operacion que desea realizar:")
    n2 = int(input("ingrese el segundo numero:"))
    if ope == "suma":
        resaltado = resaltado + n2
        print("el resultado es:", resaltado)
    elif ope == "resta":
        resaltado = resaltado - n2
        print("el resultado es:", resaltado)
    elif ope == "multi":
        resaltado = resaltado * n2
        print("el resultado es:", resaltado)
    elif ope == "div":
        resaltado = resaltado / n2
        print("el resultado es:", resaltado)

    comando = input("")
    print(comando)
    if comando.lower() == "salir":
        break
