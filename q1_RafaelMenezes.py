criar_conta = lambda: {"nome": input("Digite o nome do usuário: "), "saldo": float(input("Digite o valor na conta bancária: "))}

realizar_transacao = lambda conta: (
    "Depósito efetuado! Novo saldo: R$ " + str(conta["saldo"] + float(input("Digite o valor do depósito: ")))
    if input("Escolha 'D' para depósito ou 'S' para saque: ").upper() == "D"
    else "Saque efetuado! Novo saldo: R$ " + str(conta["saldo"] - float(input("Digite o valor do saque: ")))
) if input("Deseja realizar uma transação? (S/N): ").upper() == "S" else "Nenhuma transação realizada."

conta = criar_conta()

resultado = realizar_transacao(conta)

print(resultado)
