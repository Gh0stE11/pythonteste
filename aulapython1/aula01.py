print("1.Soma")
print("2.Subtracao")
print("3.Divisao")
print("4.Multiplicacao")

operacao = int(input("Insira o tipo de operação desejada:"))

if operacao == 1:

    numb1 = float(input("Insira o numero 1:"))
    numb2 = float(input("Insira o numero 2:"))
    res = numb1 + numb2

print("A soma dos numeros inseridos é:", res)

elif operacao == 2:

    numb1 = float(input("Insira o numero 1:"))
    numb2 = float(input("Insira o numero 2:"))
    res = numb1 - numb2

print("A soma dos numeros inseridos é:", res)

elif operacao == 3:

    numb1 = float(input("Insira o numero 1:"))
    numb2 = float(input("Insira o numero 2:"))
    res = numb1/numb2

print("A soma dos numeros inseridos é:", res)

elif operacao == 4:

    numb1 = float(input("Insira o numero 1:"))
    numb2 = float(input("Insira o numero 2:"))
    res = numb1 * numb2

print("A soma dos numeros inseridos é:", res)


