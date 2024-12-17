from registro_financiero import GestorFinanciero

def menu():
    """Interfaz de usuario en la terminal."""
    gestor = GestorFinanciero()
    gestor.cargar_datos()
    while True:
        print("\n--- Menú de Seguimiento de Gastos ---")
        print("1. Agregar Ingreso")
        print("2. Agregar Gasto")
        print("3. Listar transacciones")
        print("4. Mostrar balance")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            try:
                monto = float(input("Monto del ingreso: "))
                fecha = input("Fecha (YYYY-MM-DD): ")
                descripcion = input("Descripción: ")
                gestor.agregar_transaccion(monto, fecha, descripcion, "ingreso")
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "2":
            try:
                monto = float(input("Monto del gasto: "))
                fecha = input("Fecha (YYYY-MM-DD): ")
                descripcion = input("Descripción: ")
                gestor.agregar_transaccion(monto, fecha, descripcion, "gasto")
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "3":
            gestor.listar_transacciones()
        elif opcion == "4":
            gestor.calcular_balance()
        elif opcion == "5":
            print("Guardando datos y saliendo del programa...")
            gestor.guardar_datos()
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar la aplicación
if __name__ == "__main__":
    menu()