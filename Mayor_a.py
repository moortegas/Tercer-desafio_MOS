import sys

# Dicionario ventas Key Mes y value es monto vendido


ventas = {
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,
}
# print(ventas)

filtrado = {}

for k, v in ventas.items():
    if v>40000:
        filtrado[k] = v

# print(filtrado)
print("Los meses con ventas superiore a 40000 son los siguientes:", (filtrado))



