class Alumno:
    def __init__(self):
        # Atributos privados
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None

    # Setters (métodos para asignar valores)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Getters (métodos para obtener los valores)
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre
    def get_nombrecompleto(self):
        return self.__nombre  + " " + self.__apellido_paterno + " "+ self.__apellido_materno

# Crear una instancia de Alumno
#Una  instancia es la creacion de un objeto a partir de una clase
alumno = Alumno()

# Asignar valores utilizando los métodos set
alumno.set_nombre("María")
alumno.set_apellido_paterno("González")
alumno.set_apellido_materno("Pérez")
alumno.set_no_control("67890")
alumno.set_semestre(5)

# Obtener valores utilizando los métodos get
print("Nombre:", alumno.get_nombre())
print("Apellido Paterno:", alumno.get_apellido_paterno())
print("Apellido Materno:", alumno.get_apellido_materno())
print("No. Control:", alumno.get_no_control())
print("Semestre:", alumno.get_semestre())
print("Nombrecompleto:", alumno.get_nombrecompleto())

# Diccionario para almacenar 50 alumnos
alumnos_dict = {}

# Crear 50 alumnos
for i in range(1, 51):
    alumno = Alumno()  # Crear una instancia vacía de Alumno

    # Asignar valores ficticios utilizando los métodos set
    alumno.set_nombre(f"Alumno{i}")
    alumno.set_apellido_paterno(f"Paterno{i}")
    alumno.set_apellido_materno(f"Materno{i}")
    alumno.set_no_control(f"NC{i:05d}")  # Número de control en formato NC00001, NC00002, etc.
    alumno.set_semestre(i % 10 + 1)  # Semestre entre 1 y 10

    # Almacenar el alumno en el diccionario, usando el número de control como clave
    registro_alumnos[alumno.get_no_control()] = alumno
    print()

# Ejemplo de cómo acceder a un alumno y mostrar su nombre completo
no_control_a_buscar = "NC00005"
if no_control_a_buscar in alumnos_dict:
    alumno = alumnos_dict[no_control_a_buscar]
    print(f"Nombre completo del alumno con no. control {no_control_a_buscar}: {alumno.nombre_completo()}")
else:
    print(f"No se encontró un alumno con no. control {no_control_a_buscar}")
