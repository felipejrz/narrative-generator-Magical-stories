from planes import *
from bitacora import *

class Goal:
    def __init__(self, goal_name, character_name, preconditions, plan):
        self.goal_name = goal_name
        self.character_name = character_name
        self.preconditions = preconditions
        self.plan = plan

    def ejecutar_plan(self, character, name_plan):
        registrar_mensaje("Verifica las precondiciones de la metas")
        if self.verificar_precondiciones(character):
            #Nos regresa el diccionario exaco del plan
            diccionario_plan = diccionarioMetas[name_plan]
            registrar_mensaje("Se obtiene el diccionario espesifico del la meta")
            #Obtenemos la funcion del diccionario
            plan_Encontrado = diccionario_plan["plan"]
            registrar_mensaje("Se ejecuta el plan de la meta")
            #Ejecutamos el plan
            plan_Encontrado(character)
        else:
            registrar_mensaje("No se cumplieron las precondiciones de la meta", nivel=logging.ERROR)

    
    def verificar_precondiciones(self, character):
        bandera = False
        if not self.preconditions:
            registrar_mensaje("No hay precondiciones que cumplir")
            return True  # Si no hay precondiciones, No hay preconduciones por cumplir por lo tanto se accede el plan

        # Recorre las precondiciones
        registrar_mensaje("Recorre la lista de precondiciones de la meta")
        for funcion in self.preconditions:
            new_location = funcion(character)
            registrar_mensaje("Verifica si la localización del personaje y la localización de la precondición son iguales")
            # Verifica si la localización del personaje y la localización de la precondición son iguales
            if character.get_location() == new_location:
                registrar_mensaje("Se cumplió una precondición de la meta")
                bandera = True
        return bandera
