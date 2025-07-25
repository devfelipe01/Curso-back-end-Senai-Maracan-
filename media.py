print("Boletim escolar")
while True:
    print("Adicione as notas do aluno: Digite 'sair' quando terminar de adicionar")
    notas = []

    while True:
        nota=(input("- ")).lower().strip()
        if nota == "sair":
            break
        nota = float(nota)
        if nota > 10:
            print("Nota inválida")
            continue
        notas.append(nota)
    
    media = sum(notas)/len(notas)
    print(f"A média do aluno é: {media}")

    maior_nota = notas[0]
    menor_nota = notas[0]

    for nota in notas:
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota
        
    print(f"A menor nota desse aluno é: {menor_nota}")
    print(f"A maior nota desse aluno é: {maior_nota}")

    if media >= 7:
        print("Aluno APROVADO!")
    if media < 7:
        print("Aluno REPROVADO!")

    print("Deseja adicionar notas de outro aluno? Responda (S/N)")
    continuar=input("- ").lower().strip()

    if continuar not in "s":
        break