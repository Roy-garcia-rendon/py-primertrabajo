# and, or, not
gas = False
encendido = True
edad = 18
# if not gas and (encendido or edad > 17):
#     print("puedes avansar")
if not gas and encendido and edad > 17:
    print("puedes avansar")
else:
    print("no puedes avansar")
