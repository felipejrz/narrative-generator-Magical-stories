from post_condition import *
from precondition import *
from bitacora import *
from actions import *
from templates import *
from cuento import *

class Story_Actions:
    def __init__(self, name_action, name_charater, precondition, post_conditions, template):
        self.name_action = name_action
        self.name_charater = name_charater
        self.precondition = precondition
        self.post_conditiosn = post_conditions
        self.template = template
    
    def ejecutar(self, character, valor_aCambiar, numPostCondition):
        registrar_mensaje("Se comenzo a ejecutar la accion")
        self.verificar_precondiciones(character, valor_aCambiar, numPostCondition)#Esta misma realiza las post condiciones
    
    def verificar_precondiciones(self, character, valor_Actual, numPostCondition):
        if not self.precondition:
            registrar_mensaje("No hay precondiciones que cumplir")
            # Si no hay precondiciones, No hay preconduciones por cumplir por lo tanto se acepta la accion
            self.aplicar_postcondiciones(character, numPostCondition)
        else:
            registrar_mensaje("Verifica las precondiciones de la accion")
        for verificacionValor in self.precondition:
            verificacion_Valor = verificacionValor(character)
            if valor_Actual == verificacion_Valor:
                registrar_mensaje("Se lograron las precondiciones de la Accion")
                self.aplicar_postcondiciones(character, numPostCondition)
                break
    
    def aplicar_postcondiciones(self, character, valor_PostCondicion):
        registrar_mensaje("Se aplican las Pos condiciones de la accion")
        for valoresFuturos in self.post_conditiosn:
            valores_Futuros = valoresFuturos()
            if valor_PostCondicion == 0:
                registrar_mensaje("El template utilizado es: " + diccionarioTemplates[self.template](character.get_name(), character.get_location(), valores_Futuros))
                escribir_cuento(diccionarioTemplates[self.template](character.get_name(), character.get_location(), valores_Futuros))
                character.set_location(valores_Futuros)
            elif valor_PostCondicion == 1:
                registrar_mensaje("El template utilizado es: " + diccionarioTemplates[self.template](character.get_name()))
                escribir_cuento(diccionarioTemplates[self.template](character.get_name()))
                character.set_nvlMagic(valores_Futuros)
            elif valor_PostCondicion == 2:
                registrar_mensaje("El template utilizado es: " + diccionarioTemplates[self.template](character.get_name(), valores_Futuros))
                escribir_cuento(diccionarioTemplates[self.template](character.get_name(), valores_Futuros))
                character.set_typeMagic(valores_Futuros)
            elif valor_PostCondicion == 3:
                character.set_arma(valores_Futuros)
            elif valor_PostCondicion == 4:
                registrar_mensaje("El template utilizado es: " + diccionarioTemplates[self.template](character, valores_Futuros))
                escribir_cuento(diccionarioTemplates[self.template](character, valores_Futuros))
                character.set_amigos(valores_Futuros)
            elif valor_PostCondicion == 5:
                registrar_mensaje("El template utilizado es: " + diccionarioTemplates[self.template](character.get_name()))
                escribir_cuento(diccionarioTemplates[self.template](character.get_name()))
                character.set_valentia(valores_Futuros)
            elif valor_PostCondicion == 6:
                registrar_mensaje("El template utilizado es: " + diccionarioTemplates[self.template](character))
                escribir_cuento(diccionarioTemplates[self.template](character))
                character.set_informacion(valores_Futuros)
            elif valor_PostCondicion == 7:
                registrar_mensaje("El template utilizado es: " + diccionarioTemplates[self.template](character.get_name()))
                escribir_cuento(diccionarioTemplates[self.template](character.get_name()))
                character.set_reconocimiento(valores_Futuros)
            elif valor_PostCondicion == 8:
                registrar_mensaje("El template utilizado es: " + diccionarioTemplates[self.template](character))
                escribir_cuento(diccionarioTemplates[self.template](character))
                character.set_amenaza(valores_Futuros)   
            elif valor_PostCondicion == 9:
                registrar_mensaje("El template utilizado es: " + diccionarioTemplates[self.template](character.get_name()))
                escribir_cuento(diccionarioTemplates[self.template](character.get_name()))
                character.set_tierrasNatales(valores_Futuros)
