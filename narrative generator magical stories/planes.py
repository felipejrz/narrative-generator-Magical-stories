import random
from character_structure import *
from actions import *
from bitacora import *

def Plan1(character):
    #print("Se ejecuto Plan1")
    realizar_Action(character, character.get_amenaza(), "Inicio de la Amenaza", 8)
    realizar_Action(character, character.get_tierrasNatales(), "Peligro en las Tierras Natales", 9)
    realizar_Action(character, character.get_location(), "Caminar a la Puerta Principal", 0)
    return character.get_location()

def Plan2(character):
    #print("Se ejecuto Plan2")
    while(character.get_tierrasNatales() != "A Salvo"):
        if(character.get_nvlMagic()==None):
            #print("Se ejecuto Plan3")
            Plan3(character)
        elif(character.get_nvlMagic()== "Basico" and character.get_typeMagic() == None):
            #print("Se ejecuto Plan4")
            Plan4(character)
        elif(character.get_amigos() == None):
            #print("Se ejecuto Plan5")
            Plan5(character)
        elif(character.get_amigos() != None and character.get_informacion() == None):
            #print("Se ejecuto Plan6")
            Plan6(character)
        elif(character.get_informacion() == "Basicas" and character.get_valentia() == False and character.get_nvlMagic()== "Intermedia"):
            #print("Se ejecuto Plan7")
            Plan7(character)
        elif(character.get_nvlMagic() == "Avanzada" and character.get_informacion() == "Avanzada" and character.get_amenaza() != False):
            #print("Se ejecuto Plan8")
            Plan8(character)
        elif(character.get_nvlMagic()== "Avanzada" and character.get_amenaza() == False):
            #print("Se ejecuto Plan9")
            Plan9(character)
    return character.get_location()

def Plan3(character):
    realizar_Action(character, character.get_location(), "Caminar a los Pasillos", 0)
    realizar_Action(character, character.get_location(), "Caminar al Salon de Clases", 0)
    realizar_Action(character, character.get_nvlMagic(), "Aprender Magia", 1)
    return character.get_location()

def Plan4(character):
    realizar_Action(character, character.get_location(), "Caminar a los Pasillos", 0)
    realizar_Action(character, character.get_location(), "Caminar a la Mazmorra", 0)
    realizar_Action(character, character.get_typeMagic(), "Aprender Tipo de Magia", 2)
    realizar_Action(character, character.get_nvlMagic(), "Desafio Magico", 1)
    return character.get_location()

def Plan5(character):
    realizar_Action(character, character.get_location(), "Caminar a los Pasillos", 0)
    opcion = random.randint(0, 1)
    if opcion == 0:
        realizar_Action(character, character.get_location(), "Caminar al Dormitorio", 0)
    elif opcion == 1:
        realizar_Action(character, character.get_location(), "Caminar al Comedor", 0)
    realizar_Action(character, character.get_amigos(), "Interactuar con Alumnos", 4)
    return character.get_location()

def Plan6(character):
    realizar_Action(character, character.get_location(), "Caminar a los Pasillos", 0)
    realizar_Action(character, character.get_location(), "Caminar a la Biblioteca", 0)
    realizar_Action(character, character.get_informacion(), "Busqueda de Codices", 6)
    return character.get_location()

def Plan7(character):
    realizar_Action(character, character.get_location(), "Caminar a los Pasillos", 0)
    realizar_Action(character, character.get_location(), "Caminar a la Puerta Principal", 0)
    realizar_Action(character, character.get_location(), "Caminar al Bosque Encantado", 0)
    realizar_Action(character, character.get_location(), "Caminar al Templo de Quetzalcoatl", 0)
    realizar_Action(character, character.get_valentia(), "Hablar con Quetzalcóatl", 5)
    realizar_Action(character, character.get_location(), "Caminar al Bosque Encantado", 0)
    realizar_Action(character, character.get_nvlMagic(), "Aprendisaje Avanzado", 1)
    realizar_Action(character, character.get_informacion(), "Artefacto Encontrado", 6)
    return character.get_location()

def Plan8(character):
    realizar_Action(character, character.get_location(), "Caminar al Abismo de Tlaloc", 0)
    realizar_Action(character, character.get_amenaza(), "Batalla Final", 8)
    return character.get_location()

def Plan9(character):
    realizar_Action(character, character.get_tierrasNatales(), "Tierras Natales a Salvo", 9)
    realizar_Action(character, character.get_reconocimiento(), "Reconocimiento Mundial", 7)
    return character.get_location()

dicMeta1 = {
    "goal_name": "Inicio Aventura",
    "preconditions": [],
    "plan": Plan1,
}

dicMeta2 = {
    "goal_name": "Aprender magia en la Escuela de Magia Kukulkan para proteger su tierra de una amenaza oscura",
    "preconditions": [Plan1],
    "plan": Plan2,
}

dicMeta3 = {
    "goal_name": "Aprendizaje Inicial",
    "preconditions": [],
    "plan": Plan3,
}

dicMeta4 = {
    "goal_name": "Desafíos Magicos Escolares",
    "preconditions": [],
    "plan": Plan4,
}

dicMeta5 = {
    "goal_name": "Búsqueda de Aliados",
    "preconditions": [],
    "plan": Plan5,
}

dicMeta6 = {
    "goal_name": "Investigación de pistas",
    "preconditions": [],
    "plan": Plan6,
}

dicMeta7 = {
    "goal_name": "Búsqueda de Aliados",
    "preconditions": [],
    "plan": Plan7,
}

dicMeta8 = {
    "goal_name": "Confrontación Final",
    "preconditions": [],
    "plan": Plan8,
}

dicMeta9 = {
    "goal_name": "Final de la aventura",
    "preconditions": [],
    "plan": Plan9,
}

diccionarioMetas = {
    "Inicio Aventura": dicMeta1,
    "Aprender magia en la Escuela de Magia Kukulkan para proteger su tierra de una amenaza oscura": dicMeta2,
    "Aprendizaje Inicial": dicMeta3,
    "Desafíos Magicos Escolares":  dicMeta4,
    "Búsqueda de Aliados": dicMeta5,
    "Investigación de pistas": dicMeta6,
    "Búsqueda de Aliados": dicMeta7,
    "Confrontación Final": dicMeta8,
    "Final de la aventura": dicMeta9,
}