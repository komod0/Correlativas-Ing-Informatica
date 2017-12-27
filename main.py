import csv
import sys

AGREGAR_MATERIA = "agregar_materia"
MATERIAS_CURSABLES = "que_curso"
QUITAR_MATERIA = "quitar_materia"
MATERIAS_INICIALES = "CBC"


class Materia:
    def __init__(self, codigo, nombre, carga_horaria, correlativas):
        self.nombre = nombre
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.correlativas = correlativas

    def __str__(self):
        return self.nombre

    def es_cursable(self, materias_aprobadas):
        return all(materia in materias_aprobadas for materia in self.correlativas)

    def cargahoraria(self):
        return self.carga_horaria

    def codigo_materia(self):
        return self.codigo


def cargar_materias_de_archivo(nombre_archivo):
    materias = []
    with open(nombre_archivo) as listado:
        lector = csv.reader(listado)
        for linea in lector:
            mat_actual = Materia(linea[0], linea[1], linea[2], linea[4].split("-"))
            materias.append(mat_actual)
    return materias


def materias_cursables(materias, materias_aprobadas):
    for materia in materias:
        if materia.codigo_materia() not in materias_aprobadas and materia.es_cursable(materias_aprobadas):
            print("{} - {} - {}".format(materia.codigo_materia(), materia, materia.cargahoraria()))


def chequear_si_existe(materia, listado_materias):
    for mat in listado_materias:
        if mat.codigo_materia() == materia:
            return True
    return False


def procesar_input(linea, materias, materias_aprobadas):
    if linea[0] == AGREGAR_MATERIA:
        if chequear_si_existe(linea[1], materias):
            if linea[1] in materias_aprobadas:
                print("La materia ya ha sido agregada")
            else:
                materias_aprobadas.append(linea[1])
        else:
            print("La materia no ha sido encontrada")
    elif linea[0] == MATERIAS_CURSABLES:
        materias_cursables(materias, materias_aprobadas)
    elif linea[0] == QUITAR_MATERIA:
        if linea[1] in materias_aprobadas:
            quitar_materia(linea[1], materias_aprobadas)
        else:
            print("La materia no se encuentra aprobada")
    else:
        print("Comando no encontrado")


def quitar_materia(materia, materias_aprobadas):
    materias_aprobadas.remove(materia)


def main():
    materias = cargar_materias_de_archivo(sys.argv[1])
    materias_aprobadas = [MATERIAS_INICIALES]
    for ingreso in sys.stdin:
        linea = ingreso.rstrip().split()
        procesar_input(linea, materias, materias_aprobadas)


if __name__ == '__main__':
    main()
