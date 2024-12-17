import pickle
from typing import List
from transaccion import Transaccion

class GestorFinanciero:
    def __init__(self):
        """Clase que gestiona las transacciones financieras."""
        self.transacciones: List[Transaccion] = []
        self.archivo_datos = "datos_financieros.pkl"
    
    def agregar_transaccion(self, monto: float, fecha: str, descripcion: str, tipo: str):
        """Agrega una transacción a la lista."""
        transaccion = Transaccion(monto, fecha, descripcion, tipo)
        self.transacciones.append(transaccion)
        print(f"Transacción de {tipo} agregada con éxito.")

    def listar_transacciones(self):
        """Lista todas las transacciones ordenadas por fecha."""
        if not self.transacciones:
            print("No hay transacciones registradas.")
            return
        print("\n--- Transacciones ---")
        for trans in sorted(self.transacciones, key=lambda x: x.fecha):
            print(trans)
    
    def calcular_balance(self):
        """Calcula el balance financiero actual."""
        ingresos = sum(t.monto for t in self.transacciones if t.tipo == "ingreso")
        gastos = sum(t.monto for t in self.transacciones if t.tipo == "gasto")
        capacidad_ahorro = ingresos - gastos
        print(f"\n--- Balance ---")
        print(f"Total Ingresos:    {ingresos:.2f}")
        print(f"Total Gastos:      {gastos:.2f}")
        print(f"Capacidad Ahorro:  {capacidad_ahorro:.2f}")

    def guardar_datos(self):
        """Guarda las transacciones en un archivo."""
        with open(self.archivo_datos, "wb") as archivo:
            pickle.dump(self.transacciones, archivo)
        print("Datos guardados correctamente.")

    def cargar_datos(self):
        """Carga las transacciones desde un archivo."""
        try:
            with open(self.archivo_datos, "rb") as archivo:
                self.transacciones = pickle.load(archivo)
            print("Datos cargados correctamente.")
        except FileNotFoundError:
            print("No se encontraron datos previos. Iniciando con datos vacíos.")