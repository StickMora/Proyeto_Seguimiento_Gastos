from datetime import datetime


class Transaccion:
    def __init__(self, monto: float, fecha: str, descripcion: str, tipo: str):
        """
        Clase que representa una transacción financiera.
        
        Args:
            monto (float): Monto de la transacción.
            fecha (str): Fecha de la transacción en formato YYYY-MM-DD.
            descripcion (str): Descripción breve de la transacción.
            tipo (str): Tipo de la transacción ('ingreso' o 'gasto').
        """
        self.monto = monto
        self.fecha = datetime.strptime(fecha, "%Y-%m-%d")
        self.descripcion = descripcion
        self.tipo = tipo.lower()  # Normaliza el tipo a minúsculas
    
    def __repr__(self):
        tipo = "Ingreso" if self.tipo == "ingreso" else "Gasto"
        return f"{self.fecha.date()} | {tipo:8} | {self.monto:10.2f} | {self.descripcion}"