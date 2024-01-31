import random
from character_structure import *

def templateInicioAmenaza(character):
    phrases = [
            f"En la penumbra de un crepúsculo dorado, cuando las sombras de la noche empiezan a alargarse y la magia se despierta en el aire, un susurro se extiende por el mundo mágico. Las estrellas titilan como secretos ocultos, y todos los corazones se llenan de temor, pues un mago tenebroso se alza en las sombras.",
            f"Hace milenios, un pacto de paz fue sellado en el reino de la magia. Pero ahora, las runas ancestrales se resquebrajan, y el viento murmura historias de traición. Un mago tenebroso, despiadado y sediento de poder, amenaza con romper el equilibrio y sumir al mundo mágico en la oscuridad eterna.",
            f"En los rincones más oscuros y remotos del mundo mágico, los habitantes susurran el nombre de un mago tenebroso cuyo poder eclipsa el sol. La profecía se cumple, y la llegada de este oscuro hechicero está a punto de sumir todo en el caos.",
            f"Cuando la luna se tiñe de un rojo profundo y ominoso, el mundo mágico entero tiembla. La antigua profecía se despierta, anunciando la llegada del mago tenebroso, cuyas sombras amenazan con devorar la magia y la esperanza.",
            f"En el corazón del bosque encantado, un rugido oscuro se alza, rompiendo el silencio ancestral. Las bestias mágicas, guardianas de la armonía, se inquietan, pues sienten la proximidad de un mago tenebroso que busca someter su poder.",
            f"En las páginas de un libro olvidado y cubierto de polvo, las runas ancestrales cuentan una historia inquietante. El mago tenebroso, largo tiempo olvidado, emerge de las sombras, decidido a reclamar el trono del mundo mágico.",
            f"Un velo de oscuridad se cierne sobre el mundo mágico, y las estrellas se atenúan, incapaces de competir con el resplandor siniestro del mago tenebroso. La esperanza se desvanece, mientras su sombra se alarga.",
            f"Cuando los soles gemelos se alinean en un eclipse mágico, una profecía ancestral se cumple. El mago tenebroso, con un poder indescriptible, emerge de las sombras para reclamar su dominio sobre el mundo de la magia.",
            f"El bosque encantado, siempre un refugio de paz, exhala un suspiro tembloroso. Los árboles centenarios y las criaturas mágicas sienten la oscuridad acercándose, mientras el mago tenebroso avanza, con el deseo de subyugarlos a todos.",
            f"Los cuatro elementos, antiguos guardianes del mundo mágico, empiezan a agitarse. La tierra tiembla, el agua se agita, el viento susurra y el fuego arde con furia. Un mago tenebroso, desafiando a la misma naturaleza, se alza como una tormenta imparable."
        ]
    return random.choice(phrases)

def templateTierrasNatalesDanger(character):
    phrases = [
        f"{character} vivía una vida común en su pacífico pueblo de Teotihuacán, hasta que un sacerdote maya lo visitó con una inscripción sagrada que anunciaba su admisión a la prestigiosa escuela mágica Kukulkán. Un nuevo mundo se abría ante él, un mundo que lo prepararía para enfrentar al mago tenebroso y salvar su tierra natal.",
        f"Desde niño, {character} había observado los astros con asombro en las noches claras de Teotihuacán. Un día, las constelaciones parecieron alinearse, y un anciano sabio maya llegó para reclamarlo como estudiante, ya que los astros lo habían elegido para proteger su hogar de la amenaza del mago tenebroso.",
        f"En el templo ancestral de Teotihuacán, {character} encontró un pergamino mágico oculto que revelaba su legado como mago. Kukulkán lo convocó para entrenar y enfrentar al mago tenebroso que amenazaba con sumir su tierra natal en las sombras.",
        f"Desde niño, {character} soñaba con aventuras mágicas y la salvación de Teotihuacán. Sus sueños se hicieron realidad cuando fue aceptado en la escuela Kukulkán, donde aprendería los secretos que le permitirían enfrentar al mago tenebroso y cumplir su destino.",
        f"Durante una visita al templo ancestral de Teotihuacán, {character} descubrió una antigua profecía que hablaba de un elegido de Kukulkán destinado a salvar su tierra. Su elección como estudiante de la escuela mágica marcó el comienzo de su viaje hacia la confrontación con el mago tenebroso.",
        f"En el décimo cumpleaños de {character}, su abuela le reveló un legado mágico que había estado oculto durante generaciones. La escuela Kukulkán lo llamó, y su entrenamiento se convirtió en la única esperanza de salvación para Teotihuacán.",
        f"Mientras exploraba un bosque sagrado en las afueras de Teotihuacán, {character} se encontró con un portal mágico que lo llevó directamente a la escuela Kukulkán. Allí, se enteró de su destino como protector de su tierra natal contra el mago tenebroso.",
        f"Cuando una serie de eventos misteriosos empezaron a ocurrir en Teotihuacán, {character} descubrió que poseía un don mágico innato. Fue entonces cuando Kukulkán lo aceptó como estudiante y le encomendó la tarea de enfrentar al mago tenebroso.",
        f"Un día, {character} se encontró con un sacerdote maya errante en las tierras de Teotihuacán. Este sacerdote reveló la amenaza del mago tenebroso y lo llevó a la escuela Kukulkán para desbloquear su potencial y salvar su hogar.",
        f"{character} creció en Teotihuacán, sin conocer su destino mágico, hasta que un misterioso pergamino llegó a sus manos, desencadenando su viaje hacia la escuela Kukulkán y la confrontación con el mago tenebroso.",
        f"Las antiguas ruinas de Teotihuacán ocultaban un secreto ancestral que solo {character} podía descifrar. Su conexión con Kukulkán lo llevó a la escuela mágica y al deber de salvar su tierra natal.",
        f"Un cometa brillante cruzó el cielo de Teotihuacán la noche en que {character} descubrió su habilidad mágica. Kukulkán lo llamó para luchar contra el mago tenebroso y proteger su hogar.",
        f"La tranquilidad de Teotihuacán se vio amenazada cuando una misteriosa sombra se cernió sobre el pueblo. {character} recibió la llamada de Kukulkán para convertirse en el defensor de su tierra natal.",
        f"{character} llevaba una vida sencilla en Teotihuacán hasta que un mensaje cifrado llegó a sus manos, revelando su legado mágico y el peligro que acechaba a su tierra natal.",
        f"Los espíritus ancestrales de Teotihuacán eligieron a {character} como su campeón contra el mago tenebroso. La escuela Kukulkán lo recibió con los brazos abiertos y un destino que cumplir.",
        f"El eco de antiguas profecías llenó las noches de Teotihuacán, y {character} supo que estaba destinado a enfrentar al mago tenebroso y salvar su hogar.",
        f"{character} siempre sintió una conexión especial con las tierras de Teotihuacán, pero no fue hasta que Kukulkán lo llamó que descubrió su verdadero propósito como mago protector de su tierra natal.",
        f"Un antiguo tomo de magia descubierto en la biblioteca de Teotihuacán reveló a {character} su destino como el elegido para enfrentar al mago tenebroso. La escuela Kukulkán sería su guía en esta épica lucha.",
        f"Las estrellas en el cielo de Teotihuacán guiaron el camino de {character} hacia la escuela mágica Kukulkán, donde se entrenaría para enfrentar al mago tenebroso y salvar su hogar.",
    ]
    return random.choice(phrases)


def templateWalk(character, inicio, destino):
    phrases = [
        f"{character} se embarcó en su viaje hacia {destino} con determinación en el corazón.",
        f"Avanzó sin descanso desde {inicio} hacia {destino}, con la mente puesta en el objetivo.",
        f"En su camino hacia {destino}, {character} disfrutó del paisaje mientras caminaba desde {inicio}.",
        f"{character} avanzó de manera constante en su travesía hacia {destino}, sin mirar atrás.",
        f"Corriendo con energía, se desplazó hacia {destino} desde {inicio} sin obstáculos en el camino.",
        f"Deslizándose con gracia, exploró el trayecto hacia {destino} desde {inicio}, atento a cada detalle.",
        f"Navegando con confianza, se movió sin desviarse del rumbo desde {inicio} hacia {destino}.",
        f"Marchando con valentía, cruzó el trayecto hacia {destino}, listo para enfrentar lo que le esperaba.",
        f"Transitando el camino, {character} sintió una sensación de anticipación y emoción mientras se acercaba a {destino}.",
        f"{character} siguió su camino con la seguridad de que cada paso lo acercaba a {destino}.",
        f"En su travesía hacia {destino}, mostró un compromiso inier obstáculo con fuerza y convicción.",
        f"{character} disfrutó del viaje hacia {destino}, encontrando belleza quebrantable y una determinación férrea.",
        f"{character} se abrió paso desde {inicio} hacia {destino}, superando cualquen cada rincón del camino desde {inicio}.",
        f"{character} se mantuvo en movimiento constante en su camino hacia {destino}, sin distracciones ni descansos.",
        f"Corriendo con pasión, se desplazó desde {inicio} hacia {destino}, impulsado por un sentido de propósito imparable.",
        f"Durante su travesía, caminó con confianza hacia {destino}, sabiendo que su destino estaba cerca desde {inicio}.",
        f"Con determinación inquebrantable, avanzó sin pausa hacia {destino}, centrado en su objetivo final desde {inicio}.",
        f"Guiado por un sentido de aventura, exploró el camino hacia {destino} desde {inicio}, ansioso por descubrir lo que le deparaba.",
        f"{character} se desplazó con elegancia y gracia hacia {destino} desde {inicio}, dejando una huella de determinación en su camino.",
        f"Con un corazón valiente, avanzó hacia {destino}, preparado para enfrentar cualquier desafío que se cruzara en su camino.",
        f"Siguiendo su camino, {character} demostró una fuerza de voluntad inquebrantable mientras avanzaba hacia {destino}.",
        f"Navegó hacia {destino} con una confianza inquebrantable en su corazón desde {inicio}.",
        f"Abrazó la travesía hacia {destino} con un espíritu decidido y sin vacilaciones desde {inicio}.",
        f"Avanzó con convicción hacia {destino}, demostrando una resistencia inquebrantable en su viaje desde {inicio}.",
        f"Con pasos firmes, {character} recorrió el camino hacia {destino} sin mirar atrás desde {inicio}.",
        f"Recorrió la distancia entre {inicio} y {destino} con una dedicación implacable y un propósito claro.",
        f"Disfrutando del viaje, exploró el sendero hacia {destino}, encontrando belleza en cada paso desde {inicio}.",
        f"Avanzó decidido hacia {destino}, superando obstáculos con valentía en su travesía desde {inicio}.",
        f"Se adentró en el camino hacia {destino} con un sentido de aventura palpable desde {inicio}.",
        f"En su travesía, transitó con determinación el camino hacia {destino}, siguiendo su sueño con pasión desde {inicio}.",
        f"Avanzó con gracia y determinación hacia {destino}, dejando una huella indeleble en su camino desde {inicio}.",
        f"Sin descanso, recorrió el camino hacia {destino}, demostrando una resistencia inquebrantable desde {inicio}.",
        f"Cruzó la distancia hacia {destino} con un corazón lleno de valentía y confianza desde {inicio}.",
        f"Encontró inspiración en cada paso que dio hacia {destino}, avanzando con pasión y determinación desde {inicio}.",
        f"Se sumergió en su viaje hacia {destino} con un compromiso inquebrantable desde {inicio}.",
        f"Con un espíritu intrépido, recorrió el sendero hacia {destino}, listo para enfrentar lo desconocido desde {inicio}.",
        f"Avanzó con resolución hacia {destino}, confiado en que cada paso lo acercaba a su destino desde {inicio}.",
        f"Guiado por una sed de aventura, exploró el camino hacia {destino}, ansioso por lo que el futuro le deparaba desde {inicio}.",
        f"Avanzó con elegancia y gracia hacia {destino}, dejando una huella de determinación en su camino desde {inicio}.",
        f"Con un corazón valiente, avanzó hacia {destino}, preparado para enfrentar cualquier desafío en su camino desde {inicio}.",
        f"Se sumergió en su travesía hacia {destino}, comprometido con su objetivo y sin vacilaciones desde {inicio}.",
        f"Con una confianza inquebrantable, avanzó sin descanso hacia {destino}, siguiendo su destino con pasión desde {inicio}.",
        f"Emprendiendo su viaje, caminó con determinación hacia {destino}, demostrando su resolución inquebrantable desde {inicio}.",
    ]
    return random.choice(phrases)


def templateBasicMagical(character):
    phrases = [
        f"{character} descubrió su potencial mágico en las aulas de la prestigiosa escuela de magia. Emocionado por las posibilidades, comenzó un riguroso entrenamiento para dominar los fundamentos de la magia.",
        f"En su búsqueda de conocimiento mágico, {character} se convirtió en un estudiante dedicado en la academia de magia, donde pasaba horas estudiando y practicando hechizos básicos.",
        f"{character} se entregó de lleno a la magia, embarcándose en un viaje de autodescubrimiento y entrenamiento constante. Cada día en la escuela lo acercaba un paso más a su potencial mágico.",
        f"Guiado por los sabios profesores de la escuela de magia, {character} profundizó en los secretos de las artes arcanas, desarrollando un profundo entendimiento de la magia y sus aplicaciones.",
        f"La magia se convirtió en el núcleo de la vida de {character}, tejida en su identidad y propósito. A medida que avanzaba en su entrenamiento, su poder mágico crecía constantemente, abriendo un mundo de posibilidades.",
        f"En la escuela de magia, {character} se destacó como un aprendiz prodigio, asombrando a sus compañeros y profesores con su destreza mágica. Su dedicación y habilidad eran insuperables.",
        f"Enfrentando desafíos mágicos aparentemente insuperables dados por sus profesores, {character} no se amedrentó. Cada desafío lo impulsó a crecer en habilidad y poder mágico, forjando su camino hacia la grandeza.",
    ]
    return random.choice(phrases)


def templateMagicAffinity(character, magic_type):
    phrases = [
        f"Durante una incursión en la mazmorra, {character} hizo un sorprendente descubrimiento, su afinidad innata con la magia de {magic_type}.",
        f"{character} explorando las profundidades de la mazmorra, sintió una conexión profunda con la magia de {magic_type}.",
        f"En una encrucijada oscura dentro de la mazmorra, {character} experimentó una revelación mágica, descubriendo su afinidad con la magia de {magic_type}.",
        f"{character} desenterró un antiguo grimorio en la mazmorra, revelando su innata habilidad con la magia de {magic_type}.",
        f"En una misteriosa cámara mágica de la mazmorra, {character} desbloqueó su potencial mágico, alineándose con la magia de {magic_type}.",
        f"{character} atrajo la atención de una entidad mágica en la mazmorra, que le otorgó el don de dominar la magia de {magic_type}.",
        f"Después de enfrentar peligros inimaginables en la mazmorra, {character} emergió con un poder mágico innato, relacionado con el tipo {magic_type}.",
    ]
    return random.choice(phrases)

def templateMagicChallenge(character):
    phrases = [
        f"La escuela de magia organizó un desafío único, y {character} se enfrentó a él con valentía. Cada prueba superada en la competencia escolar aumentó su habilidad mágica.",
        f"En la academia de magia, se llevó a cabo una prueba desafiante para los estudiantes, y {character} la afrontó como una oportunidad para crecer. Cada fase del desafío en el entorno escolar le permitió mejorar su magia.",
        f"{character} participó en un torneo mágico dentro de la escuela, compitiendo contra otros estudiantes en un despliegue de poder y destreza. A medida que avanzaba en el torneo escolar, su magia se volvía más formidable.",
        f"Durante su tiempo en la escuela de magia, {character} se encontró con un antiguo grimorio mágico que desafió a los estudiantes a desentrañar sus secretos. Al explorar sus páginas en el entorno escolar, su magia se volvía más profunda y poderosa.",
        f"Bajo la tutela de un mentor mago en la academia de magia, {character} se embarcó en una búsqueda mágica en el entorno escolar, que lo llevó a enfrentar pruebas místicas y superar desafíos mágicos. Cada victoria fortaleció su habilidad mágica en el contexto escolar.",
    ]
    return random.choice(phrases)

def templateCharacterMeeting(obj_character, other_character):
    character = obj_character.get_name()
    if obj_character.get_location() == "el Comedor":
        phrases = [
            f"{character} conoció a {other_character} en el comedor durante una comida compartida y pronto se dieron cuenta de que compartían intereses en común.",
            f"Compartiendo una mesa en el comedor, {character} y {other_character} comenzaron a conversar y descubrieron una afinidad mutua.",
            f"Durante una comida en el comedor, {character} y {other_character} se cruzaron y entablaron una conversación, estableciendo una conexión instantánea.",
            f"{character} y {other_character} se encontraron en el comedor y comenzaron a charlar sobre sus pasiones y aventuras, lo que rápidamente los unió en amistad.",
            f"En una comida casual en el comedor, {character} y {other_character} compartieron anécdotas y descubrieron intereses comunes, lo que fortaleció su vínculo.",
        ]
    elif obj_character.get_location() == "los Dormitorios":
        phrases = [
            f"{character} conoció a {other_character} en su dormitorio compartido como nuevo compañero de cuarto. Al principio, eran extraños, pero rápidamente se hicieron amigos inseparables.",
            f"Por la noche, {character} y {other_character} entablaron una conversación en su dormitorio compartido y descubrieron que tenían mucho en común, lo que fortaleció su amistad.",
            f"La primera vez que {character} y {other_character} compartieron el dormitorio, se dieron cuenta de que tenían intereses similares y comenzaron a forjar una sólida amistad.",
            f"{character} y {other_character} se convirtieron en compañeros de cuarto en el dormitorio, y su amistad creció a medida que compartían historias y experiencias en su nuevo hogar compartido.",
            f"Compartir el dormitorio con {other_character} resultó en una amistad inesperada para {character}. Sus conversaciones nocturnas los unieron en una sólida relación.",
        ]
    return random.choice(phrases)


def templateLibraryDiscovery(obj_character):
    character = obj_character.get_name()
    secondary_character = obj_character.get_amigos()
    magical_language = obj_character.get_typeMagic()
    phrases = [
        f"Mientras exploraba la biblioteca, {character} hizo un descubrimiento intrigante. {secondary_character} notó que las páginas del antiguo códice, escrito en el lenguaje de {magical_language}, parecían relatar secretos milenarios que solo {character} podía entender. Al descifrar el códice, encontraron una pista crucial para su búsqueda del señor tenebroso era un artefacto mágico ubicado en el Bosque Encantado.",
        f"En la sección de libros prohibidos de la biblioteca, {character} encontró un códice misterioso. Su amigo, {secondary_character}, se dio cuenta de que el lenguaje utilizado en el libro, un dialecto mágico ancestral, estaba lleno de sabiduría perdida, y solo {character} podía descifrarlo. La lectura del códice les proporcionó una pista vital para encontrar un artefacto en el Bosque Encantado.",
        f"Mientras exploraba la biblioteca, {character} se topó con un códice encriptado, y junto a {secondary_character}, notaron que las páginas estaban llenas de símbolos y caracteres extraños en lengua de {magical_language}. Ambos quedaron perplejos ante los misterios que encerraba. Al descifrar el códice, encontraron una pista esencial para su búsqueda del señor tenebroso, era un artefacto ubicadoe en el Bosque Encantado.",
        f"Explorando entre las estanterías polvorientas, {character} hizo un hallazgo extraordinario. {secondary_character} notó que el códice antiguo, con páginas que parecían susurrar secretos ancestrales en {magical_language}, podría contener conocimientos únicos. Al estudiar el códice, encontraron una pista crucial para su búsqueda un artefacto ubicadoe en el Bosque Encantado.",
        f"Entre los libros olvidados de la biblioteca, {character} descubrió un códice enigmático. {secondary_character} se maravilló al descubrir que el libro estaba lleno de conocimiento arcano escrito en un idioma que solo {character} podía descifrar, un lenguaje mágico antiguo. La lectura del códice les proporcionó una pista vital para encontrar un artefacto en el Bosque Encantado.",
    ]
    return random.choice(phrases)


def templateForestDiscovery(character):
    phrases = [
        f"Mientras {character} exploraba el Bosque Encantado de Cuetzpalin, descubrió pistas misteriosas que apuntaban al paradero del señor oscuro. Cada árbol y susurro del bosque parecía llevarlo más cerca de su destino.",
        f"En lo más profundo del Bosque Encantado de Cuetzpalin, {character} encontró una revelación sorprendente, pistas cruciales que lo llevarían a enfrentar al señor oscuro y poner fin a su reinado de terror.",
        f"Criaturas mágicas del Bosque Encantado guiaron a {character} hacia pistas ocultas que señalaban la ubicación del señor oscuro. Cada encuentro con estas criaturas era un paso hacia la confrontación final.",
        f"{character} desenterró el secreto del Bosque Encantado de Cuetzpalin, un enigma que lo conduciría directamente al señor oscuro. Las pistas que descubrió iluminaron su camino hacia la confrontación inevitable.",
        f"En su búsqueda en el Bosque Encantado de Cuetzpalin, {character} descubrió un antiguo santuario mágico que ocultaba pistas ancestrales sobre el paradero del señor oscuro.",
        f"El Bosque Encantado de Cuetzpalin reveló sus secretos a {character} a medida que exploraba a fondo sus rincones mágicos. Cada hallazgo lo acercó más a su enfrentamiento con el señor oscuro.",
        f"Mientras recorría el Bosque Encantado, {character} tuvo un encuentro sorprendente con el espíritu guardián del bosque, quien le otorgó pistas vitales sobre la ubicación del señor oscuro.",
    ]
    return random.choice(phrases)

def templateTempleEncounter(character):
    phrases = [
        f"{character} se aventuró en el antiguo Templo de Quetzalcótal en busca de respuestas y sabiduría. Allí, en medio de la majestuosidad del templo, tuvo un encuentro con el propio Quetzalcótal. Durante la conversación, el dios serpiente infundió en {character} un profundo sentido de valentía y determinación, fortaleciendo su espíritu y preparándolo para el desafío que se avecinaba.",
        f"Explorando el antiguo Templo de Quetzalcótal, {character} se encontró con una inscripción mágica que lo transportó a una visión mística. En esta visión, recibió la bendición de Quetzalcótal, que llenó su corazón de coraje y sabiduría.",
        f"{character} se aventuró en el templo sagrado de Quetzalcótal en busca de guía y protección. En el interior, tuvo un encuentro místico con el dios serpiente, que lo dotó de poderes divinos para enfrentar las amenazas que se cernían sobre él.",
        f"En el Templo de Quetzalcótal, {character} descubrió un altar secreto donde se encontró con una manifestación del dios serpiente. El dios le otorgó una visión y una misión, fortaleciendo su determinación para cumplirla.",
    ]
    return random.choice(phrases)

def templateForestMagicPower(character):
    phrases = [
        f"Dentro del Bosque Encantado de Cuetzpalin, {character} desbloqueó un inmenso poder mágico, llevando sus habilidades a un nivel extremo.",
        f"Explorando el Bosque Encantado, {character} ascendió a un nivel de magia inimaginable, transformándose en un mago de poder sin igual.",
        f"En medio de la magia del Bosque Encantado de Cuetzpalin, {character} experimentó una transformación mágica profunda, fortaleciendo sus habilidades más allá de lo que creía posible.",
        f"{character} se sumergió en los misterios del Bosque Encantado y emergió con un poder mágico que desafía la comprensión, listo para enfrentar al señor oscuro con sus nuevas habilidades.",
        f"El Bosque Encantado reveló a {character} secretos antiguos que desbloquearon su máximo potencial mágico, convirtiéndolo en un mago excepcionalmente poderoso.",
    ]
    return random.choice(phrases)

def templateForestEncounter(obj_character):
    character = obj_character.get_name()
    phrases = [
        f"En el Bosque Encantado de Cuetzpalin, {character} se encontró cara a cara con gigantes ancestrales que guardaban el camino. La lucha fue ardua, pero al vencerlos, obtuvo una pista vital para encontrar el artefacto que lo llevaría al señor oscuro.",
        f"{character} se encontró a Tepoyóllotl, el mítico guardián del bosque. Para avanzar, tuvo que superar sus desafíos en una serie de pruebas. Al completarlas, ganó acceso a la ubicación del artefacto.",
        f"En medio del Bosque Encantado de Cuetzpalin, {character} se topó con un enigma antiguo y misterioso. Al resolverlo, desbloqueó el camino hacia el artefacto que le permitiría enfrentar al señor oscuro.",
        f"Explorando el Bosque Encantado de Cuetzpalin, {character} descubrió una aldea oculta de criaturas mágicas que le proporcionaron información crucial sobre la ubicación del artefacto que necesitaba.",
        f"Mientras viajaba por el Bosque Encantado de Cuetzpalin, {character} se encontró con un antiguo templo en ruinas. Después de superar peligros y desafíos, encontró pistas que lo llevarían al artefacto necesario para su enfrentamiento con el señor oscuro.",
    ]
    return random.choice(phrases)

def templateEpicBattle(obj_character):
    character = obj_character.get_name()
    weapon_name = obj_character.get_arma()
    phrases = [
        f"Tras varios días de incansable búsqueda, {character} finalmente encontró al mago oscuro en las profundidades del Abismo. La batalla que siguió fue una tormenta de hechizos y estrategia. {character} luchó con valentía, esquivando los poderosos hechizos del mago oscuro, y finalmente, con un golpe certero de su {weapon_name}, derrotó al malvado hechicero, poniendo fin a su amenaza y restaurando la paz en el reino.",
        f"Después de semanas de intensa búsqueda, {character} localizó al mago oscuro y se desencadenó un duelo mortal. Ambos magos desataron un torrente de hechizos que iluminó el oscuro abismo. {character}, empapado en sudor y determinación, empuñó su {weapon_name} legendaria, enfrentándose al mago oscuro con maestría. La lucha fue feroz, pero {character} emergió victorioso, restaurando la paz y la esperanza en el reino.",
        f"La batalla épica entre {character} y el mago oscuro marcó el culmen de una búsqueda que duró meses. Armado con su {weapon_name}, {character} lanzó una avalancha de hechizos y contrahechizos, creando un espectáculo de magia deslumbrante. El enfrentamiento culminó con {character} superando los desafíos mágicos y derrotando al mago oscuro, convirtiéndose en una leyenda y protegiendo el reino de la oscuridad.",
        f"Después de una larga y extenuante búsqueda que duró meses, {character} finalmente localizó al mago oscuro y se desató una batalla feroz en el abismo. Ambos magos lucharon con determinación y astucia, desplegando un torrente de hechizos. {character} empuñó su {weapon_name} con firmeza, parando los ataques del mago oscuro y contraatacando con valentía. La victoria de {character} restauró la paz en el reino, iluminando la oscuridad con la luz de la esperanza.",
        f"La confrontación entre {character} y el mago oscuro fue el resultado de semanas de búsqueda incansable. Los hechizos chisporroteaban en el aire mientras {character} y el mago oscuro se enfrentaban en un duelo de magia. Con su {weapon_name} en mano, {character} demostró valentía y destreza, desafiando los poderes del malvado mago. La victoria de {character} restauró la armonía en el mundo, y su nombre se convirtió en sinónimo de heroísmo y valentía.",
        f"{character} se preparó durante mucho tiempo para el enfrentamiento con el mago oscuro. Armado con su {weapon_name}, se lanzó a la batalla con determinación después de semanas de búsqueda incansable. Los hechizos volaban en todas direcciones mientras {character} y el mago oscuro se enfrentaban en un espectáculo asombroso de magia y habilidad. Con un ataque decisivo de su {weapon_name}, {character} emergió victorioso, poniendo fin a la amenaza del mago oscuro y convirtiéndose en un héroe legendario, reverenciado en todo el reino.",
        f"El duelo entre {character} y el mago oscuro fue el resultado de una búsqueda que duró meses. Fue un espectáculo asombroso de magia y habilidad, con hechizos y contrahechizos deslumbrantes. {character} empuñó su {weapon_name} con maestría, desafiando al mago oscuro en una lucha épica. Con un golpe certero y la última chispa de energía, {character} emergió como vencedor, poniendo fin a la amenaza del mago oscuro y convirtiéndose en un héroe legendario en el reino, cuya valentía sería recordada por generaciones.",
    ]
    return random.choice(phrases)

def templateVictory(character):
    phrases = [
        f"Con la derrota del mago tenebroso, {character} aseguró la seguridad de sus tierras natales. La amenaza había sido eliminada, y la paz finalmente regresó a su hogar.",
        f"Tras la victoria sobre el mago tenebroso, {character} garantizó la salvación de sus tierras natales. La oscuridad retrocedió y la luz retornó a su hogar.",
        f"La derrota del mago tenebroso por parte de {character} aseguró la seguridad de su pueblo y sus seres queridos. Las tierras natales están a salvo una vez más.",
        f"La valentía de {character} en la batalla contra el mago tenebroso inspiró a su pueblo. La victoria trajo esperanza y unidad a las tierras natales.",
        f"Después de vencer al mago tenebroso, {character} lideró la reconstrucción de las tierras natales, restaurando la prosperidad y la armonía que habían sido arrebatadas por la oscuridad.",
    ]
    return random.choice(phrases)

def templateTierrasNatales(character):
    phrases = [
        f"Con la derrota del mago tenebroso, {character} aseguró la seguridad de sus tierras natales. La amenaza había sido eliminada, y la paz finalmente regresó a su hogar.",
        f"Tras la victoria sobre el mago tenebroso, {character} garantizó la salvación de sus tierras natales. La oscuridad retrocedió y la luz retornó a su hogar.",
        f"La derrota del mago tenebroso por parte de {character} aseguró la seguridad de su pueblo y sus seres queridos. Las tierras natales están a salvo una vez más.",
        f"La valentía de {character} en la batalla contra el mago tenebroso inspiró a su pueblo. La victoria trajo esperanza y unidad a las tierras natales.",
        f"Después de vencer al mago tenebroso, {character} lideró la reconstrucción de las tierras natales, restaurando la prosperidad y la armonía que habían sido arrebatadas por la oscuridad.",
    ]
    return random.choice(phrases)

def templateBecomingALegend(character):
    phrases = [
        f"Tras la derrota del mago tenebroso, {character} se convirtió en una leyenda reconocida en todo el mundo por su valentía y habilidad mágica incomparable.",
        f"{character} se elevó al estatus de héroe internacional después de vencer al mago tenebroso. Sus hazañas mágicas lo convirtieron en un símbolo de esperanza para personas de todas partes.",
        f"Después de la derrota del mago tenebroso, {character} ganó la admiración de personas de todas las naciones. Se convirtió en un ícono mundial de valentía y poder mágico.",
        f"{character} se convirtió en una leyenda viviente después de su victoria sobre el mago tenebroso, y sus hazañas mágicas inspiraron a generaciones futuras de magos y aventureros.",
        f"La historia de {character} se convirtió en una leyenda que se contaba de generación en generación, inspirando a jóvenes magos a emular su valentía y destreza mágica.",
    ]
    return random.choice(phrases)

diccionarioTemplates = {
    "template Inicio Amenaza": templateInicioAmenaza,
    "template Tierras Natales Danger": templateTierrasNatalesDanger,
    "template Caminar":templateWalk,
    "template Magia Basica": templateBasicMagical,
    "template Tipo de Magia": templateMagicAffinity,
    "template Desafio Magico": templateMagicChallenge,
    "template Interactuar": templateCharacterMeeting,
    "template Codices": templateLibraryDiscovery,
    "template Busqueda Artefacto": templateForestDiscovery,
    "template Hablar Quetzalcotal": templateTempleEncounter,
    "template Magia Avanzada": templateForestMagicPower,
    "template Artefacto Encontrado": templateForestEncounter,
    "template Batalla Final": templateEpicBattle,
    "template Tierras Natales Safe": templateTierrasNatales,
    "template Reconocimiento Mundial": templateBecomingALegend
}