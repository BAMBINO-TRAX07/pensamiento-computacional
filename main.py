Aldy Abiimael Ramos Mota 1589025
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Control:
    def __init__(self, dias, azucar, sal, presion_sistolica):
        self.dias = dias
        self.azucar = azucar
        self.sal = sal
        self.presion_sistolica = presion_sistolica
        self.presion_diastolica = [75, 78, 72, 79, 95]  

    def evaluar_dia(self, dia, azucar, sal, sistolica, diastolica):
        print(f"\n--- {dia} ---")
        alerta = False

        if 70 <= azucar <= 140:
            print(f"Nivel de azúcar: {azucar} mg/dL (Normal)")
        else:
            print(f"Nivel de azúcar: {azucar} mg/dL (¡Fuera de rango!)")
            alerta = True

        if sal <= 2300:
            print(f"Consumo de sal: {sal} mg (Normal)")
        else:
            print(f"Consumo de sal: {sal} mg (¡Excesivo!)")
            alerta = True

        print(f"Presión arterial: {sistolica}/{diastolica} mmHg")
        if sistolica < 120 and diastolica < 80:
            print("Presión arterial: Normal")
        elif 120 <= sistolica <= 129 and diastolica < 80:
            print("Presión arterial: Elevada")
        elif 130 <= sistolica <= 139 or 80 <= diastolica <= 89:
            print("Presión arterial: Hipertensión Etapa 1")
            alerta = True
        elif sistolica >= 140 or diastolica >= 90:
            print("Presión arterial: Hipertensión Etapa 2")
            alerta = True

        if alerta:
            print("¡Alerta! Se recomienda atención médica.")
        else:
            print("Todo en orden.")

    def evaluar_semana(self):
        suma_azucar = sum(self.azucar)
        suma_sal = sum(self.sal)
        suma_presion_s = sum(self.presion_sistolica)
        suma_presion_d = sum(self.presion_diastolica)

        for i in range(len(self.dias)):
            self.evaluar_dia(
                self.dias[i],
                self.azucar[i],
                self.sal[i],
                self.presion_sistolica[i],
                self.presion_diastolica[i]
            )

        print("\n--- Promedios Semanales ---")
        print(f"Promedio azúcar: {suma_azucar / len(self.azucar):.2f} mg/dL")
        print(f"Promedio sal: {suma_sal / len(self.sal):.2f} mg")
        print(f"Promedio presión sistólica: {suma_presion_s / len(self.presion_sistolica):.2f} mmHg")
        print(f"Promedio presión diastólica: {suma_presion_d / len(self.presion_diastolica):.2f} mmHg")

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
niveles_azucar = [130, 160, 95, 175, 160]
niveles_sal = [2000, 2400, 1800, 2400, 2700]
presion_sistolica = [115, 130, 110, 125, 175]

paciente = Persona("Juan Pérez")
control = Control(dias, niveles_azucar, niveles_sal, presion_sistolica)
print(f"Evaluación semanal de salud para {paciente.nombre}")
control.evaluar_semana()
