import sys
from string import ascii_lowercase
# from getpass import getpass

password = "gato"
contador = 0

print("Ingrese su clave: ", password)

for letra in password:
    for elemento in ascii_lowercase:
        contador = contador+1
        if letra == elemento:

            break
print("El contador de su clave es :", (contador))

# password = getpass("Ingrese su clave: ")


# print(ascii_lowercase)
# for letra in ascii_lowercase:
#     print(letra)
# for elemento in password:
#     print(elemento)

