#Habia que cambiar los valores de las funciones por las variables usadas en ella
#y no usar  a y b que no se usaban en la funcion
def most(x,y):
    if(x>y):
        return x
    else:
        return y


def least(x,y):
    if(x<y):
        return x
    else:
        return y

x= int(input("Un numero: "))
y= int(input("Otro numero: "))

print(most(x-3, least(x+2, y-5)))