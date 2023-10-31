#3.	Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y
# devuelva una lista con las posiciones en donde se encuentra b dentro de a
def encontrar(string1, string2, indice=0):
    if indice >= len(string1) - len(string2) + 1:
        return []
    if string1[indice:indice + len(string2)] == string2:
        return [indice] + encontrar(string1, string2, indice + 1)
    else:
        return encontrar(string1, string2, indice + 1)


string1 = input("Ingrese el primer string: ").lower()
string2 = input("Ingrese el segundo string: ").lower()
posiciones = encontrar(string1, string2)


print(f"Las posiciones donde '{string2}' aparece en '{string1}' son: {posiciones}")