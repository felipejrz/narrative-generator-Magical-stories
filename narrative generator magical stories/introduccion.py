import random
from character_structure import *

def seleccionName():
    nombre = ["Ixchel", "Hunahpu", "Itzamna", "Yum Kaax", "Ixtab", "Ixpiyacoc", "Xquic", "Hunab Ku", "Ah Mun", "Ek Chuah", "K'aparoso", "Iwan", "Sahlma", "Phredo", "Phelip", "Mow", "Chu'mi"]
    return random.choice(nombre)

def seleccionLocation():
    return "su Casa"
