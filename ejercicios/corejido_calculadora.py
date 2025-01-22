print("bienvenidos a la calculadora")
print("ingrese 'salir' para terminar")
print("Las operaciones que se pueden realisar son, suma, resta, multiy div")

resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese el primer numero:")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("ingrese la operacion que desea realizar:")
    if op.lower() == "salir":
        break
    n2 = input("ingrese el siguiente numero:")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("operacion no valida")
        break
    print("el resultado es:", {resultado})
