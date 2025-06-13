listaDNI = []
listaConjuntos = []

print("== Semana de Integración II - Matemática ==")

print("Operaciones")
print("A. Operaciones con multiples DNI")
print("B. Operaciones con años de Nacimiento")
opcion = input("Seleccione una opción: ")

if opcion.lower() == "a":
    cantidad = int(input("Elija si ingresará 2 ó 4 DNI: "))
    while cantidad != 2 and cantidad != 4:
        cantidad = int(input("Elija si ingresará 2 ó 4 DNI: "))
    for i in range(1, cantidad+1):
        entrada = input("Ingrese el DNI: ")
        if entrada.isdigit():
            listaDNI.append(entrada)
    
    for dni in listaDNI:
        listaConjuntos.append(set(dni))
        print(f"A partir del DNI {dni} se obtuvo el conjunto: {set(dni)}")

    if len(listaDNI) == 2:
        print("Operaciones con conjuntos")
        a = set(listaDNI[0])
        b = set(listaDNI[1])
        print(f"El resultado de la unión entre los conjuntos {listaConjuntos[0]} y {listaConjuntos[1]} es: {a.union(b)}")
        print(f"El resutlado de la intersección entre los conjuntos {listaConjuntos[0]} y {listaConjuntos[1]} es: {a.intersection(b)}")
        print(f"El resultado de la diferencia entre los conjuntos {listaConjuntos[0]} y {listaConjuntos[1]} es: {a.difference(b)}")
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
        print(f"El resultado de la diferencia entre los conjuntos {listaConjuntos[2]} y {listaConjuntos[3]} es: {c.difference(d)}")
        print(f"El resultado de la diferencia simétrica entre los conjuntos {listaConjuntos[0]} y {listaConjuntos[1]} es: {a.symmetric_difference(b)}")
        print(f"El resultado de la diferencia simétrica entre los conjuntos {listaConjuntos[2]} y {listaConjuntos[3]} es: {c.symmetric_difference(d)}")

    for dni in listaDNI:
        dni_str = str(dni)
        for digito in set(dni):
            repite = dni_str.count(digito)
            print(f"El dígito {digito} se  repite {repite} veces en {dni_str}")
    
    # Evaluar condiciones lógicas (Si el hay un número común en los conjuntos)
    # y la condición lógica con respecto a si los conjuntos ingresados tiene una cantidad par de elementos o no

elif opcion.lower() == "b":
    # Trabajo con los años de nacimiento (borrar el pass.)
    pass
else:
    print("Opción incorrecta")