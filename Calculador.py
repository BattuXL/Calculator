#puta perra calculadora matematica normal

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multi(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        print("No se puede dividir entre 0")

def exponente(a, b):
    return a ** b

print("Calculadora")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Exponenciación")
print("6. Salir")

respuesta = None

while True:
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        if respuesta is None:
            num1 = float(input("Ingrese el primer número: "))
        else:
            num1 = respuesta
        num2 = float(input("Ingrese el segundo número: "))
        respuesta = suma(num1, num2)
        print("El resultado es:", respuesta)

    elif opcion == "2":
        if respuesta is None:
            num1 = float(input("Ingrese el primer número: "))
        else:
            num1 = respuesta
        num2 = float(input("Ingrese el segundo número: "))
        respuesta = resta(num1, num2)
        print("El resultado es:", respuesta)

    elif opcion == "3":
        if respuesta is None:
            num1 = float(input("Ingrese el primer número: "))
        else:
            num1 = respuesta
        num2 = float(input("Ingrese el segundo número: "))
        respuesta = multi(num1, num2)
        print("El resultado es:", respuesta)

    elif opcion == "4":
        if respuesta is None:
            num1 = float(input("Ingrese el primer número: "))
        else:
            num1 = respuesta
        num2 = float(input("Ingrese el segundo número: "))
        respuesta = division(num1, num2)
        print("El resultado es:", respuesta)

    elif opcion == "5":
        if respuesta is None:
            num1 = float(input("Ingrese el primer número: "))
        else:
            num1 = respuesta
        num2 = float(input("Ingrese el segundo número: "))
        respuesta = exponente(num1, num2)
        print("El resultado es:", respuesta)

    elif opcion == "6":
        print("chao chuchetumadre")
        break

    else:
        print("Opción no válida")

    if respuesta is not None:
        continuar = input("¿Desea continuar con el resultado? (s/n): ")
        if continuar.lower() != "s":
            respuesta = None






