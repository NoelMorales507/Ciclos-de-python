secreto = 7 
intentos = int(input("Adivina el número secreto del 1 al 10:  "))
while intentos != secreto:
    if intentos < secreto:
        print("ni por ahí, el número secreto es mayor")
    else:
        print ("ni por ahí, el número secreto es menor")
    intentos = int(input("Intentalo de nuevo porfavor:"))
print("felicidades hasta que alfin lo lograste")
