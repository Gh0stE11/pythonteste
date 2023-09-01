import time

print("Carregando programa...")

time.sleep(2)

print("Calculadora de Bhaskara")
a = float(input("Insira o valor de a:"))
b = float(input("Insira o valor de b:"))
c = float(input("Insira o valor de c:"))

print("Calculando...")

time.sleep(2)

delta = b**2-(4*a*c)
x1 = (-b + (delta**1/2)/(2*a))
x2 = (-b - (delta**1/2)/(2*a))

print("O x1 é igual a", x1, "e o x2 é igual a", x2)
