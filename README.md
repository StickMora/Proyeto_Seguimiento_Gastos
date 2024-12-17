# Aplicación de Seguimiento de Gastos

Esta es una aplicación de terminal para el seguimiento de gastos personales. Permite a los usuarios registrar ingresos y gastos, listar transacciones ordenadas por fecha y generar un balance financiero.

## Características

- **Registrar Ingresos**: Agrega transacciones de tipo ingreso.
- **Registrar Gastos**: Agrega transacciones de tipo gasto.
- **Listar Transacciones**: Muestra las transacciones ordenadas por fecha.
- **Generar Balance**:
  - Total de ingresos.
  - Total de gastos.
  - Capacidad de ahorro (ingresos - gastos).
- **Persistencia de Datos**:
  - Las transacciones se guardan automáticamente en el archivo `datos_financieros.pkl` al salir del programa.
  - Los datos se cargan automáticamente al iniciar el programa.

---

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/StickMora/Proyeto_Seguimiento_Gastos.git

2. Cambia al directorio del proyecto:
   ```bash
   cd Proyeto_Seguimiento_Gastos

## Ejecución
Ejecuta el archivo principal `main.py` desde la terminal:

## Uso
Al ejecutar la aplicación, se te mostrará un menú con las siguientes opciones:
  1. Agregar Ingreso
  2. Agregar Gasto
  3. Listar Transacciones
  4. Mostrar Balance
  5. Salir

## 1. Agregar Ingreso
Ingresa el monto, la fecha (en formato YYYY-MM-DD) y una descripción.
Ejemplo:
  - Monto: 1000
  - Fecha (YYYY-MM-DD): 2024-12-17
  - Descripción: Sueldo

## 2. Agregar Gasto
Ingresa el monto, la fecha (en formato YYYY-MM-DD) y una descripción.
Ejemplo:
  - Monto: 200
  - Fecha (YYYY-MM-DD): 2024-12-17
  - Descripción: Supermercado

## 3. Listar Transacciones
Muestra una lista ordenada de todas las transacciones registradas.

## 4. Mostrar Balance
Muestra el balance financiero actual:
- Total de ingresos.
- Total de gastos.
- Capacidad de ahorro (ingresos - gastos).
  
Ejemplo:
  - Total Ingresos: 3000
  - Total Gastos: 1500
  - Capacidad de Ahorro: 1500

## 5. Salir
Guarda automáticamente los datos en el archivo datos_financieros.pkl y cierra la aplicación.


