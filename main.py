import sqlite3
conexion = sqlite3.connect("datos.db")
cursor = conexion.cursor()

def crearTarea():
  # Pedir número de la tarea
  print("Ingresa un numero de lista para tu tarea: ")
  numeroIngresado = int(input())

  # Pedir hora en que realizara la tarea
  print("A que hora realizarás la tarea: ")
  horarioIngresado = input()

  # Pedir la tarea a realizar
  print("¿Cuál es la tarea que realizaras?: ")
  tareaIngresada = input()

  # Creo una tupla y le asigno los elementos recibidos desde el usuario
  detallesTarea = (numeroIngresado, horarioIngresado, tareaIngresada)

  # Agregar tupla a la lista
  listaTareas = [detallesTarea] 

  # insertando filas
  cursor.executemany("INSERT INTO tareas VALUES (?,?,?)", listaTareas)

  # consultando datos
  cursor.execute("Select * FROM tareas")
  tareas = cursor.fetchall()

  for tarea in tareas:
    print(tarea)

  # Actualizo base y cierro conexión
  conexion.commit()
  conexion.close()

def modificarTarea():
  # Pedir indice de tarea que quiere modificar
  print("Ingresa el número de la tarea que quieres modificar:")
  idTarea = input()

  # Pedir elemento que quiere modificar
  print("Qué quieres modificar: hora/tarea")
  elementoModificar = input()

  # Pedir modificación
  print("Agrega el cambio que quieres hacer: ")
  valorModificado = input()

  cursor.execute("UPDATE tareas SET " + elementoModificar + " = " + valorModificado + " where id = "+ idTarea)

  # se actualiza la base y se cierra la conexión
  conexion.commit()
  conexion.close()

def eliminarTarea():
  print("Ingresa el número de la tarea que quieres eliminar:")
  idTareaEliminar = input()

  cursor.execute("DELETE FROM tareas WHERE id =" + idTareaEliminar)
  conexion.commit()
  conexion.close()

def verTareas():
  cursor.execute("Select * FROM tareas")
  tareas = cursor.fetchall()

  for tarea in tareas:
    print(tarea)

# Preguntar que quiere hacer el usuario
print("Que quieres hacer: agregar/modificar/eliminar/ver")
accion = input()

if(accion == "agregar"):
  crearTarea()
elif(accion == "modificar"):
  modificarTarea()
elif(accion == "eliminar"): 
  eliminarTarea()
elif(accion == "ver"):
  verTareas()  
