import random # Generación de valores aleatorios
import datetime # Manejo de fechas y horas
import unicodedata # Normalización y eliminación de acentos en texto

# ESTADO
estados_mexico = {"clave": "02", "nombre": "BAJA CALIFORNIA", "abreviacion": "B.C."}

# MUNICIPIOS DE BAJA CALIFORNIA
municipios_baja_california = {"001": "ENSENADA", "002": "MEXICALI", "003": "TECATE", "004": "TIJUANA", "005": "PLAYAS DE ROSARITO", "006": "SAN QUINTIN", "007": "SAN FELIPE"}

# SEXOS
sexos = {"M": "MUJER", "H": "HOMBRE"}

# NOMBRES VINCULADOS POR SEXO
nombres = {
    "MUJER": [
      "ABIGAIL", "ADRIANA", "AIDA", "ALEJANDRA", "ALEXA", "ALEXANDRA", "ALICIA", "ALMA", "AMANDA", "AMELIA", "ANA", "ANDREA", "ANGELA", "ANGELICA", "ANTONIA", "ARIADNA", "BEATRIZ", "BELEN", "BERENICE", "BRENDA", "BRIANNA", "BRISEIDA", "CAMILA", "CARLA", "CARMEN", "CAROLINA", "CECILIA", "CELIA", "CLARA", "CLAUDIA", "CRISTINA", "DANIELA", "DIANA", "DOLORES", "ELENA", "ELISA", "ELIZABETH", "EMILIA", "EMMA", "ERIKA", "ESMERALDA", "ESTEFANIA", "EUGENIA", "FABIOLA", "FERNANDA", "FLORENCIA", "FRANCISCA", "GABRIELA", "GEMA", "GISELA", "GLORIA", "GUADALUPE", "HELENA", "ILSE", "INES", "IRENE", "IRMA", "ISABEL", "JACQUELINE", "JAZMIN", "JESSICA", "JOANA", "JOSEFINA", "JUANA", "JULIA", "JULIANA", "KAREN", "KARINA", "KARLA", "LAURA", "LETICIA", "LILIANA", "LIZBETH", "LORENA", "LUCIA", "LUISA", "MAGDALENA", "MARCELA", "MARGARITA", "MARIA", "MARIANA", "MARIBEL", "MARICELA", "MARINA", "MARTA", "MARTINA", "MAYRA", "MELANIE", "MELISSA", "MICAELA", "MICHELLE", "MIRIAM", "MONICA", "NANCY", "NATALIA", "NATALY", "NAYELI", "NORMA", "OLGA", "PATRICIA", "PAOLA", "PAULA", "PILAR", "RAQUEL", "REBECA", "REGINA", "RENATA", "RITA", "ROSA", "ROSALBA", "ROSARIO", "RUBI", "SANDRA", "SARA", "SILVIA", "SOFIA", "SONIA", "TATIANA", "TERESA", "VALENTINA", "VALERIA", "VERONICA", "VIRIDIANA", "VIRGINIA", "XIMENA", "YADIRA", "YESENIA", "YOLANDA", "ZOE"
    ],
    "HOMBRE": [
      "ADAN", "ADRIAN", "AGUSTIN", "ALBERTO", "ALEJANDRO", "ALEX", "ALFONSO", "ALFREDO", "ANDRES", "ANGEL", "ANTONIO", "ARIEL", "ARTURO", "AUGUSTO", "BENJAMIN", "BERNARDO", "BRUNO", "CARLOS", "CESAR", "CHRISTIAN", "CRISTOBAL", "DANIEL", "DARIO", "DAVID", "DIEGO", "EDGAR", "EDUARDO", "EFRAIN", "ELIAS", "EMILIANO", "EMMANUEL", "ENRIQUE", "ERNESTO", "ESTEBAN", "EUGENIO", "FABIAN", "FELIPE", "FERNANDO", "FRANCISCO", "GABRIEL", "GERARDO", "GILBERTO", "GONZALO", "GREGORIO", "GUILLERMO", "GUSTAVO", "HECTOR", "HERIBERTO", "HUGO", "IGNACIO", "ISAAC", "ISAIAS", "ISMAEL", "IVAN", "JAIME", "JAVIER", "JESUS", "JOAQUIN", "JORGE", "JOSE", "LEONARDO", "LEOPOLDO", "LUIS", "MANUEL", "MARCO", "MARCOS", "MARIO", "MARTIN", "MATIAS", "MAURICIO", "MAXIMILIANO", "MIGUEL", "MOISES", "NESTOR", "NICOLAS", "NOE", "NORBERTO", "OCTAVIO", "OSCAR", "PABLO", "PASCUAL", "PATRICIO", "PEDRO", "RAFAEL", "RAMON", "RAUL", "RENE", "RICARDO", "ROBERTO", "RODRIGO", "RUBEN", "SALVADOR", "SAMUEL", "SANTIAGO", "SAUL", "SEBASTIAN", "SERGIO", "SIMON", "TEODORO", "TOMAS", "ULISES", "VALENTIN", "VICTOR", "VICENTE", "XAVIER", "YONATHAN"
    ]
}

# APELLIDOS
apellidos = ["ACOSTA", "AGUILAR", "ALANIZ", "ALCANTAR", "ALFARO", "ALONSO", "ALVARADO", "AMADOR", "ANGULO", "ARANDA", "ARELLANO", "ARIAS", "AVALOS", "AVILA", "AYALA", "BAEZ", "BAÑUELOS", "BARAJAS", "BARRAZA", "BARRERA", "BAUTISTA", "BELTRAN", "BENITEZ", "BERNAL", "BLANCO", "BOJORQUEZ", "BORREGO", "BRAVO", "BUSTAMANTE", "CABRERA", "CALDERON", "CAMACHO", "CAMPOS", "CANALES", "CARDENAS", "CARDONA", "CARRANZA", "CARRILLO", "CASTAÑEDA", "CASTILLO", "CASTRO", "CEJA", "CERVANTES", "CHAVEZ", "CISNEROS", "CONTRERAS", "CORONADO", "CORRAL", "CORTES", "CRUZ", "CUELLAR", "DE LA CRUZ", "DE LEON", "DELGADO", "DIAZ", "DOMINGUEZ", "DUARTE", "DURAN", "ESCOBAR", "ESPINOZA", "ESTRADA", "FELIX", "FERNANDEZ", "FIGUEROA", "FLORES", "FONSECA", "FRANCO", "GALINDO", "GALLEGOS", "GARCIA", "GARIBAY", "GARZA", "GASTELUM", "GOMEZ", "GONZALEZ", "GUTIERREZ", "GUZMAN", "HERNANDEZ", "HERRERA", "IBARRA", "JIMENEZ", "JUAREZ", "LARA", "LEAL", "LEYVA", "LOPEZ", "LUCERO", "LUNA", "MACIAS", "MALDONADO", "MARQUEZ", "MARTINEZ", "MEDINA", "MEJIA", "MENDOZA", "MENA", "MERCADO", "MIRANDA", "MOLINA", "MONDRAGON", "MONROY", "MONTES", "MORA", "MORALES", "MORENO", "MORONES", "MOTA", "MUNOZ", "NAVARRO", "NEGRETE", "NIEVES", "NIETO", "NUNEZ", "OCHOA", "OLIVAS", "OROZCO", "ORTEGA", "ORTIZ", "OSORIO", "PACHECO", "PADILLA", "PALACIOS", "PARRA", "PARRILLA", "PATIÑO", "PEÑA", "PEREZ", "PONCE", "PORTILLO", "PRIETO", "RAMIREZ", "RAMOS", "RANGEL", "REYES", "RIVAS", "RIVERA", "ROBLES", "RODRIGUEZ", "ROJAS", "ROMAN", "ROMERO", "ROSAS", "RUIZ", "SALAS", "SALAZAR", "SALCEDO", "SANCHEZ", "SANDOVAL", "SANTIAGO", "SANTOS", "SEPULVEDA", "SERRANO", "SILVA", "SOLIS", "SOTO", "TAPIA", "TOVAR", "TORRES", "TREJO", "VALDEZ", "VALENCIA", "VALENZUELA", "VARGAS", "VAZQUEZ", "VEGA", "VELASCO", "VELAZQUEZ", "VERDUGO", "VILLA", "VILLALOBOS", "VILLANUEVA", "ZAMORA", "ZAVALA", "ZEPEDA"]

# TIPOS DE VIALIDAD
tipos_vialidad = ["CALLE", "AVENIDA", "BOULEVARD", "CALZADA", "PRIVADA", "PASEO", "CAMINO", "CARRETERA", "ANDADOR", "CERRADA", "CIRCUITO", "PROLONGACION", "RETORNO", "DIAGONAL"]

# NOMBRES DE VIALIDADES
nombres_vialidades = ["REVOLUCION", "CONSTITUCION", "INDEPENDENCIA", "JUAREZ", "HIDALGO", "MORELOS", "CUAUHTEMOC", "LAZARO CARDENAS", "BENITO JUAREZ", "MEXICO", "SONORA", "BAJA CALIFORNIA", "PRIMERA", "SEGUNDA", "TERCERA", "CUARTA", "QUINTA", "SEXTA", "SEPTIMA", "OCTAVA", "NOVENA", "AGUA CALIENTE", "INSURGENTES", "LAS FERIAS", "DE LAS AMERICAS", "TECNOLOGICO", "UNIVERSIDAD", "OTAY", "GARITA DE OTAY", "LIBERTAD", "PASEO DE LOS HEROES", "PASEO DEL CENTENARIO", "FUNDADORES", "PADRE KINO", "ANAHUAC", "RIO NUEVO", "VENUSTIANO CARRANZA", "MISION DE SAN DIEGO"]

# ABREVIACIONES DE COLONIAS
abreviaciones_colonia = {"RESIDENCIAL": "RDCIAL", "FRACCIONAMIENTO": "FRACC", "COLONIA": "COL", "UNIDAD HABITACIONAL": "U HAB", "AMPLIACION": "AMPL", "RANCHO": "RCHO", "EJIDO": "EJ"}

# DOMICILIOS DE BAJA CALIFORNIA
domicilios_baja_california = [
    {
        "municipio": "ENSENADA", "localidades":
      [
            {
                "clave": "001",
                "nombre": "ENSENADA",
                "colonias": [
                    {"nombre": "ZONA CENTRO", "codigo_postal": "22800"},
                    {"nombre": "PLAYA ENSENADA", "codigo_postal": "22880"},
                    {"nombre": "EX EJIDO CHAPULTEPEC", "codigo_postal": "22785"},
                    {"nombre": "VALLE DORADO", "codigo_postal": "22785"}
                ]
            },
            {
                "clave": "002",
                "nombre": "MANEADERO",
                "colonias": [
                    {"nombre": "MANEADERO", "codigo_postal": "22790"},
                    {"nombre": "LOMA LINDA", "codigo_postal": "22790"}
                ]
            },
            {
                "clave": "003",
                "nombre": "EL SAUZAL",
                "colonias": [
                    {"nombre": "EL SAUZAL", "codigo_postal": "22760"},
                    {"nombre": "PUERTO SALINA", "codigo_postal": "22760"}
                ]
            }
        ]
    },
    {
        "municipio": "MEXICALI", "localidades":
      [
            {
                "clave": "001",
                "nombre": "MEXICALI",
                "colonias": [
                    {"nombre": "ZONA CENTRO", "codigo_postal": "21100"},
                    {"nombre": "NUEVA", "codigo_postal": "21100"},
                    {"nombre": "INDUSTRIAL", "codigo_postal": "21010"}
                ]
            },
            {
                "clave": "002",
                "nombre": "GONZALEZ ORTEGA",
                "colonias": [
                    {"nombre": "GONZALEZ ORTEGA", "codigo_postal": "21397"},
                    {"nombre": "EJIDO PUEBLA", "codigo_postal": "21620"}
                ]
            }
        ]
    },
    {
        "municipio": "TECATE", "localidades":
      [
            {
                "clave": "001",
                "nombre": "TECATE",
                "colonias": [
                    {"nombre": "ZONA CENTRO", "codigo_postal": "21400"},
                    {"nombre": "INDUSTRIAL", "codigo_postal": "21430"},
                    {"nombre": "EL DESCANSO", "codigo_postal": "21440"},
                    {"nombre": "BENITO JUAREZ", "codigo_postal": "21470"},
                    {"nombre": "CUAUHTEMOC", "codigo_postal": "21440"},
                    {"nombre": "MORELOS", "codigo_postal": "21460"},
                    {"nombre": "FUNDADORES", "codigo_postal": "21453"},
                    {"nombre": "LAS HUERTAS", "codigo_postal": "21453"}
                ]
            },
            {
                "clave": "002",
                "nombre": "LA RUMOROSA",
                "colonias": [
                    {"nombre": "LA RUMOROSA", "codigo_postal": "21510"}
                ]
            }
        ]
    },
    {
        "municipio": "TIJUANA", "localidades":
      [
            {
                "clave": "001",
                "nombre": "TIJUANA",
                "colonias": [
                    {"nombre": "ZONA RIO", "codigo_postal": "22010"},
                    {"nombre": "ZONA CENTRO", "codigo_postal": "22000"},
                    {"nombre": "LIBERTAD", "codigo_postal": "22400"},
                    {"nombre": "MESA DE OTAY", "codigo_postal": "22450"},
                    {"nombre": "OTAY UNIVERSIDAD", "codigo_postal": "22427"},
                    {"nombre": "BUENA VISTA", "codigo_postal": "22415"},
                    {"nombre": "MORELOS", "codigo_postal": "22115"},
                    {"nombre": "CONSTITUCION", "codigo_postal": "22150"},
                    {"nombre": "INDEPENDENCIA", "codigo_postal": "22055"},
                    {"nombre": "FRANCISCO VILLA", "codigo_postal": "22205"},
                    {"nombre": "ALTAMIRA", "codigo_postal": "22000"},
                    {"nombre": "SOLER", "codigo_postal": "22105"},
                    {"nombre": "CACHO", "codigo_postal": "22040"},
                    {"nombre": "CHAPULTEPEC", "codigo_postal": "22020"},
                    {"nombre": "HIPODROMO", "codigo_postal": "22020"},
                    {"nombre": "AGUA CALIENTE", "codigo_postal": "22024"},
                    {"nombre": "20 DE NOVIEMBRE", "codigo_postal": "22100"},
                    {"nombre": "PLAYAS DE TIJUANA", "codigo_postal": "22200"},
                    {"nombre": "SANTA FE", "codigo_postal": "22664"}
                ]
            }
        ]
    },
    {
        "municipio": "PLAYAS DE ROSARITO", "localidades":
      [
            {
                "clave": "001",
                "nombre": "PLAYAS DE ROSARITO",
                "colonias": [
                    {"nombre": "CENTRO", "codigo_postal": "22700"},
                    {"nombre": "ZONA CENTRO", "codigo_postal": "22700"},
                    {"nombre": "EJIDO MAZATLAN", "codigo_postal": "22710"},
                    {"nombre": "PLAN LIBERTADOR", "codigo_postal": "22706"}
                ]
            },
            {
                "clave": "002",
                "nombre": "PRIMO TAPIA",
                "colonias": [
                    {"nombre": "PRIMO TAPIA", "codigo_postal": "22740"},
                    {"nombre": "VENUSTIANO CARRANZA", "codigo_postal": "22740"}
                ]
            }
        ]
    },
    {
        "municipio": "SAN QUINTIN", "localidades":
      [
            {
                "clave": "001",
                "nombre": "SAN QUINTIN",
                "colonias": [
                    {"nombre": "SAN QUINTIN", "codigo_postal": "22940"},
                    {"nombre": "NUEVA ERA", "codigo_postal": "22940"},
                    {"nombre": "LAS FLORES", "codigo_postal": "22940"}
                ]
            },
            {
                "clave": "002",
                "nombre": "VICENTE GUERRERO",
                "colonias": [
                    {"nombre": "VICENTE GUERRERO", "codigo_postal": "22920"},
                    {"nombre": "EJIDO NUEVO BAJA CALIFORNIA", "codigo_postal": "22930"}
                ]
            },
            {
                "clave": "003",
                "nombre": "CAMALU",
                "colonias": [
                    {"nombre": "CAMALU", "codigo_postal": "22910"}
                ]
            }
        ]
    },
    {
        "municipio": "SAN FELIPE", "localidades":
      [
            {
                "clave": "001",
                "nombre": "SAN FELIPE",
                "colonias": [
                    {"nombre": "CENTRO", "codigo_postal": "21850"},
                    {"nombre": "LOS ARCOS", "codigo_postal": "21850"},
                    {"nombre": "PORTUARIO", "codigo_postal": "21850"},
                    {"nombre": "SEGUNDA SECCION", "codigo_postal": "21850"}
                ]
            },
            {
                "clave": "002",
                "nombre": "PUERTECITOS",
                "colonias": [
                    {"nombre": "PUERTECITOS", "codigo_postal": "21870"}
                ]
            }
        ]
    }
]

# SECCIONES
# Se generan todas las secciones de 0000 a 2999.
secciones_prueba = [f"{numero:04d}" for numero in range(3000)]

# TIPOS DE VIVIENDA
tipos_vivienda = ["CASA", "DEPARTAMENTO", "CONDOMINIO", "DUPLEX", "TRIPLEX"]

# TIPOS DE DOMICILIO
tipos_domicilio = ["PARTICULAR", "LABORAL", "TEMPORAL", "FAMILIAR"]

# FUNCIONES
# Elimina acentos y convierte el texto a mayúsculas
def limpiar_texto(texto):
    texto_normalizado = unicodedata.normalize("NFD", texto)
  
    return "".join(caracter for caracter in texto_normalizado if unicodedata.category(caracter) != "Mn").upper()

# Obtiene la primera vocal interna de una palabra
def obtener_vocal_interna(texto):
    for caracter in limpiar_texto(texto)[1:]:
        if caracter in "AEIOU":
            return caracter

    return "X"

# Obtiene la primera consonante interna de una palabra
def obtener_consonante_interna(texto):
    for caracter in limpiar_texto(texto)[1:]:
        if caracter in "BCDFGHJKLMNPQRSTVWXYZ":
            return caracter

    return "X"

# Genera una fecha de nacimiento aleatoria entre 18 y 90 años
def generar_fecha_nacimiento():
    fecha_actual = datetime.date.today()

    fecha_maxima = fecha_actual.replace(year=fecha_actual.year - 18)

    try:
        fecha_minima = fecha_actual.replace(year=fecha_actual.year - 90)
    except ValueError:
        fecha_minima = fecha_actual.replace(year=fecha_actual.year - 90, day=28)

    dias_diferencia = (fecha_maxima - fecha_minima).days

    return fecha_minima + datetime.timedelta(days=random.randint(0, dias_diferencia))

# Selecciona aleatoriamente un municipio y sus localidades
def seleccionar_municipio():
    municipio_clave = random.choice(list(municipios_baja_california.keys()))

    municipio_nombre = municipios_baja_california[municipio_clave]

    for municipio_iter in domicilios_baja_california:
        if municipio_iter["municipio"] == municipio_nombre:
            return municipio_clave, municipio_iter

    return municipio_clave, None

# Selecciona una localidad y colonia relacionadas
def seleccionar_domicilio(municipio):
    localidad = random.choice(municipio["localidades"])
    colonia = random.choice(localidad["colonias"])

    return localidad, colonia

# Genera abreviación de una colonia
def abreviar_colonia(nombre):
    partes = nombre.split()

    resultado = []

    for parte in partes:
        resultado.append(abreviaciones_colonia.get(parte, parte))

    return " ".join(resultado)

# Genera un domicilio siguiendo el orden solicitado
def generar_domicilio(localidad, colonia, municipio):
    tipo_vialidad = random.choice(tipos_vialidad)
    nombre_vialidad = random.choice(nombres_vialidades)

    numero_exterior = random.randint(1, 99999)

    # El exterior puede ser numérico o alfanumérico
    if random.choice([True, False]):
        exterior = str(numero_exterior)
    else:
        exterior = random.choice(["A", "B", "C", "D", "T", "R", "M"]) + str(random.randint(1, 999))

    # Interior opcional
    interior = random.choice(["", str(random.randint(1, 999)), random.choice(["A", "B", "C", "T", "R"]) + str(random.randint(1, 999))])

    domicilio = (tipo_vialidad + " " + nombre_vialidad)

    # Interior antes del exterior cuando existe
    if interior:
        domicilio += " " + interior

    domicilio += " " + exterior

    # Colonia
    colonia_nombre = abreviar_colonia(colonia["nombre"])

    domicilio += (" " + colonia_nombre + " " + colonia["codigo_postal"] + " " + municipio + ", " + estados_mexico["abreviacion"])

    return domicilio

# Genera año y mes de registro entre los 18 y 20 años
def generar_registro(fecha_nacimiento):
    fecha_actual = datetime.date.today()

    fecha_18 = fecha_nacimiento.replace(year=fecha_nacimiento.year + 18)

    fecha_20 = fecha_nacimiento.replace(year=fecha_nacimiento.year + 20)

    fecha_inicio = fecha_18
  
    fecha_fin = min(fecha_20, fecha_actual)

    if fecha_inicio > fecha_fin:
        fecha_inicio = fecha_actual

    diferencia_dias = (fecha_fin - fecha_inicio).days

    fecha_registro = (fecha_inicio + datetime.timedelta(days=random.randint(0, diferencia_dias)))

    return fecha_registro.strftime("%Y %m")

# Genera emisión
def generar_emision():
    fecha_actual = datetime.date.today()

    return fecha_actual.year - random.randint(0, 3)

# Genera vigencia como rango
def generar_vigencia(anio_emision):
    return f"{anio_emision}-{anio_emision + 10}"

# Genera una clave de elector
def generar_clave_elector(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo):
    paterno = limpiar_texto(apellido_paterno)
    materno = limpiar_texto(apellido_materno)
    nombres_limpios = limpiar_texto(nombre)

    # Primeras letras de los apellidos y nombre
    letras = (paterno[:2] + materno[:2] + nombres_limpios[:2])

    # Fecha de nacimiento
    fecha = fecha_nacimiento.strftime("%y%m%d")

    # Identificador aleatorio
    aleatorio = f"{random.randint(0, 99999999):08d}"

    # Prefijo que indica que es un dato sintético
    return letras + fecha + sexo + aleatorio

# Genera una CURP
def generar_curp(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo):
    paterno = limpiar_texto(apellido_paterno)
    materno = limpiar_texto(apellido_materno)
    nombres_limpios = limpiar_texto(nombre)

    letra1 = paterno[0]
    letra2 = obtener_vocal_interna(paterno)
    letra3 = materno[0]
    letra4 = nombres_limpios[0]

    fecha = fecha_nacimiento.strftime("%y%m%d")

    estado = "BC"

    consonante_paterno = obtener_consonante_interna(paterno)
    consonante_materno = obtener_consonante_interna(materno)
    consonante_nombre = obtener_consonante_interna(nombres_limpios)

    texto_digitos = paterno + materno + nombres_limpios + fecha + sexo + estado

    suma_digitos = sum(ord(caracter) for caracter in texto_digitos)

    digitos_sinteticos = f"{suma_digitos % 100:02d}"

    curp = (letra1 + letra2 + letra3 + letra4 + fecha + sexo + estado + consonante_paterno + consonante_materno + consonante_nombre + digitos_sinteticos)

    return curp

# Genera identificador sintético claramente ficticio
def generar_id(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo):
    paterno = limpiar_texto(apellido_paterno)
    materno = limpiar_texto(apellido_materno)
    nombres_limpios = limpiar_texto(nombre)

    letras = (paterno[:2] + materno[:2] + nombres_limpios[:2])

    fecha = fecha_nacimiento.strftime("%y%m%d")

    aleatorio = f"{random.randint(0, 99999999):08d}"

    return (letras + fecha + sexo + aleatorio)

# Genera perfil sintético
def generar_perfil():
    sexo = random.choice(list(sexos.keys()))

    sexo_nombre = sexos[sexo]

    # Uno o dos nombres
    cantidad_nombres = random.choice([1, 2])

    nombres_seleccionados = random.sample(nombres[sexo_nombre], cantidad_nombres)

    nombre = " ".join(nombres_seleccionados)

    # Dos apellidos diferentes
    apellido_paterno = random.choice(apellidos)

    apellido_materno = random.choice(apellidos)

    while apellido_materno == apellido_paterno:
        apellido_materno = random.choice(apellidos)

    # Fecha de nacimiento
    fecha_nacimiento = generar_fecha_nacimiento()

    # Municipio
    municipio_clave, municipio = seleccionar_municipio()

    # Localidad y colonia
    localidad, colonia = seleccionar_domicilio(municipio)

    # Domicilio
    domicilio = generar_domicilio(localidad, colonia, municipio["municipio"])

    # Nombre en orden: APELLIDO PATERNO + APELLIDO MATERNO + NOMBRES
    nombre_completo = (apellido_paterno + " " + apellido_materno + " " + nombre)

    # Identificadores
    clave_elector = generar_clave_elector(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo)

    curp_sintetica = generar_curp(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo)

    # Registro
    registro = generar_registro(fecha_nacimiento)

    # Emisión y vigencia
    anio_emision = generar_emision()
    vigencia = generar_vigencia(anio_emision)

    # Sección de exactamente 4 dígitos
    seccion = random.choice(secciones_prueba)

    # Localidad de exactamente 4 dígitos
    localidad_codigo = localidad["clave"].zfill(4)

    return {"NOMBRE": nombre_completo, "FECHA DE NACIMIENTO": fecha_nacimiento.strftime("%d/%m/%Y"), "SEXO": sexo, "DOMICILIO": domicilio, "CLAVE DE ELECTOR": clave_elector, "CURP": curp_sintetica, "AÑO DE REGISTRO": registro, "ESTADO": estados_mexico["nombre"], "MUNICIPIO": municipio["municipio"], "SECCIÓN": seccion, "LOCALIDAD": localidad_codigo, "EMISIÓN": anio_emision, "VIGENCIA": vigencia}

# Muestra todos los datos en una misma línea
def mostrar_perfil(perfil):
    print("\n".join(f"{campo}: {valor}" for campo, valor in perfil.items()))

# Genera y muestra un perfil sintético
perfil = generar_perfil()
mostrar_perfil(perfil)