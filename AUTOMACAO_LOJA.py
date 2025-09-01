# Dicionários e listas para armazenar os dados

# Estoque: 'produto': quantidade
estoque = {
    "Vestido Floral": 15,
    "Calça Jeans Skinny": 20,
    "Blusa de Tricô": 10,
    "Saia Midi Preta": 8
}

# Caixa: Saldo inicial e listas de transações
saldo_caixa = 500.00
transacoes_caixa = []

def adicionar_produto_estoque():
    """Adiciona um novo produto ou mais quantidade a um existente no estoque."""
    nome_produto = input("Digite o nome do produto: ").strip().title()
    try:
        quantidade = int(input("Digite a quantidade a ser adicionada: "))
        if quantidade <= 0:
            print("A quantidade deve ser um número positivo.")
            return

        if nome_produto in estoque:
            estoque[nome_produto] += quantidade
            print(f"{quantidade} unidades de '{nome_produto}' adicionadas. Total: {estoque[nome_produto]}")
        else:
            estoque[nome_produto] = quantidade
            print(f"'{nome_produto}' adicionado ao estoque com {quantidade} unidades.")
    except ValueError:
        print("Entrada inválida. A quantidade deve ser um número inteiro.")

def remover_produto_estoque():
    """Remove uma quantidade de um produto existente no estoque."""
    nome_produto = input("Digite o nome do produto: ").strip().title()
    if nome_produto not in estoque:
        print("Produto não encontrado no estoque.")
        return

    try:
        quantidade = int(input(f"Digite a quantidade de '{nome_produto}' a ser removida: "))
        if quantidade <= 0:
            print("A quantidade deve ser um número positivo.")
            return

        if quantidade > estoque[nome_produto]:
            print(f"Não é possível remover {quantidade} unidades. O estoque atual é de {estoque[nome_produto]}.")
        else:
            estoque[nome_produto] -= quantidade
            print(f"{quantidade} unidades de '{nome_produto}' removidas. Restam: {estoque[nome_produto]}")
            if estoque[nome_produto] == 0:
                print(f"'{nome_produto}' está com estoque zerado e foi removido da lista.")
                del estoque[nome_produto]
    except ValueError:
        print("Entrada inválida. A quantidade deve ser um número inteiro.")

def visualizar_estoque():
    """Mostra todos os produtos e suas quantidades no estoque."""
    print("\n--- Estoque Atual ---")
    if not estoque:
        print("O estoque está vazio.")
    else:
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade} unidades")
    print("---------------------\n")

def registrar_venda():
    """Registra uma venda, atualiza o saldo do caixa e remove do estoque."""
    global saldo_caixa
    nome_produto = input("Digite o nome do produto vendido: ").strip().title()
    if nome_produto not in estoque:
        print("Produto não encontrado no estoque.")
        return

    try:
        quantidade_vendida = int(input(f"Digite a quantidade de '{nome_produto}' vendida: "))
        if quantidade_vendida <= 0:
            print("A quantidade deve ser um número positivo.")
            return
        
        if quantidade_vendida > estoque[nome_produto]:
            print(f"Venda não pode ser registrada. Apenas {estoque[nome_produto]} unidades de '{nome_produto}' em estoque.")
            return

        valor_venda = float(input("Digite o valor total da venda: R$ "))
        
        # Atualiza estoque e caixa
        estoque[nome_produto] -= quantidade_vendida
        saldo_caixa += valor_venda
        
        transacao = {
            'tipo': 'venda',
            'produto': nome_produto,
            'quantidade': quantidade_vendida,
            'valor': valor_venda
        }
        transacoes_caixa.append(transacao)
        
        print(f"Venda de {quantidade_vendida} unidades de '{nome_produto}' registrada com sucesso!")
        print(f"Novo saldo do caixa: R$ {saldo_caixa:.2f}")

    except ValueError:
        print("Entrada inválida. A quantidade e o valor devem ser números.")

def registrar_despesa():
    """Registra uma despesa e subtrai do saldo do caixa."""
    global saldo_caixa
    descricao_despesa = input("Digite a descrição da despesa (ex: aluguel, luz): ").strip().title()
    try:
        valor_despesa = float(input("Digite o valor da despesa: R$ "))
        if valor_despesa <= 0:
            print("O valor da despesa deve ser positivo.")
            return

        saldo_caixa -= valor_despesa
        
        transacao = {
            'tipo': 'despesa',
            'descricao': descricao_despesa,
            'valor': valor_despesa
        }
        transacoes_caixa.append(transacao)

        print(f"Despesa de R$ {valor_despesa:.2f} registrada com sucesso.")
        print(f"Novo saldo do caixa: R$ {saldo_caixa:.2f}")

    except ValueError:
        print("Entrada inválida. O valor deve ser um número.")

def visualizar_caixa():
    """Mostra o saldo atual do caixa e as últimas transações."""
    print("\n--- Controle de Caixa ---")
    print(f"Saldo atual: R$ {saldo_caixa:.2f}")
    print("\nÚltimas transações:")
    if not transacoes_caixa:
        print("Nenhuma transação registrada ainda.")
    else:
        for transacao in transacoes_caixa[-5:]: # Mostra as últimas 5 transações
            if transacao['tipo'] == 'venda':
                print(f"Venda de {transacao['quantidade']} unidades de '{transacao['produto']}' - Valor: R$ {transacao['valor']:.2f}")
            elif transacao['tipo'] == 'despesa':
                print(f"Despesa ('{transacao['descricao']}') - Valor: -R$ {transacao['valor']:.2f}")
    print("------------------------\n")

def menu_principal():
    """Exibe o menu de opções e processa a escolha do usuário."""
    while True:
        print("--- Menu Principal ---")
        print("1. Adicionar produto ao estoque")
        print("2. Remover produto do estoque")
        print("3. Visualizar estoque")
        print("4. Registrar venda")
        print("5. Registrar despesa")
        print("6. Visualizar caixa")
        print("7. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_produto_estoque()
        elif escolha == '2':
            remover_produto_estoque()
        elif escolha == '3':
            visualizar_estoque()
        elif escolha == '4':
            registrar_venda()
        elif escolha == '5':
            registrar_despesa()
        elif escolha == '6':
            visualizar_caixa()
        elif escolha == '7':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 7.")

# Executa o menu
if __name__ == "__main__":
    menu_principal()
