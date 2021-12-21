def run():
    name = input('ingrese su nombre: ')
    #convertir toda la cadena a mayuscula
    print('su nombre en mayuscula =>',name.upper())
    #convertir la primera letra del cadena a mayuscula
    print('su nombre en mayuscula =>',name.capitalize())
    #convertir la cadena en minuscula
    print('su nobre en minuscula =>',name.lower())
    #quitar los espacios de la cadena
    print('su nombre sin los espacio innecesario =>',name.strip())
    #remplazar letra
    a=input('ingrese la letra que queire cambiar')
    b=input('ingrese la letra que quiere remplazar')
    print('las palabras ya remplasadas =>',name.replace(a,b))
    #indice o posiciones de cada letra
    print('PARA MAS METODOS O FUNCIONES VAMOS A LA DOCUMENTACION: https://docs.python.org/3/library/functions.html#oct')

if __name__ == "__main__":
    run()
    print("hola")