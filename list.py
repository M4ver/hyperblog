numero=[1,44,55,66,'hola',True]
print(numero[1:])
print(numero[::-1])
##Metodo para agregar mas objetos
numero.append(False)
numero.append(55)
print(numero)
#Metodo para quitar objetos colocando el indice en los parentesis
numero.pop(2)
print(numero)


#recoreer en un for
for i in numero:
    print(i)