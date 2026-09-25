# Lista de Tarefas

# 1 - Mostrar as tarefas
# 2 - Mostrar as tarefas concluidas
# 3 - Mostrar as tarefas não concluidas
# 4 - Mostrar as tarefas por Prioridades
# 5 - Mostrar tarefa nova
# 6 - Finalizar tarefas
# 7 - Remover tarefas
# 0 - sair
lista_tarefas = [
    {"titulo":"Estudar","Concluida":"SIM", "Prioridade":"Alta"},
    {"titulo":"Ler","Concluida":"NÃO", "Prioridade":"Baixa"},
    {"titulo":"Comprar_lanche","Concluida":"SIM", "Prioridade":"Média"}
]

def tarefas_concluidas():
    for tarefa in lista_tarefas:
        if tarefa["Concluida"] == "SIM":
            print(tarefa)

def tarefas_nao_concluidas():
    for tarefa in lista_tarefas:
        if tarefa["Concluida"] == "NÃO":
            print(tarefa)

def prioridade():
    for tarefa in lista_tarefas:
        if tarefa["Prioridade"] == "Alta":
            print(tarefa)
    for tarefa in lista_tarefas:
        if tarefa ["Prioridade"] == "Média":
            print(tarefa)
    for tarefa in lista_tarefas:
        if tarefa["Prioridade"] == "Baixa":
            print(tarefa)

def cadastrar():
        tarefa_cadastro = input("Qual tarefa você gostaria de cadastrar?: ")
        prioridade = input("Qual a prioridade da tarefa?: ")

        cadastrar_tarefa = {
        "titulo": tarefa_cadastro,
        "Concluida": "Não",
        "Prioridade": prioridade
        }
        lista_tarefas.append(cadastrar_tarefa)
        print(lista_tarefas)

def re_tarefa():
    remove_tarefa = str(input("Digite o Nome da Tarefa que você deseja remover: "))

    for tarefa in lista_tarefas:
        if tarefa["titulo"] == 

    for tarefa in lista_tarefas:
        if tarefa ["titulo"] == remove_tarefa:
            lista_tarefas.remove(remove_tarefa)
            
        





while True:
    print("1 - Mostrar as tarefas")
    print("2 - Mostrar as tarefas concluidas")
    print("3 - Mostrar as tarefas não concluidas")
    print("4 - Mostrar as tarefas por Prioridades")
    print("5 - Cadastrar uma tarefa nova")
    print("6 - Finalizar tarefas")
    print("7 - Remover tarefas")
    print("0 - sair")
    opcao = input("Qual ação você deseja fazer?: ")

    if opcao == "1":
        print(lista_tarefas)

    elif opcao == "2":
        tarefas_concluidas()

    elif opcao == "3":
        tarefas_nao_concluidas()

    elif opcao == "4":
        prioridade()

    elif opcao == "5":
        cadastrar()

    elif opcao == "7":
        re_tarefa()

    elif opcao == "0":
        print("Saindo da lista de tarefas...")
        break


    


