print("escriba una palabra para saber si es palindromo")


def palindromo(texto):

    while True:
        texto = texto.replace(" ", "").lower()

        if texto == texto[::-1]:
            return (f"{texto}, es palindromo")

        if texto != texto[::-1]:
            return (f"{texto}, no es palindromo")

        if texto.lower() == "salir":
            break


print(palindromo(input("escriba una palabra: ")))
