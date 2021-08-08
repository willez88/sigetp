# Nombre del Sitio
APP_NAME = 'SIGETP'

# Asunto del mensaje de bienvenida
EMAIL_SUBJECT = 'Bienvenido a %s' % APP_NAME

# Tipo de rif para consejos comunales y comunas
RIF_TYPE = (
    ('C', 'C'),
)

# Nacionalidades (ABREVIADO)
NATIONALITY = (
    ('V', 'V'), ('E', 'E')
)

# Tipo de la vivienda
TIPO_VIVIENDA = (
    ('CA', 'Casa'),
    ('AP', 'Apartamento'),
    ('QU', 'Quinta'),
    ('RA', 'Rancho'),
    ('HA', 'Habitación'),
)

# Tipo del Techo
TIPO_TECHO = (
    ('AC', 'Acerolit'),
    ('AS', 'Asbesto'),
    ('CT', 'Carruzo y Teja'),
    ('PB', 'Plata Banda'),
    ('TE', 'Teja'),
    ('TJ', 'Tejalic'),
    ('ZI', 'Zinc'),
    ('OT', 'Otros'),
)

# Tipo de la Pared
TIPO_PARED = (
    ('AD', 'Adobe'),
    ('BA', 'Bahareque'),
    ('BR', 'Barro'),
    ('BL', 'Bloque'),
    ('LA', 'Ladrillo'),
    ('PI', 'Piedra'),
    ('ZI', 'Zinc'),
    ('OT', 'Otros'),
)

# Tipo del Piso
TIPO_PISO = (
    ('TI', 'Tierra'),
    ('CE', 'Cemento'),
    ('GR', 'Granito'),
    ('CR', 'Cerámica'),
    ('BA', 'Baldosa'),
    ('MA', 'Madera'),
    ('TE', 'Terracota'),
    ('OT', 'Otros'),
)

# Valoracion
VALORACION = (
    ('B', 'Buena'),
    ('R', 'Regular'),
    ('M', 'Mala'),
)

# Tipo del Cemento
TIPO_CEMENTO = (
    ('RU', 'Rústico'),
    ('PU', 'Pulido'),
)

# Tipo del Servicio Eléctrico
SERVICIO_ELECTRICO = (
    ('DI', 'Directa'),
    ('CO', 'Compartida'),
    ('IL', 'Ilegal'),
    ('OT', 'Otros'),
)

# Tipo de la Situación Sanitaria
SITUACION_SANITARIA = (
    ('CL', 'Cloacas'),
    ('PS', 'Pozo Séptico'),
    ('CA', 'Campo Abierto'),
    ('LE', 'Letrina'),
)

# Tipo de la Disposición de la Basura
DISPOSICION_BASURA = (
    ('RD', 'Recolección Directa'),
    ('CO', 'Container'),
    ('QU', 'Quemada'),
    ('EN', 'Enterrada'),
)

# Tipo de Tenencia
TIPO_TENENCIA = (
    ('PR', 'Propia Pagada'),
    ('AL', 'Alquilada'),
    ('PO', 'Propia Pagando'),
    ('HE', 'Heredada'),
    ('CE', 'Cedida'),
    ('PE', 'Prestada'),
    ('EC', 'En Cuido'),
    ('DE', 'Desocupada'),
)

# Género
GENDER = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

# Parentesco
RELATIONSHIP = (
    # ('JF', 'Jefe Familiar'),
    # Parentesco de primer grado
    ('MA', 'Madre'),
    ('PA', 'Padre'),
    ('ES', 'Esposo(a)'),
    ('CN', 'Concubino(a)'),
    ('HI', 'Hijo(a)'),
    ('YE', 'Yerno(a)'),
    ('SU', 'Suegro(a)'),
    # Parentesto de segundo grado
    ('AB', 'Abuelo(a)'),
    ('NI', 'Nieto(a)'),
    ('HE', 'Hermano(a)'),
    ('CU', 'Cuñado(a)'),
    # Parentesco de tercer grado
    ('BI', 'Bisabuelo(a)'),
    ('BS', 'Bisnieto(a)'),
    ('TI', 'Tío(a)'),
    ('SO', 'Sobrino(a)'),
    # Parentesco de cuarto grado
    ('PR', 'Primo(a)'),
    ('TA', 'Tio(a) Abuelo(a)'),
)

# Estado Civil
ESTADO_CIVIL = (
    ('SO', 'Soltero(a)'),
    ('CA', 'Casado(a)'),
    ('CF', 'Concubino(a) Formal'),
    ('CI', 'Concubino(a) Informal'),
    ('DI', 'Divirciado(a)'),
    ('VI', 'Viudo(a)'),
)

# Grado de Instrucción
GRADO_INSTRUCCION = (
    ('NE', 'No Estudió'),
    ('LA', 'Lactante'),
    ('PR', 'Preescolar'),
    ('1G', 'Primer Grado'),
    ('2G', 'Segundo Grado'),
    ('3G', 'Tercer Grado'),
    ('4G', 'Cuarto Grado'),
    ('5G', 'Quinto Grado'),
    ('6G', 'Sexto Grado'),
    ('7G', 'Septimo Grado'),
    ('8G', 'Octavo Grado'),
    ('9G', 'Noveno Grado'),
    ('1A', 'Primer Año Diversificado'),
    ('2A', 'Segundo Año Diversificado'),
    ('BA', 'Bachiller'),
    ('TM', 'Técnico Medio'),
    ('TS', 'Técnico Superior Universitario'),
    ('UN', 'Universitario'),
)

# Misión Educativa
MISION_EDUCATIVA = (
    ('NI', 'Ninguna'),
    ('R1', 'Misión Robinson 1'),
    ('R2', 'Misión Robinson 2'),
    ('MR', 'Misión Rivas'),
    ('MS', 'Misión Sucre'),
    ('MA', 'Misión Alma Mater'),
    ('MC', 'Misión Ciencia'),
    ('PA', 'Misión Cultura Corazón Abierto'),
    ('MM', 'Misión Música'),
)

MISION_SOCIAL = (
    ('NI', 'Ninguna'),
    ('HP', 'Hogares de la Patria'),
    ('NH', 'Negra Hipólita'),
    ('JG', 'José Gregorio Hernández'),
    ('BA', 'Barrio Adentro Deportivo'),
    ('EA', 'En Amor Mayor'),
    ('NE', 'Nevado'),
    ('JP', 'Jóvenes de la Patria'),
    ('ID', 'Identidad'),
    ('GP', 'Guaicaipuro y Piar'),
    ('MB', 'Madres del Barrio'),
)

TIPO_INGRESO = (
    ('NI', 'Ninguno'),
    ('ME', 'Menos de un Sueldo Mínimo'),
    ('1S', '1 Sueldo Mínimo'),
    ('M1', 'Más de 1 sueldo Mínimo'),
    ('2S', '2 Sueldos Mínimos'),
    ('M2', 'Más de 2 Sueldos Mínimos'),
)

ORGANIZACION_COMUNITARIA = (
    ('CD', 'Comité Deportivo'),
    ('CS', 'Comité de Salud'),
    ('MS', 'Mesa Técnica de Seguridad'),
    ('ME', 'Mesa Técnica de Energía'),
    ('MT', 'Mesa Técnica de Tierras'),
    ('CC', 'Consejo Comunal'),
)

PHONE_PREFIX = (
    ('+58', 'VE +58'),
)

# Mensaje de error para peticiones AJAX
MSG_NOT_AJAX = 'No se puede procesar la petición. Verifique que posea las \
    opciones javascript habilitadas e intente nuevamente.'
