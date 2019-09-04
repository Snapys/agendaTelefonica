# Agregar Contacto
# Remover Contactos
# Actualizar un Contacto
# Ver un Contacto
# Ver todos nuestros Contactos

agenda_telefonica = dict()

def imprimir_operacion(nombre_operacion):
  print("\n----- Agenda Telefonica -----\n")
  print(nombre_operacion)
  print("\n-----------------------------\n")


def agregar_contacto():
  nombre = input("\nNombre del nuevo Contacto: ")
  numero = input("Numero del Contacto: ")
  agenda_telefonica[nombre] = numero
  print("\n" + nombre + " fue agregado exitosamente a nuestra agenda\n")


def remover_contacto():
  nombre = input("\nNombre del Contacto que desea borrar: ")

  try:
    del agenda_telefonica[nombre]
  except KeyError:
    print("\n" + nombre + " no existe en la agenda Telefonica\n")
  else:
    imprimir_operacion(nombre + " fue borrado exitosamente")


def actualizar_contacto():
  nombre = input("\nNombre del contacto que deseas actulizar: ")
  numero = input("Nuevo numero de este contacto: ")
  print("\n" + nombre + " " + "fue actualizado exitosamente")
  print("\n-----------------------------\n")
  agenda_telefonica[nombre] = numero


def ver_contacto():
  nombre = input("\nNombre del Contacto que desea ver: ")
  
  nombre_operacion = None
  try:
    # nombre_operacion = nombre + " - " + agenda_telefonica[nombre]
    nombre_operacion = "{} - {}".format(nombre,agenda_telefonica[nombre])
  except KeyError:
    nombre_operacion = "El contacto " + nombre + " no existente en la Agenda Telefonica"
  imprimir_operacion(nombre_operacion)


def ver_todos():
  nombre_operacion = None
  if len(agenda_telefonica) == 0:
   nombre_operacion = "No tienen ningun contacto agendado en tu Agenda Telefonica"
  else:
    for contacto in agenda_telefonica:
      pure_contacto = "{} - {}".format(contacto,agenda_telefonica[contacto])
      if nombre_operacion == None:
        nombre_operacion = pure_contacto
      else:
        nombre_operacion += "\n" + pure_contacto
      # print(contacto +  " - " + agenda_telefonica[contacto])
  imprimir_operacion(nombre_operacion)


def iniciar_agenda():
  print("\nBienvenido a la Agenda Telefonica de Federico\n")

  while True:
    print("1 - Agregar Contacto \n2 - Remover Contacto \n3 - Actualizar Contacto \n4 - Ver un contacto \n5 - Ver todos los contactos \n6 - Salir\n")

    try:
      operacion = int(input(": "))
    except ValueError:
      print("\nPorfavor selecciona una opcion valida del 1 al 6\n")
    else:
      if operacion == 1:
        agregar_contacto()
      elif operacion == 2:
        remover_contacto()
      elif operacion == 3:
        actualizar_contacto()
      elif operacion == 4:
        ver_contacto()
      elif operacion == 5:
        ver_todos()
      elif operacion == 6:
        break
      else:
        print("\nOperacion desconocida\n")


def cerrar_agenda():
  print("\nGracias por usar nuestra agenda Telefonica\n")


iniciar_agenda()
cerrar_agenda()
