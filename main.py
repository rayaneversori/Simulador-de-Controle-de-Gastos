despesas = []

def adicionar_despesa():
    categoria = input("Categoria: ")
    valor = float(input("Valor: R$ "))
    despesas.append({"categoria": categoria, "valor": valor})
    print("Despesa adicionada com sucesso!")

def visualizar_despesas():
    if despesas:
        for despesa in despesas:
            print(f"{despesa['categoria']}: R$ {despesa['valor']:.2f}")
    else:
        print("Nenhuma despesa registrada.")

def menu():
    while True:
        print("\n=== Controle de Gastos ===")
        print("1. Adicionar despesa")
        print("2. Visualizar despesas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_despesa()
        elif opcao == "2":
            visualizar_despesas()
        elif opcao == "3":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
    