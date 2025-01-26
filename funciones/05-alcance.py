saludo = "hola global"


def saludar():
    global saludo
    saludo = "hola mundo"


def saludarpero():
    global saludo
    saludo = "hola nacos"
    print(saludo)


print(saludo)
saludar()
print(saludo)
saludarpero()
