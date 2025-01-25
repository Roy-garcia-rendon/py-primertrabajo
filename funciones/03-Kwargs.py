def get_product(**datos):  # **kwargs argument
    print(datos["id"], datos["name"])


get_product(id="23",
            name="samsung",
            precio="$1000")
