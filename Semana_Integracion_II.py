# Funciones

def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def digito_comun(lista_conjuntos, digito):
    return all(digito in conjunto for conjunto in lista_conjuntos)

def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero = numero // 10
    return suma

# Programa principal
while True:
    listaDNI = []
    listaConjuntos = []

    print("== Semana de Integración II - Matemática ==")

    print("Operaciones")
    print("A. Operaciones con multiples DNI")
    print("B. Operaciones con años de Nacimiento")
    print("Presione ENTER para terminar.")
    opcion = input("Seleccione una opción: ")
    
    if not opcion: # Si el usuario solo presiona Enter, sale del bucle
        break

    if opcion.lower() == "a":
        cantidad = int(input("Elija si ingresará 2 ó 4 DNI: "))
        while cantidad != 2 and cantidad != 4:
            cantidad = int(input("Elija si ingresará 2 ó 4 DNI: "))
        for i in range(0, cantidad):
            entrada = input("Ingrese el DNI: ")
            if entrada.isdigit():
                listaDNI.append(entrada)
    
        for dni in listaDNI:
            listaConjuntos.append(set(dni))
        
        for i in range(0, len(listaConjuntos)):
            print(f"A partir del DNI {listaDNI[i]} se obtuvo el conjunto: {listaConjuntos[i]}")

        if len(listaDNI) == 2:
            print("Operaciones con conjuntos")
            a = set(listaDNI[0])
            b = set(listaDNI[1])
            print(f"El resultado de la unión entre los conjuntos {listaConjuntos[0]} y {listaConjuntos[1]} es: {a.union(b)}")
            print(f"El resutlado de la intersección entre los conjuntos {listaConjuntos[0]} y {listaConjuntos[1]} es: {a.intersection(b)}")
            print(f"El resultado de la diferencia entre los conjuntos {listaConjuntos[0]} y {listaConjuntos[1]} es: {a.difference(b)}")
            print(f"El resultado de la diferencia entre los conjuntos {listaConjuntos[1]} y {listaConjuntos[0]} es: {b.difference(a)}")
            print(f"El resultado de la diferencia simétrica entre los conjuntos {listaConjuntos[0]} y {listaConjuntos[1]} es: {a.symmetric_difference(b)}")
        elif len(listaDNI) == 4:
            a = set(listaDNI[0])
            b = set(listaDNI[1])
            c = set(listaDNI[2])
            d = set(listaDNI[3])
            print(f"El resultado de la unión entre los conjuntos {listaConjuntos[0]} y {listaConjuntos[1]} es: {a.union(b)}")
            print(f"El resultado de la unión entre los conjuntos {listaConjuntos[2]} y {listaConjuntos[3]} es: {c.union(d)}")
            print(f"El resutlado de la intersección entre los conjuntos {listaConjuntos[0]} y {listaConjuntos[1]} es: {a.intersection(b)}")
            print(f"El resutlado de la intersección entre los conjuntos {listaConjuntos[2]} y {listaConjuntos[3]} es: {c.intersection(d)}")
            print(f"El resultado de la diferencia entre los conjuntos {listaConjuntos[0]} y {listaConjuntos[1]} es: {a.difference(b)}")
            print(f"El resultado de la diferencia entre los conjuntos {listaConjuntos[1]} y {listaConjuntos[0]} es: {b.difference(a)}")
            print(f"El resultado de la diferencia entre los conjuntos {listaConjuntos[2]} y {listaConjuntos[3]} es: {c.difference(d)}")
            print(f"El resultado de la diferencia entre los conjuntos {listaConjuntos[3]} y {listaConjuntos[2]} es: {d.difference(c)}")
            print(f"El resultado de la diferencia simétrica entre los conjuntos {listaConjuntos[0]} y {listaConjuntos[1]} es: {a.symmetric_difference(b)}")
            print(f"El resultado de la diferencia simétrica entre los conjuntos {listaConjuntos[2]} y {listaConjuntos[3]} es: {c.symmetric_difference(d)}")

        for dni in listaDNI:
            string_dni = str(dni)
        for digito in set(dni):
            repite = string_dni.count(digito)
            print(f"El dígito {digito} se  repite {repite} veces en {string_dni}")
    
        for dni in listaDNI:
            num = int(dni)
        print(f"La suma de los dígitos presentes en el DNI {dni} da como resultado: {suma_digitos(num)}")
    
        for i in range(0, 10):
            if digito_comun(listaConjuntos, str(i)) is True:
                print(f"El dígito {i} forma parte de todos los conjuntos, entonces {i} es un número común")
    
        contador = 0
        for conjunto in listaConjuntos:
            if len(conjunto) % 2 == 0:
                contador += 1

        if contador > (len(listaConjuntos) / 2):
            print(f"De los {len(listaConjuntos)}, hay {contador} conjuntos con una cantidad par de elementos por ende el grupo se considera par")

    elif opcion.lower() == "b":
        años = []
        print("Por favor ingrese 4 años de nacimiento")
        while len(años) < 4:
            entrada = int(input(f"Ingrese el año de nacimiento: "))
            if entrada in años:
                print("Año repetido, ingrese un año distinto.")
            else:
                años.append(entrada)

        pares = 0
        impares = 0
        for entrada in años:
            if entrada % 2 == 0:
                pares += 1
            else:
                impares += 1
        print(f"Cantidad de años pares: {pares}")
        print(f"Cantidad de años impares: {impares}")
        
        for year in años:
            if es_bisiesto(year):
                print(f"Tenemos un año especial. {year} Es bisiesto.")
        
        if all(entrada > 2000 for entrada in años):
            print("Todos los años ingresados pertenecen al grupo Z")
        else:
            print("Existe al menos un integrante del grupo que no pertenece al grupo Z")

    
print("Fin del programa.")