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