class Character:
    def __init__(self, name=None, location=None, nvlMagic=None, typeMagic=None, arma="Varita Magica", amigos=None, valentia=False, informacion=None, reconocimiento=False, amenaza=False, tierrasNatales="En Peligro"):
        self.name = name
        self.location = location
        self.nvlMagic = nvlMagic
        self.typeMagic = typeMagic
        self.arma = arma
        self.amigos = amigos
        self.valentia = valentia
        self.informacion = informacion
        self.reconocimiento = reconocimiento
        self.amenaza = amenaza
        self.tierrasNatales = tierrasNatales

    # Getters
    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_nvlMagic(self):
        return self.nvlMagic

    def get_typeMagic(self):
        return self.typeMagic

    def get_arma(self):
        return self.arma

    def get_amigos(self):
        return self.amigos

    def get_valentia(self):
        return self.valentia

    def get_informacion(self):
        return self.informacion
    
    def get_reconocimiento(self):
        return self.reconocimiento

    def get_amenaza(self):
        return self.amenaza

    def get_tierrasNatales(self):
        return self.tierrasNatales

    # Setters
    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

    def set_nvlMagic(self, nvlMagic):
        self.nvlMagic = nvlMagic

    def set_typeMagic(self, typeMagic):
        self.typeMagic = typeMagic

    def set_arma(self, arma):
        self.arma = arma

    def set_amigos(self, amigos):
        self.amigos = amigos

    def set_valentia(self, valentia):
        self.valentia = valentia

    def set_informacion(self, informacion):
        self.informacion = informacion
    
    def set_reconocimiento(self, reconocimiento):
        self.reconocimiento = reconocimiento

    def set_amenaza(self, amenaza):
        self.amenaza = amenaza

    def set_tierrasNatales(self, tierrasNatales):
        self.tierrasNatales = tierrasNatales
