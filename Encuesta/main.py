from numpy import linspace 
from persona import Persona
import operator as op
import matplotlib.pyplot as plt

def noInAnswere(answer):
    no_answers = ["No", "no", "nada", "ninguna", "Ninguna", "N/A", "Nop", "Nopp"]

    for no in no_answers:
        if no in answer:
            return True
    
    return False

def createPersonsVector():
    # creamos una matriz con cada linea en new data #
    new_data = []
    file = open("encuesta2.tsv", "r")
    for line in file:
        new_data.append(line.strip().split("\t"))
    file.close

    # por cada linea creamos un objeto de persona y lo añadimos al vector 
    vec_personas = []
    for i in range( 1, len(new_data) ):
        # inicializamos todas las propiedades con la info 
        vec_personas.append( Persona(
            edad               = new_data[i][0],
            lugar              = new_data[i][1],
            new_red_social     = True if new_data[i][2] == "Sí" else False, 
            tiempo_aumento     = True if new_data[i][3] == "Sí" else False,                      #3 bool
            redes_fav_des      = new_data[i][4],          
            ver_amig_durante   = new_data[i][5],        
            ver_amig_antes     = new_data[i][6],         
            actividad_out      = False if noInAnswere(new_data[i][7]) else True,
            actividad_in       = False if noInAnswere(new_data[i][8]) else True,       
            salir_fiesta       = new_data[i][9],            
            alejarse           = True if new_data[i][10] == "Sí" else False, 
            nuevos_amigos      = True if new_data[i][11] == "Sí" else False, 
            perdida            = True if new_data[i][12] == "Sí" else False, 
            clases_online      = new_data[i][13],           
            interaccion_online = new_data[i][14],     
            clases_online_like = new_data[i][15],
            antes              = new_data[i][16],                 
            despues            = new_data[i][17],
        ))

    return vec_personas

def cambioDeFelicidad(poblacion, operator):
    counter = 0

    for person in poblacion:
        if operator(person.antes, person.despues):
            counter += 1
    
    return counter

def cambioDeFelicidad(poblacion, operator):
    counter = 0

    for person in poblacion:
        if operator(person.antes, person.despues):
            counter += 1
    
    return counter

def promedioFelicidad(poblacion, momento):
    felicidad_total = 0
    count = 0
    
    for person in poblacion:
        felicidad_total += momento(person)
        count += 1
    
    return felicidad_total / count


def felicidadGeneral(poblacion, title):
    sizes = [ cambioDeFelicidad(poblacion, op.lt), 
              cambioDeFelicidad(poblacion, op.eq), 
              cambioDeFelicidad(poblacion, op.gt) ]

    #labels = [f"Aumento: {sizes[0]}", f"Igual: {sizes[1]}", f"Disminuyo: {sizes[2]}"]
    labels = [f"Aumento:", f"Igual:", f"Disminuyo:"]
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, shadow=True, autopct='%1.1f%%')
    plt.title(title)
    plt.show()

    # lt <
    # eq ==
    # gt >

def perdidaInfluencia(poblacion):
    sub_pobla = []
    for person in poblacion:
        if person.perdida:
            sub_pobla.append(person)

    #print(len(sub_pobla))
    print(promedioFelicidad(sub_pobla, Persona.getAntes))
    print(promedioFelicidad(sub_pobla, Persona.getDespues))
    felicidadGeneral(sub_pobla, "Felicidad despues de la pandemia. (personas con perdidas)")


def antesDespuesBar(x, y_1, y_2, title):
    fig, ax = plt.subplots()
    ax.bar(x, y_1, label="Antes")
    ax.bar(x, y_2, label="Despues")
    ax.text(x[0], y_1[0]-.3, round(y_1[0],1))
    ax.text(x[0], y_2[0]-1, round(y_2[0],1))
    ax.text(x[1], y_1[1]-.3, round(y_1[1],1))
    ax.text(x[1], y_2[1]-1, round(y_2[1],1))
    
    plt.title(title)
    plt.legend(loc='lower right')
    plt.show()

def edadesAnalisis(poblacion):
    menores_sub_p = []
    mayores_sub_p = []

    for person in poblacion:
        if person.edad < 18:
            menores_sub_p.append(person)
        else:
            mayores_sub_p.append(person)
    
    print( f"Promedio antes mayores: {promedioFelicidad(mayores_sub_p, Persona.getAntes) }")
    print( f"Promedio antes menores: {promedioFelicidad(menores_sub_p, Persona.getAntes) }")
    print()
    print( f"Promedio despues mayores: {promedioFelicidad(mayores_sub_p, Persona.getDespues) }")
    print( f"Promedio despues menores: {promedioFelicidad(menores_sub_p, Persona.getDespues) }")

    x = ["Mayores", "Menores"]

    y_1 = [promedioFelicidad(mayores_sub_p, Persona.getAntes), 
           promedioFelicidad(menores_sub_p, Persona.getAntes)]

    y_2 = [promedioFelicidad(mayores_sub_p, Persona.getDespues),
           promedioFelicidad(menores_sub_p, Persona.getDespues)]
    
    antesDespuesBar(x, y_1, y_2, "Felicidad por edad")

def analisiRedes_1(poblacion):
    tiempo_aumento = [0, 0]
    labels = ["Tiempo aumento", "Tiempo no aumento"]
    
    for persona in poblacion:
        if not persona.new_red_social:
            if persona.tiempo_aumento:
                tiempo_aumento[0] += 1
            else:
                tiempo_aumento[1] += 1

    sub_poblacion = tiempo_aumento[0] + tiempo_aumento[1]
    # labels = [f"Tiempo aumento: {tiempo_aumento[0]}", f"Tiempo no aumento {tiempo_aumento[1]}"]
    labels = [f"Tiempo aumento", f"Tiempo no aumento"]


    fig1, ax1 = plt.subplots()
    ax1.pie(tiempo_aumento, labels=labels, shadow=True, autopct='%1.1f%%')
    plt.title(f"Personas que no usaron una nueva red social.  Sub-población: {sub_poblacion}")
    plt.show()

def analisisRedes_2(poblacion):
    desfavorecieron = []
    ayudaron = []

    for persona in poblacion:
        if persona.redes_fav_des <= 5:
            desfavorecieron.append(persona)
        else:
            ayudaron.append(persona)
    
    print(f"Personas que desfavorecieron, felicidad promedio despues: {promedioFelicidad(desfavorecieron, Persona.getDespues)}")
    print(f"Personas que ayudaron, felicidad promedio despues: {promedioFelicidad(ayudaron, Persona.getDespues)}")
    
    
    x = ["Ayudaron", "Desfavorecieron"]

    y_1 = [promedioFelicidad(ayudaron, Persona.getAntes), 
            promedioFelicidad(desfavorecieron, Persona.getAntes)]

    y_2 = [promedioFelicidad(ayudaron, Persona.getDespues), 
            promedioFelicidad(desfavorecieron, Persona.getDespues)]
    
    antesDespuesBar(x, y_1, y_2, "Felicidad con redes")

def analisisActividades(poblacion):
    vec_act_out = []
    vec_no_act_out = []
    vec_act_in =  []
    vec_no_act_in = []

    for persona in poblacion:

        if persona.actividad_out:
            vec_act_out.append(persona)
        else:
            vec_no_act_out.append(persona)
    
        if persona.actividad_in:
            vec_act_in.append(persona)
        else:
            vec_no_act_in.append(persona)

    x = ["Dejaron actividad", "No dejaron actividad"]
    x_2 = ["Empezaron actividad", "No empeazaron actividad"]

    y_1 = [promedioFelicidad(vec_act_out, Persona.getAntes),
            promedioFelicidad(vec_no_act_out, Persona.getAntes)]
    
    y_2 = [promedioFelicidad(vec_no_act_out, Persona.getDespues),
            promedioFelicidad(vec_act_out, Persona.getDespues)]

    y_1_1 = [promedioFelicidad(vec_act_in, Persona.getAntes),
            promedioFelicidad(vec_no_act_in, Persona.getAntes)]
    
    y_2_2 = [promedioFelicidad(vec_act_in, Persona.getDespues),
            promedioFelicidad(vec_no_act_in, Persona.getDespues)]

    #print(len(vec_no_act_out))
    #antesDespuesBar(x, y_1, y_2, "Felicidad dejando actividad")
    antesDespuesBar(x_2, y_1_1, y_2_2, "Felicidad adquiriendo actividad")

if __name__ == "__main__":
    vec_personas = createPersonsVector() # Total: 145
    
    # felicidadGeneral(vec_personas, "Felicidad despues de pandemia.")
    perdidaInfluencia(vec_personas)
    # edadesAnalisis(vec_personas)
    # analisiRedes_1(vec_personas)
    # analisisRedes_2(vec_personas)
    # analisisActividades(vec_personas)
    
    
