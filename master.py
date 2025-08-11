print("Programa de eligibilidade de desconto!")

def calcular_desconto(profissional,conhecimento,comunidade):
        desconto = 0

        match profissional:
            case "estudante":
                desconto += 10
            case "desempregado":
                desconto += 15
            case "empregado":
                desconto += 0
        if conhecimento == "s":
            desconto += 5
        if comunidade == "s":
            desconto += 20
        return desconto 

while True:
    print("Qual sua idade?")
    idade =int(input("-"))

    if idade < 18:
        print("Menores de idade não recebem desconto!")
        print("Deseja fazer outra verificação? Digite (S/N)")
        continuar2 =input("- ").strip().lower()
        match continuar2:
            case "s":
                continue
            case "n":
                break

    print("Qual sua situação profisisonal? Digite 'Estudante', 'Empregado e 'Desempregado'")
    profissional =input("- ").strip().lower()

    print("Você possui conhecimento prévio em TI? Digite (S/N)")
    conhecimento =input("- ").strip().lower()

    print("Você é ativo na comunidade de TI? Digite (S/N)")
    comunidade =input("- ").strip().lower()
    
    total = calcular_desconto(profissional,conhecimento,comunidade)
    
    print(f"Você tem direito a {total}% de desconto!")
    print("Deseja fazer outra verificação? Digite (S/N)")
    continuar =input("- ").strip().lower()

    if continuar != "s":
        break