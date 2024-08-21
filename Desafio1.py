import random

def crear_matriz (alumnos, materias):
    n=len(alumnos)+1
    m=len(materias)+1
    matriz=[[0]*m for fill in range(n)]
    matriz[0][0]= "Nro legajo"
    for i in range (1,m):
        matriz[0][i]= materias[i-1] #Rellena la primera fila encabezado de materias, aparte de el 0 0
    return matriz

def llenar_matriz(matriz, alumnos):
    filas = len(matriz)
    for fil in range(1, filas):
        matriz[fil][0] = alumnos[fil-1] #Rellena la primera columna con encabezado de alumnos
        columnas = len(matriz[0])
        for col in range(1, columnas):
            '''Llena notas con numeros aleatorios'''
            num = random.randint(1, 10)
            matriz[fil][col] = num

def mostrar_matriz (matriz):
    for fila in matriz:
        print(fila)

def promedio_alumnos (matriz):
    promedios =[]
    filas= len(matriz)
    columnas= len(matriz[0])
    for i in range (1,filas):
        suma=0
        for j in range (1,columnas):
            suma += matriz[i][j]
        promedio = suma / (columnas - 1)
        promedios.append (promedio)
    print(promedios)

def promedio_materias (matriz):
    promaterias = []
    filas= len(matriz)
    columnas = len(matriz[0])
    for i in range (1,columnas):
        suma=0
        for j in range (1,filas):
            suma += matriz[j][i]
        prom= suma/(filas-1)
        promaterias.append(prom)
    print(promaterias)


alumnos=[]
matriz= [[],[]]

for i in range (10):
    leg = random.randint(0,100000000)
    alumnos.append(leg)
    
materias = ['Fundamentos de quimica', 'Matematica Discreta','Programacion I','Algebra', 'Arquitectura de computadores']

matriz = crear_matriz(alumnos,materias)
llenar_matriz(matriz,alumnos)
mostrar_matriz(matriz)
promedio_alumnos(matriz)
promedio_materias(matriz)