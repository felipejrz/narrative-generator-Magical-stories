import random

def Post_SurgeAmenaza():
    return True

def Post_TierrasNatalesDanger():
    return "En Peligro"

def Post_SalonClases():
    return "el Salón de Clases"

def Post_Dormitorio():
    return "los Dormitorios"

def Post_Mazmorra():
    return "la Mazmorra"

def Post_Comedor():
    return "el Comedor"

def Post_Biblioteca():
    return "la Biblioteca"

def Post_PuertaPrincipal():
    return "la Puerta Principal de Kukulkan"

def Post_BosqueEncanatado():
    return "el Bosque Encantado de Cuetzpalin"

def Post_TemploQuetzalcoatl():
    return "el Templo de Quetzalcoatl"

def Post_AbismoTlaloc():
    return "el Abismo Tlaloc"

def Post_Pasillo():
    return "los Pasillos"

def Post_Casa():
    return "su Casa"

def Post_MagiaBasica():
    return "Basico"

def Post_TipoMagia():
    tipoMagic = ["Jaguar", "Serpiente", "Mono araña", "Cocodrilo", "Guajolote", "Tapir", "Armadillo"]
    return random.choice(tipoMagic)

def Post_MagiaIntermedia(): 
    return "Intermedia"

def Post_Amigos():
    nombre = ["Balam", "Kukulkan", "Ah Puch", "Chac", "Xibalba", "Yum Cimil", "Ix Chel", "Kukumatz", "Ah Mun", "Ah Cacao", "Hunahpu", "Ixik", "Yum Kimil", "Chaac", "Hunab Ku", "K'uk'", "Yumil Kaxob"]
    return random.choice(nombre)

def Post_InformacionBasicas():
    return "Basicas"

def Post_Valentia():
    return True

def Post_MagiaAvanzada():
    return "Avanzada"

def Post_InformacionAvanzadas():
    return "Avanzada"

def Post_NoAmenaza():
    return False

def Post_TierrasNatalesSafe():
    return "A Salvo"

def Post_Reconocimiento():
    return True