# WHILE:
# Esto es un comentario
fin = int(input("Digite el último número a imprimir:"))
x = 0
while x <= fin:
    if x % 2 == 0:
        print("El último valor de x durante la condicional es: " + str(x))
    else:
        print("El valor ingresado es impar")
    x = x + 1