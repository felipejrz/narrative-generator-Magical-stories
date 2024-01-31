import logging
import os

def configurar_bitacora():
    # Eliminar el archivo de bitácora anterior si existe
    log_filename = 'bitacora.log'
    if os.path.exists(log_filename):
        os.remove(log_filename)

    # Configurar la nueva bitácora
    logging.basicConfig(filename=log_filename, level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def registrar_mensaje(mensaje, nivel=logging.INFO):
    logging.log(nivel, mensaje)

def registrar_objeto(objeto, nivel=logging.INFO):
    mensaje = repr(objeto)  # Convierte el objeto en una cadena
    registrar_mensaje(mensaje, nivel)