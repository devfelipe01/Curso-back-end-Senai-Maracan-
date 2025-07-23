print("Calculadora")
while True:
    print("Escolha uma das seguintes operações: Soma, subtração, multiplicação, divisão")
    operação =input("- ").strip().lower()
    if operação not in("soma","subtração","subtracao","multiplicação","multiplicacao","divisão", "divisao"):
        print("Operação inválida")
        continue

    n1 =float(input('Primeiro número: '))
    n2 =float(input('Segundo número: '))

    if operação == 'soma':
        print(f"Resultado: {n1 + n2}")
    elif operação in("subtração","subtracao"):
        print(f"resultado: {n1 - n2}")
    elif operação in("multiplicação","multiplicacao"):
        print(f"resultado: {n1 * n2}")
    elif operação in("divisão", "divisao"):
        if n2 == 0:
            print("Operação inválida")
        else:
            print(f"Reultado: {n1/n2}")
    
    print("Deseja fazer outra operação?")
    continuar = input("- ").strip().lower()
    if continuar != 's' and continuar != 'sim':
        break