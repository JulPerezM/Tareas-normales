print("Este algoritmo le avisa del estado actual de hemoglobina de los pacientes")
n = input("Ingrese la cantidad de pacientes registrados: ")  # Pido la cantidad de estudiantes con nota

while all(map(str.isdigit, n)) is False:  # Identifico si el valor ingresado es un numero
    print("Tiene que introducir un valor numerico")
    n = input("Ingrese la cantidad de pacientes registrados: ")

n = int(n)
s = 0
HB = 0  # Hombres con hemoglobina baja
LHB = []  # Lista de Hombres con hemoglobina baja

HM = 0  # Hombres con hemoglobina media
LHM = []  # Lista de Hombres con hemoglobina media

HA = 0  # Hombres con hemoglobina alta
LHA = []  # Lista de Hombres con hemoglobina alta

MB = 0  # Mujeres con hemoglobina baja
LMB = []  # Lista de Mujeres con hemoglobina baja

MM = 0  # Mujeres con hemoglobina media
LMM = []  # Lista de Mujeres con hemoglobina media

MA = 0  # Mujeres con hemoglobina alta
LMA = []  # Lista de Mujeres con hemoglobina alta

while n > s:
    # Hago listas para identificar los pacientes con sus respectivos diagnosticos
    s += 1

    g = int(input("Ingrese el genero del paciente (1 para masculino, 2 para femenino): "))
    while g != 1 and g != 2:
        print("Tiene que ingresar uno de los 2 generos biologicos asignados")
        g = int(input("Ingrese el genero del paciente (1 para masculino, 2 para femenino): "))

    h = float(input("Ingrese el resultado de la prueba de hemoglobina: "))

    if g == 2:  # Para las mujeres
        if h > 15:
            MA += 1
            LMA.append(s)
        elif 12.6 <= h <= 15:
            MM += 1
            LMM.append(s)
        elif 12.6 > h:
            MB += 1
            LMB.append(s)

    elif g == 1:  # Para los hombres
        if h > 16.6:
            HA += 1
            LHA.append(s)
        elif 12.2 <= h <= 16.6:
            HM += 1
            LHM.append(s)
        elif 12.2 > h:
            HB += 1
            LHB.append(s)

print("Teniendo los datos registrados, podemos decir que:")
print("La cantidad de hombres con hemoglobina alta es de", HA)
if HA > 0:
    print("y estos fueron los pacientes numero: ")
    for pacientes in LHA:
        print(pacientes)


print("La cantidad de hombres con hemoglobina normal es de", HM)
if HM > 0:
    print("y estos fueron los pacientes numero: ")
    for pacientes in LHM:
        print(pacientes)


print("La cantidad de hombres con hemoglobina baja es de", HB)
if HB > 0:
    print("y estos fueron los pacientes numero: ")
    for pacientes in LHB:
        print(pacientes)


print("La cantidad de mujeres con hemoglobina alta es de", MA)
if MA > 0:
    print("y estos fueron los pacientes numero: ")
    for pacientes in LMA:
        print(pacientes)


print("La cantidad de mujeres con hemoglobina normal es de", MM)
if MM > 0:
    print("y estos fueron los pacientes numero: ")
    for pacientes in LMM:
        print(pacientes)


print("La cantidad de mujeres con hemoglobina baja es de", MB,)
if MB > 0:
    print("y estos fueron los pacientes numero: ")
    for pacientes in LMB:
        print(pacientes)
