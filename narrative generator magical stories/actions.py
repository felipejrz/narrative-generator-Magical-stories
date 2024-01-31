from story_actions_structure import Story_Actions
from post_condition import *
from precondition import *
from bitacora import *
from templates import *

amenazaDespierta = {
    "name_action": "Inicio de la Amenaza",
    "precondition": [],
    "post_conditions": [Post_SurgeAmenaza],
    "template": "template Inicio Amenaza"
}

tierrasNatalesDanger = {
    "name_action": "Peligro en las Tierras Natales",
    "precondition": [],
    "post_conditions": [Post_TierrasNatalesDanger],
    "template": "template Tierras Natales Danger"
}

walkSalonClases = {
    "name_action": "Caminar al Salon de Clases",
    "precondition": [Pre_Pasillo],
    "post_conditions": [Post_SalonClases],
    "template": "template Caminar"
}

walkDormitorio = {
    "name_action": "Caminar al Dormitorio",
    "precondition": [Pre_Pasillo],
    "post_conditions": [Post_Dormitorio],
    "template": "template Caminar"
}

walkMazmorra = {
    "name_action": "Caminar a la Mazmorra",
    "precondition": [Pre_Pasillo],
    "post_conditions": [Post_Mazmorra],
    "template": "template Caminar"
}

walkComedor = {
    "name_action": "Caminar al Comedor",
    "precondition": [Pre_Pasillo],
    "post_conditions": [Post_Comedor],
    "template": "template Caminar"
}

walkBiblioteca = {
    "name_action": "Caminar a la Biblioteca",
    "precondition": [Pre_Pasillo],
    "post_conditions": [Post_Biblioteca],
    "template": "template Caminar"
}

walkPuertaPrincipal = {
    "name_action": "Caminar a la Puerta Principal",
    "precondition": [Pre_Pasillo, Pre_Casa, Pre_BosqueEncantado],
    "post_conditions": [Post_PuertaPrincipal],
    "template": "template Caminar"
}

walkPasillo = {
    "name_action": "Caminar a los Pasillos",
    "precondition": [Pre_SalonClases, Pre_Dormitorio, Pre_Mazmorra, Pre_Comedor, Pre_Biblioteca, Pre_PuertaPrincipal],
    "post_conditions": [Post_Pasillo],
    "template": "template Caminar"
}

walkCasa = {
    "name_action": "Caminar a la Casa",
    "precondition": [Pre_PuertaPrincipal],
    "post_conditions": [Post_Casa],
    "template": "template Caminar"
}

walkBosqueEncantado= {
    "name_action": "Caminar al Bosque Encantado",
    "precondition": [Pre_PuertaPrincipal, Pre_AbismoTlaloc, Pre_TemploQuetzalcoatl],
    "post_conditions": [Post_BosqueEncanatado],
    "template": "template Caminar"
}

walkTemploQuetzalcoatl = {
    "name_action": "Caminar al Templo de Quetzalcoatl",
    "precondition": [Pre_BosqueEncantado],
    "post_conditions": [Post_TemploQuetzalcoatl],
    "template": "template Caminar"
}

walkAbismoTlaloc = {
    "name_action": "Caminar al Abismo de Tlaloc",
    "precondition": [Pre_BosqueEncantado],
    "post_conditions": [Post_AbismoTlaloc],
    "template": "template Caminar"
}

aprenderMagia = {
    "name_action": "Aprender Magia",
    "precondition": [],
    "post_conditions": [Post_MagiaBasica],
    "template": "template Magia Basica"
}

tipodeMagia = {
    "name_action": "Aprender Tipo de Magia",
    "precondition": [],
    "post_conditions": [Post_TipoMagia],
    "template": "template Tipo de Magia"
}

desafioMagico = {
    "name_action": "Desafio Magico",
    "precondition": [Pre_AprenderMagia],
    "post_conditions": [Post_MagiaIntermedia],
    "template": "template Desafio Magico"
}

interactuar = {
    "name_action": "Interactuar con Alumnos",
    "precondition": [],
    "post_conditions": [Post_Amigos],  
    "template": "template Interactuar"
}

busquedaCodices = {
    "name_action": "Busqueda de Codices",
    "precondition": [],
    "post_conditions": [Post_InformacionBasicas],
    "template": "template Codices"  
}

busquedaArtefacto = {
    "name_action": "Busqueda de Artefacto",
    "precondition": [Pre_BosqueEncantado],
    "post_conditions": [Post_InformacionAvanzadas],
    "template": "template Busqueda Artefacto"
}

hablarQuetzalcoatl = {
    "name_action": "Hablar con Quetzalcóatl",
    "precondition": [],
    "post_conditions": [Post_Valentia],
    "template": "template Hablar Quetzalcotal"
}

aprendisajeAvanzado = {
    "name_action": "Aprendisaje Avanzado",
    "precondition": [Pre_DesafioMagico],
    "post_conditions": [Post_MagiaAvanzada],
    "template": "template Magia Avanzada"
}

artefactoEncontrado = {
    "name_action": "Artefacto Encontrado",
    "precondition": [Pre_BusquedaCodices],
    "post_conditions": [Post_InformacionAvanzadas],
    "template": "template Artefacto Encontrado"
}

batallaFinal = {
    "name_action": "Batalla Final",
    "precondition": [Pre_Amenaza],
    "post_conditions": [Post_NoAmenaza],
    "template": "template Batalla Final"
}

tierrasNatalesSafe = {
    "name_action": "Tierras Natales a Salvo",
    "precondition": [Pre_TierrasNatales],
    "post_conditions": [Post_TierrasNatalesSafe],
    "template": "template Tierras Natales Safe"
}

reconocimientoMundial = {
    "name_action": "Reconocimiento Mundial",
    "precondition": [Pre_ReconocimientoMundial],
    "post_conditions": [Post_Reconocimiento],
    "template": "template Reconocimiento Mundial"
}

# Diccionario principal
diccionarioAcciones = {
    "Inicio de la Amenaza": amenazaDespierta,
    "Peligro en las Tierras Natales": tierrasNatalesDanger,
    "Caminar al Salon de Clases": walkSalonClases,
    "Caminar al Dormitorio": walkDormitorio,
    "Caminar a la Mazmorra": walkMazmorra,
    "Caminar al Comedor": walkComedor,
    "Caminar a la Biblioteca": walkBiblioteca,
    "Caminar a la Puerta Principal": walkPuertaPrincipal,
    "Caminar a los Pasillos": walkPasillo,
    "Caminar a la Casa": walkCasa,
    "Caminar al Bosque Encantado": walkBosqueEncantado,
    "Caminar al Templo de Quetzalcoatl": walkTemploQuetzalcoatl,
    "Caminar al Abismo de Tlaloc": walkAbismoTlaloc,
    "Aprender Magia": aprenderMagia,
    "Aprender Tipo de Magia": tipodeMagia,
    "Desafio Magico": desafioMagico,
    "Interactuar con Alumnos": interactuar,
    "Busqueda de Codices": busquedaCodices,
    "Busqueda de Artefacto": busquedaArtefacto,
    "Hablar con Quetzalcóatl": hablarQuetzalcoatl,
    "Aprendisaje Avanzado": aprendisajeAvanzado,
    "Artefacto Encontrado": artefactoEncontrado,
    "Batalla Final": batallaFinal,
    "Tierras Natales a Salvo": tierrasNatalesSafe,
    "Reconocimiento Mundial": reconocimientoMundial
}


def realizar_Action(character, personajeGet, name_action, numPostCondition):
    # Verificar si la acción existe en el diccionarioAcciones
    registrar_mensaje("Verificar si la acción existe en el diccionarioAcciones")
    if name_action in diccionarioAcciones:
        action = diccionarioAcciones[name_action]
        registrar_mensaje("Se crea la accion para ejecutarla")
        # Si no existe el archivo de BD, lo crea
        story_actions = Story_Actions(
            action["name_action"],
            character.get_name(),
            action["precondition"],
            action["post_conditions"],
            action["template"]
        )
        #Registro Bitacora
        registrar_mensaje('Se creo el objeto accion "'+ action["name_action"] +'":', nivel=logging.DEBUG)
        registrar_objeto(story_actions, nivel=logging.DEBUG)
        # Inicia la acción
        story_actions.ejecutar(character, personajeGet, numPostCondition)
    else:
        registrar_mensaje("La acción no existe en el diccionario Acciones", nivel=logging.ERROR)
