alumnos = [
    ["Ana", 8, 9, 7],
    ["Juan", 5, 6, 4],
    ["Mariana", 9, 10, 10],
    ["Juan", 8, 7, 9],
    ["Pedro", 4, 5, 3],
    ["Lucia", 10, 9, 10],
    ["Ana", 6, 4, 5]
]
def alcular_promedio(nombre):
    alumn = []

    for alumno in alumnos:
        cantidad = 1
        lugar = 1
        suma = 0
        if alumno[0] == nombre:
            a = len(alumno)
            while cantidad < a:
                suma = suma + alumno[lugar]
                lugar += 1
                cantidad += 1
            promedio = suma / (a - 1)
            nom = []
            nom.append(alumno[0])
            nom.append(promedio)
            alumn.append(nom)

    if alumn == []:
        return "No se encontró ningún alumno con ese nombre"

    return alumn
def alumnos_aprobados(lis_alumnos):
   
   aprobados = []
   nueva_lista = []
   notas = []
   for alumno in lis_alumnos:
    nombre = alumno[0]
    if nombre not in nueva_lista:
       nueva_lista.append(nombre)
       notas = alcular_promedio(nombre)
       for nota in notas:
          if nota[1] >= 6:
             aprobados.append(nota)
   return aprobados
def mejor_alumno(lis_alumnos):
   
   mayor = []
   nota = 0
   maximo = []
   for alumno in lis_alumnos:
      if alumno[0] not in mayor:
         mayor = alcular_promedio(alumno[0])
         for may in mayor:
            if may[1] > nota:
               nota = may[1]
               maximo = [may]
            elif may[1] == nota:
               maximo.append(may)
   return maximo
def estadisticas(lis_alumnos):
   promedio = []
   menor_nota = []
   total = 0
   menor = 10
   cantidad_de_alumnos = len(lis_alumnos)
   cantida_aprobados = len(alumnos_aprobados(lis_alumnos))
   desaprobados = cantidad_de_alumnos - cantida_aprobados
   for alumno in lis_alumnos:
      if alumno[0] not in promedio:
         alumn = alcular_promedio(alumno[0])
         promedio.append(alumno[0])
         for nota in alumn:
            total = total + nota[1]
            if nota[1] < menor:
               menor_nota = [nota]
               menor = nota[1]
            elif nota[1] == menor:
               menor_nota.append(nota)
    
   return print(f"cantidadaa alumnos {cantidad_de_alumnos},aprobados{cantida_aprobados},desaprobados{desaprobados}, menor nota{menor_nota}promedio{total/cantidad_de_alumnos} ")
    
def ordena_lista(lis_alumno):
    lugares = []
    lista_auxiliar = []
    ordenar = []

    for alumno in lis_alumno:
        if alumno[0] not in lista_auxiliar:
            promedio = alcular_promedio(alumno[0])
            lista_auxiliar.append(alumno[0])

            for alumn in promedio:
                lugares.append(alumn)

    for lugar in lugares:
        posicion = 0

        while posicion < len(ordenar) and ordenar[posicion][1] >= lugar[1]:
            posicion += 1

        ordenar.insert(posicion, lugar)

    return ordenar

print(ordena_lista(alumnos))


         


