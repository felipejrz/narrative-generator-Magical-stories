import logging, os
from character_structure import Character
from goals_structure import Goal
from introduccion import *
from bitacora import *
from templates import *
from planes import *
from cuento import *

def main():
    # Configurar la bitácora
    configurar_bitacora()
    registrar_mensaje("Se Inicio el programa")

    # Crear una instancia de la interfaz y ejecutarla
    personaje = Character()
    #Registro Bitacora
    registrar_mensaje('Se creo el objeto Personaje:', nivel=logging.DEBUG)
    registrar_objeto(personaje, nivel=logging.DEBUG)

    #Intancia los valores principales del personaje
    personaje.set_name(seleccionName())
    personaje.set_location(seleccionLocation())

    registrar_mensaje("Verifica si la meta existe en diccionario de metas")
    meta = "Aprender magia en la Escuela de Magia Kukulkan para proteger su tierra de una amenaza oscura"
    #Verificamos el existe la meta
    if meta in diccionarioMetas:
        #Nos regresa el diccionario exacta de la meta
        diccionario_plan = diccionarioMetas[meta]
        #Se crea la meta
        registrar_mensaje("Meta encontrada se procede a realiza el Plan")
        goals = Goal(diccionario_plan["goal_name"], personaje.get_name(), diccionario_plan["preconditions"], meta)
        #Registro Bitacora
        registrar_mensaje('Se creo el objeto Meta:'+ meta, nivel=logging.DEBUG)
        registrar_objeto(goals, nivel=logging.DEBUG)
        #Se ejecuta el plan    
        goals.ejecutar_plan(personaje, meta)
    else:
        registrar_mensaje("No encontro la meta indicada:" + meta, nivel=logging.ERROR)

    arreglar_cuento()
    registrar_mensaje("Programa terminado")

if __name__ == "__main__":
    main()