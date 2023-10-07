fecha = input('Ingrese la fecha en formato día, DD/MM: ')
partes = fecha.split(', ')
dia_semana = partes[0]
dia_semana = dia_semana.upper()

numero_dia = int(fecha[fecha.find(" ") + 1:fecha.find("/")])
mes_numero = int(fecha[fecha.find("/") + 1:])

dias = {'LUNES', 'MARTES', 'MIERCOLES', 'JUEVES', 'VIERNES', 'SABADO', 'DOMINGO'}
if dia_semana not in dias or numero_dia > 31 or mes_numero > 12:
    print('Los datos ingresados son incorrectos.')
else:
    nivel = input('Ingrese el nivel: ').upper()
    if nivel == 'INICIAL' or nivel == 'INTERMEDIO' or nivel == 'AVANZADO':
        hubo_examen = input('¿Hubo examen, responda SI o NO?').upper()
        if hubo_examen == 'SI':
            cant_aprobados = int(input('Ingrese la cantidad de aprobados: '))
            cant_desaprobados = int(input('Ingrese la cantidad de desaprobados: '))
            total = cant_aprobados + cant_desaprobados
            porcentaje_aprobados = (cant_aprobados / total) * 100
            print('El porcentaje de aprobados es: ' + str(porcentaje_aprobados) + '%')
    elif nivel == 'CONVERSACION':
        asistencia = int(input('Ingrese el porcentaje de asistencia a la clase: '))
        if asistencia > 50:
            print('Asistió la mayoría.')
        else:
            print('No asistió la mayoría.')
    elif nivel == 'VIAJEROS' and (numero_dia == 1 and (mes_numero == 1 or mes_numero == 7)):
        print('Comienzo de nuevo ciclo.')
        alumnos_nuevo_ciclo = int(input('Ingrese la cantidad de nuevos alumnos: '))
        arancel = int(input('Ingrese el arancel por cada alumno: '))
        ingreso_total = alumnos_nuevo_ciclo * arancel
        print('El ingreso total es: ' + str(ingreso_total))
