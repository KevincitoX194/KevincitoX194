def calcular():
    operacion = input("Ingrese la operación (+, -, *, /): ")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if operacion == '+':
        print(f"Resultado: {num1 + num2}")
    elif operacion == '-':
        print(f"Resultado: {num1 - num2}")
    elif operacion == '*':
        print(f"Resultado: {num1 * num2}")
    elif operacion == '/':
        print(f"Resultado: {num1 / num2}")
    else:
        print("Operación no válida.")

calcular()