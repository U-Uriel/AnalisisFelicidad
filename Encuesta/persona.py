class Persona:
    edad                = 0      #0 
    lugar               = ""     #1
    new_red_social      = False  #2 
    tiempo_aumento      = False  #3 
    redes_fav_des       = 0      #4  1-10
    ver_amig_durante    = 0      #5 
    ver_amig_antes      = 0      #6 
    actividad_out       = False  #7 
    actividad_in        = False  #8
    salir_fiesta        = 0      #9 
    alejarse            = False  #10 
    nuevos_amigos       = False  #11
    perdida             = False  #12 
    clases_online       = 0      #13 
    interaccion_online  = 0      #14 
    clases_online_like  = 0  #15 
    antes               = 0      #16 
    despues             = 0      #17

    def __init__(self) -> None:
        pass

    def __init__(self, edad, lugar, new_red_social, tiempo_aumento,
        redes_fav_des, ver_amig_durante, ver_amig_antes, 
        actividad_out, actividad_in, salir_fiesta, alejarse,
        nuevos_amigos, perdida, clases_online, interaccion_online,
        clases_online_like, antes, despues):

        self.edad                   = int(edad)
        self.lugar                  = lugar
        self.new_red_social         = new_red_social
        self.tiempo_aumento         = tiempo_aumento
        self.redes_fav_des          = int(redes_fav_des)
        self.ver_amig_durante       = int(ver_amig_durante)
        self.ver_amig_antes         = int(ver_amig_antes)
        self.actividad_out          = actividad_out
        self.actividad_in           = actividad_in
        self.salir_fiesta           = int(salir_fiesta)
        self.alejarse               = alejarse
        self.nuevos_amigos          = nuevos_amigos
        self.perdida                = perdida
        self.clases_online          = int(clases_online)
        self.interaccion_online     = int(interaccion_online)
        self.clases_online_like     = clases_online_like
        self.antes                  = int(antes)
        self.despues                = int(despues)

    def getAntes(self):
        return self.antes
    
    def getDespues(self):
        return self.despues
        


