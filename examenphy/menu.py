from fuciones import sueldo_aleatorio,clasificacion_sueldo,estadisticas,guardar,reporte_sueldo

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

while True:
  print("\nMenu:")
  print("1) Asignar sueldo aleatorio")
  print("2) Clasificar sueldo")
  print("3) Ver estadisticas")
  print("4) Reporte de sueldo")
  print("5) Salir del programa")
  opcion = input("Seleccione una opción: ")

  if opcion == '1':

    sueldo_aleatorio(trabajadores)
  elif opcion == '2':
    clasificacion_sueldo(trabajadores)
  elif opcion == '3':
    estadisticas(trabajadores)
  elif opcion == '4': 
    reporte_sueldo(trabajadores)
  elif opcion == '5':
    guardar()
    break

  else:

    print("Opción no válida. Por favor, seleccione una opción del menú.")