print("ejercicio 1")
print("Aldy Abimael Ramos Mota 158902520")
def llenar_multiplicadores(tamaño, base):
    arreglo = []
    for i in range(1, tamaño + 1):
        arreglo.append(base * i)
    return arreglo
tamaño = int(input("Ingresa el tamaño del arreglo: "))
base = int(input("Ingresa el número base para generar los múltiplos: "))
arreglo = llenar_multiplicadores(tamaño, base)
print(f"El arreglo con los primeros {tamaño} múltiplos de {base} es: {arreglo}")

print("ejercicio 2")
tamaño = int(input("Ingrese el número de personas: "))
nombres = []
longitudes = []
for i in range(tamaño):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    nombres.append(nombre)
    longitudes.append(len(nombre))
print("\nNombres almacenados:")
print(nombres)
print("\nLongitudes de los nombres:")
print(longitudes)

print("esenario 1")
def registrar_respuestas(n):
    respuestas = []
    for i in range(n):
        respuesta = int(input(f"Ingrese la evaluación para el cliente {i+1} (1 a 5): "))
        while respuesta < 1 or respuesta > 5:
            print("Respuesta no válida. Ingrese un valor entre 1 y 5.")
            respuesta = int(input(f"Ingrese la evaluación para el cliente {i+1} (1 a 5): "))
        respuestas.append(respuesta)
    
    return respuestas

def analizar_respuestas(respuestas):
    conteo_respuestas = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for respuesta in respuestas:
        conteo_respuestas[respuesta] += 1
    promedio = sum(respuestas) / len(respuestas)
    max_frecuencia = max(conteo_respuestas.values())
    respuesta_frecuente = [k for k, v in conteo_respuestas.items() if v == max_frecuencia][0]
    clientes_menor_promedio = [respuesta for respuesta in respuestas if respuesta < promedio]
    porcentaje_menor_promedio = (len(clientes_menor_promedio) / len(respuestas)) * 100
    print("\nRespuestas")
    for i in range(1, 6):
        print(f"{i}: {conteo_respuestas[i]}")
    print(f"\nb) Respuesta más frecuente: {respuesta_frecuente}")
    print(f"c) Promedio: {promedio:.2f}")
    print(f"Porcentaje menor al promedio: {porcentaje_menor_promedio:.2f}%")
n = int(input("Ingrese el número de clientes: "))
respuestas = registrar_respuestas(n)
analizar_respuestas(respuestas)