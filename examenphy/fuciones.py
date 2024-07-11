import csv
import random


def sueldo_aleatorio(trabajadores):
  sueldo = round(random.uniform(300000, 2500000))
  trabajadores.append(sueldo)
  print(f"trabajador {trabajadores} agregado con sueldo {sueldo}.")

def clasificacion_sueldo(trabajadores):
  if sueldo_aleatorio < 800000:
    print("nombre empleado          sueldo")
    print(f"trabajador {trabajadores}  {trabajadores.sueldo}.")
  elif sueldo_aleatorio > 800000 and sueldo_aleatorio<2000000: 
    print("nombre empleado          sueldo")
    print(f"trabajador {trabajadores}  {trabajadores.sueldo}.") 
  else:
    print("nombre empleado          sueldo")
    print(f"trabajador {trabajadores}  {trabajadores.sueldo}.")
 
def estadisticas(trabajadores):
  if trabajadores:
    trabajadores.sueldo
    
  
  if trabajadores:
    promedio = sum(trabajadores['sueldo'] for trabajadores in trabajadores) / len(trabajadores)
    print(f"El promedio de los sueldo de los trabajadores es: {promedio}")

  else:
    print("No hay trabajadores aun para la estadistica")

def reporte_sueldo(trabajadores):
  if trabajadores:
    print

def guardar():
    print(" finalizando el programa")
    print(" desarrollado por Juan Pablo Gonzalez")
    print(" rut 17597383-4")

 


