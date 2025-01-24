def hola(nombre, apellido="feliz"):  # parametros #PARAMETROS OPCIONALES
    print("Hola mundo")
    print(f"Bienvenido {nombre}, {apellido}")


hola("Roy", "Garcia")  # argumentos
hola("Luis")


hola(apellido="GArcia", nombre="rodri")  # argumentos nombrados
