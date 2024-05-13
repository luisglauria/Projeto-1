import os

atividades = [ ]
nomes = [ ]

def adicionar_atividade():
    os.system("cls")
    nome_atividade = input("Digite o nome da atividade que você quer adicionar: ").lower()
    dia_da_semana = input("Digite o dia da semana da atividade: ").lower()

    for atividade in atividades:
        if nome_atividade == atividade:
            print("A atividade já foi adicionada!")
            input("Pressione ENTER para continuar")
            return
        
    horario_atividade = input("Digite o horário da atividade: ")
    separador = '-----------------'

    os.system("cls")

    tipo_atividade = f"""Atividade: {nome_atividade}\nHorário: {horario_atividade}\nDia da semana: {dia_da_semana}\n{separador}"""
    atividades.append(nome_atividade)
    
    with open("lista.txt", "a", encoding="UTF-8") as arquivo:
        arquivo.write(tipo_atividade)
        arquivo.write("\n")
    print("Atividade adicionada com sucesso!\n") 
    input("Pressione ENTER para continuar")

def atualizar_atividade():
    nova_atividade = input("Digite a atividade que você quer atualizar: ").lower()

    if nova_atividade not in nomes:
        print(f"\nA atividade '{nova_atividade}' não foi encontrada.")
        return

    tipo_atividade_nova = input("\nDigite o novo tipo de Atividade: ").lower()
    dia_da_semana_novo = input("Digite o novo Dia Da Semana: ").lower()
    horario_novo = input("Digite o novo Horário: ").lower()
    separador = "----------"

    nova_atividade_formatada = f"Atividade Nova: {tipo_atividade_nova}\nDia da Semana: {dia_da_semana_novo}\nHorário Novo: {horario_novo}\n{separador}"

    with open("lista.txt", "r", encoding="UTF-8") as arquivo:
        linhas = arquivo.readlines()
    with open("lista.txt", "w", encoding="UTF-8") as arquivo:
        i = 0
        while i < len(linhas):
            if nova_atividade in linhas[i]:
                i += 3
            else:
                arquivo.write(linhas[i])
                i += 1
    with open("lista.txt", "r", encoding="UTF-8") as arquivo:
        arquivo.write(nova_atividade_formatada)
        arquivo.write("\n")

    print(f"A Atividade '{nova_atividade}' foi atualizada com sucesso.\n")
    input("Pressione ENTER para continuar")

while True:
    
    print(f"""
    ------ FUNÇÕES ------
    1. Adicionar Atividade
    2. Trocar Atividade ou Horário
    3. Visualizar cronograma
    4. Encerrar programa
    """)

    escolha = input("Escolha a função que você deseja: ")

    if escolha == '1':
        adicionar_atividade()
    elif escolha == '2':
        atualizar_atividade()
    elif escolha == '3':
        visualizar_cronograma()
    elif escolha == '4':
        print("Programa encerrado!")
        break
    else:
        print("Digite um número válido!")