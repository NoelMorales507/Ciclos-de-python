numero =int(input("¿Hasta que número quieres sumar? "))
suma = 0
for i in range(1, numero + 1):
    suma += i
print("La suma de los números del 1 al", numero, "Es:", suma)