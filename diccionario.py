def run():
    dic={
        #llave:valor
        "key_1":1,
        "key_2":2,
        "key_3":3,
    }
    #solo se imprime el valor
    print(dic["key_1"])
    print(dic["key_2"])
    print(dic["key_3"])

    #el metodo keys solo pued imprimir las llaves
    for llave in dic.keys():
        print(llave)

    #el metodo que imprime los valores de las llaves
    for valor in dic.values():
        print(valor)

    #el metodo que imprime las llave sy los valores
    for llaves,valor in dic.items():
        print(llaves,"--",str(valor))

if __name__ == '__main__':
    run()