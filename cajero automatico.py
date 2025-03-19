def cajero_automatico():
    saldo = 3000  # Saldo inicial
    intentos = 0  # Contador de intentos para verificar si el usuario supera los 3 intentos

    while True:
        # Mostrar saldo disponible
        print(f"Saldo disponible: Q{saldo}")
        
        # Solicitar al usuario el monto que desea retirar
        retiro = float(input("Ingrese el monto a retirar (0 para salir): "))
        
        if retiro == 0:
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break
        
        if retiro > saldo:
            intentos += 1
            print(f"No tiene suficiente saldo para retirar Q{retiro}. Intento {intentos} de 3.")
            
            if intentos >= 3:
                print("Ha intentado retirar más de tres veces una cantidad superior al saldo disponible. El programa terminará.")
                break
        
        elif retiro == saldo:
            print(f"Has retirado todo tu saldo: Q{retiro}. ¡Gracias por usar el cajero!")
            break
        
        elif retiro < saldo:
            saldo -= retiro
            print(f"Has retirado Q{retiro}. Saldo restante: Q{saldo}")

if __name__ == "__main__":
    cajero_automatico()