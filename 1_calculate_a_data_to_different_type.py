def run():
    # convertir un cadena de texto a entero
    number = input('escribe un nuemro: ')
    number = int(number)
    print("se convirtio en entero el numero: ",number)

    # convertir un entero a cadena de texto
    text = str(number)
    print('se convirtio en cadena de texto el numero: ',text)


if __name__ == "__main__":
    run()