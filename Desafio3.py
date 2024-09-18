def recortar_dato(texto, max_len):
    """Recorta el texto a una longitud máxima de max_len caracteres."""
    return texto[:max_len]

def convertir_a_mayusculas(texto):
    """Convierte el texto a mayúsculas."""
    return texto.upper()

def agregar_alumno(matrizalumnos):
    legajo = int(input('Ingrese el legajo: '))
    nombre = convertir_a_mayusculas(input('Ingrese el nombre: '))
    apellido = convertir_a_mayusculas(input('Ingrese el apellido: '))
    
    # Limitar nombre y apellido a 20 caracteres
    nombre = recortar_dato(nombre, 20)
    apellido = recortar_dato(apellido, 20)
    
    matrizalumnos.append([legajo, nombre, apellido])
    print('Alumno agregado correctamente.')

def leer_alumno(matrizalumnos):
    legajo = int(input('Ingrese el legajo del alumno que desea buscar: '))
    for alumno in matrizalumnos:
        if alumno[0] == legajo:
            print(f'El alumno {alumno} ha sido encontrado.')
            return
    print('No se ha encontrado el alumno con el legajo ingresado')

def actualizar_alumno(matrizalumnos):
    legajo = int(input('Ingrese el legajo del alumno a actualizar: '))
    for i in range(len(matrizalumnos)):
        if matrizalumnos[i][0] == legajo:
            nuevo_nombre = convertir_a_mayusculas(input('Ingrese el nuevo nombre: '))
            nuevo_apellido = convertir_a_mayusculas(input('Ingrese el nuevo apellido: '))
            # Limitar nombre y apellido a 20 caracteres
            nuevo_nombre = recortar_dato(nuevo_nombre, 20)
            nuevo_apellido = recortar_dato(nuevo_apellido, 20)
            
            matrizalumnos[i][1] = nuevo_nombre
            matrizalumnos[i][2] = nuevo_apellido
            print('Datos actualizados.')
            return
    print('No se ha encontrado el alumno a actualizar')

def eliminar_alumno(matrizalumnos):
    legajo = int(input('Ingrese el legajo del alumno a eliminar: '))
    for alumno in matrizalumnos:
        if alumno[0] == legajo:
            matrizalumnos.remove(alumno)
            print('Alumno eliminado correctamente.')
            return
    print('Alumno no encontrado')

def mostrar_matriz(matrizalumnos):
    """Muestra en forma de tabla"""
    print(f"{'Legajo':<10} {'Nombre':<20} {'Apellido':<20}")
    print('-' * 50)
    for alumno in matrizalumnos:
        print(f"{alumno[0]:<10} {alumno[1]:<20} {alumno[2]:<20}")

def ordenar_matriz(matrizalumnos):
    """Ordena la matriz por legajo y secundario por nombre."""
    matrizalumnos.sort(key=lambda x: (x[0], x[1]))

matrizalumnos = []
agregar_alumno(matrizalumnos)
leer_alumno(matrizalumnos)
eliminar_alumno(matrizalumnos)
actualizar_alumno(matrizalumnos)
print("Matriz antes de ordenar:")
mostrar_matriz(matrizalumnos)
ordenar_matriz(matrizalumnos)
print("Matriz después de ordenar:")
mostrar_matriz(matrizalumnos)