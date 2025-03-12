print("ejercicio 1")
print("Aldy Abimael Ramos Mota 1589025")
def calcular_costo(consumo, habitantes):
    if consumo < 15:
        tarifa = 5
    elif 15 <= consumo <= 30:
        if habitantes > 3:
            tarifa = 4
        elif habitantes == 3:
            tarifa = 4.5
        else:
            tarifa = 5
    else:  # consumo > 30
        if habitantes > 5:
            tarifa = 3.5
        elif habitantes % 2 == 0:  # número de habitantes par
            tarifa = 4
        else:
            tarifa = 4.2

    costo_total = consumo * tarifa
    return costo_total

# Ejemplo de uso
consumo = float(input("Ingrese el consumo de agua en m³: "))
habitantes = int(input("Ingrese el número de habitantes: "))

costo = calcular_costo(consumo, habitantes)
print(f"El costo del consumo de agua es: Q{costo:.2f}")

print("ejercicio 2")
year= float(input("ingrese el year del vehiculo"))
numero= int(input("ingrese el ultimo digito de la placa de su vehiculo"))

if numero % 2 ==0:
    print("No circula los lunes")
elif numero != 0 :
    print("No circula los viernes")
if year % 2 == 0:
    print("Puede circular los sabados solo hasta medio dia")
if year <=1976:
    print("ADVERTENCIA: Mantenimiento obligatorio ")
