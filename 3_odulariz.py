def run(edad):
    if edad > 17:
        print('Es mayor de edad',cantidad())
    elif edad > 14 and edad <17:
        print('Permiso de los padres',cantidad())
    else:
        print('eres muy menor',cantidad())


def cantidad():
    print('cantidad de personas que ingresan')
    canti = int(input('ingrese la cantidad de personas'))
    return canti

if __name__ == "__main__":
    age=int(input('Ingrese su edad'))
    run(age)