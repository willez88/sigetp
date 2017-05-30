"""
Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica (SIGETP)

Copyleft (@) 2017 CENDITEL nodo Mérida
"""
## @namespace base.constant
#
# Contiene las constantes de usos generales
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>

from django.utils.translation import ugettext_lazy as _

## Nacionalidades (ABREVIADO)
SHORT_NACIONALIDAD = (
    ("V", "V"), ("E", "E")
)

## Tipo de la vivienda
TIPO_VIVIENDA = (
    ("CA",_("Casa")),
    ("AP",_("Apartamento")),
    ("QU",_("Quinta")),
    ("RA",_("Rancho")),
    ("HA",_("Habitación")),
)

## Tipo del Techo
TIPO_TECHO = (
    ("AC",_("Acerolit")),
    ("AS",_("Asbesto")),
    ("CT",_("Carruzo y Teja")),
    ("PB",_("Plata Banda")),
    ("TE",_("Teja")),
    ("TJ",_("Tejalic")),
    ("ZI",_("Zinc")),
    ("OT",_("Otros")),
)

## Tipo de la Pared
TIPO_PARED = (
    ("AD",_("Adobe")),
    ("BA",_("Bahareque")),
    ("BR",_("Barro")),
    ("BL",_("Bloque")),
    ("LA",_("Ladrillo")),
    ("PI",_("Piedra")),
    ("ZI",_("Zinc")),
    ("OT",_("Otros")),
)

## Tipo del Piso
TIPO_PISO = (
    ("TI",_("Tierra")),
    ("CE",_("Cemento")),
    ("GR",_("Granito")),
    ("CR",_("Cerámica")),
    ("BA",_("Baldosa")),
    ("MA",_("Madera")),
    ("TE",_("Terracota")),
    ("OT",_("Otors")),
)

## Valoracion
VALORACION = (
    ("B",_("Buena")),
    ("R",_("Regular")),
    ("M",_("Mala")),
)

# Tipo del Cemento
TIPO_CEMENTO = (
    ("RO",_("Robusto")),
    ("PU",_("Pulido")),
)

## Tipo del Servicio Eléctrico
SERVICIO_ELECTRICO = (
    ("DI",_("Directa")),
    ("CO",_("Compartida")),
    ("IL",_("Ilegal")),
    ("OT",_("Otros")),
)

## Tipo de la Situación Sanitaria
SITUACION_SANITARIA = (
    ("CL",_("Cloacas")),
    ("PS",_("Pozo Séptico")),
    ("CA",_("Campo Abierto")),
    ("LE",_("Letrina")),
)

## Tipo de la Disposición de la Basura
DISPOSICION_BASURA = (
    ("RD",_("Recolección Directa")),
    ("CO",_("Container")),
    ("QU",_("Quemada")),
    ("EN",_("Enterrada")),
)

## Tipos de Animales
ANIMALES = (
    (1,_("Gatos")),
    (2,_("Perros")),
    (3,_("Vacas")),
    (4,_("Cochinos")),
    (5,_("Caballos")),
    (6,_("Gallinas")),
    (7,_("Serpientes")),
    (8,_("Hamster")),
    (10,_("Conejos")),
    (11,_("Peces")),
    (12,_("Ratones")),
    (13,_("Iguanas")),
    (14,_("Obejas")),
    (15,_("Loros")),
    (16,_("Guacamayas")),
    (17,_("Chivos")),
    (18,_("Arañas")),
)

## Tipo de Tenencia
TIPO_TENENCIA = (
    ("PR",_("Propia")),
    ("AL",_("Alquilada")),
    ("PA",_("Pagada")),
    ("HE",_("Heredada")),
    ("CE",_("Cedida")),
)

## Sexo
SEXO = (
    ("M",_("Masculino")),
    ("F",_("Femenino")),
)

## Tipo del Parentesco
PARENTESCO = (
    ("JF",_("Jefe Familiar")),
    ## Parentesco de primer grado
    ("MA",_("Madre")),
    ("PA",_("Padre")),
    ("CO",_("cónyuge")),
    ("CN",_("Concubino(a)")),
    ("HI",_("Hijo(a)")),
    ("YE",_("Yerno(a)")),
    ("SU",_("Suegro(a)")),
    ## Parentesto de segundo grado
    ("AB",_("Abuelo(a)")),
    ("NI",_("Nieto(a)")),
    ("HE",_("Hermano(a)")),
    ("CU",_("Cuñado(a)")),
    ## Parentesco de tercer grado
    ("BI",_("Bisabuelo(a)")),
    ("BS",_("Bisnieto(a)")),
    ("TI",_("Tío(a)")),
    ("SO",_("Sobrino(a)")),
    ## Parentesco de cuarto grado
    ("PR",_("Primo(a)")),
    ("TA",_("Tio(a) Abuelo(a)")),
    ## Otro
    ("AD",_("Adoptado(a)")),
)

## Estado Civil
ESTADO_CIVIL = (
    ("SO",_("Soltero(a)")),
    ("CA",_("Casado(a)")),
    ("CO",_("Concubino(a)")),
    ("DI",_("Divirciado(a)")),
    ("VI",_("Viudo(a)")),
)

## Grado de Instrucción
GRADO_INSTRUCCION = (
    ("LA",_("Lactante")),
    ("PR",_("Preescolar")),
    ("1G",_("Primer Grado")),
    ("2G",_("Segundo Grado")),
    ("3G",_("Tercer Grado")),
    ("4G",_("Cuarto Grado")),
    ("5G",_("Quinto Grado")),
    ("6G",_("Sexto Grado")),
    ("7G",_("Septimo Grado")),
    ("8G",_("Octavo Grado")),
    ("9G",_("Noveno Grado")),
    ("1A",_("Primer Año Diversificado")),
    ("2A",_("Segundo Año Diversificado")),
    ("BA",_("Bachiller")),
    ("TM",_("Técnico Medio")),
    ("TS",_("Técnico Superior Universitario")),
    ("UN",_("Universitario")),
)

## Misión Educativa
MISION_EDUCATIVA = (
    ("NI",_("Ninguna")),
    ("R1",_("Misión Robinson 1")),
    ("R2",_("Misión Robinson 2")),
    ("MR",_("Misión Rivas")),
    ("MS",_("Misión Sucre")),
    ("MA",_("Misión Alma Mater")),
    ("MC",_("Misión Ciencia")),
    ("PA",_("Misión Cultura Corazón Abierto")),
    ("MM",_("Misión Música")),
)

TIPO_INGRESO = (
    ("NI",_("Ninguno")),
    ("ME",_("Menos de un Sueldo Mínimo")),
    ("1S",_("1 Sueldo Mínimo")),
    ("M1",_("Más de 1 sueldo Mínimo")),
    ("2S",_("2 Sueldos Mínimos")),
    ("M2",_("Más de 2 Sueldos Mínimos")),
)

ORGANIZACION_COMUNITARIA = (
    ("CD",_("Comité Deportivo")),
    ("CS",_("Comité de Salud")),
    ("MS",_("Mesa Técnica de Seguridad")),
    ("ME",_("Mesa Técnica de Energía")),
    ("MT",_("Mesa Técnica de Tierras")),
    ("CC",_("Consejo Comunal")),
)

## Mensaje de error para peticiones AJAX
MSG_NOT_AJAX = _("No se puede procesar la petición. "
                 "Verifique que posea las opciones javascript habilitadas e intente nuevamente.")
