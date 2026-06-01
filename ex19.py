# 1. Entrada de dados
# Adicionado o input e o .title() para aceitar "caixa", "CAIXA" ou "Caixa"
cargo = input("Digite o cargo do funcionário (Caixa, Vendedor, Gerente): ").title()

if cargo == "Caixa":
    salario_bruto = 1500.00
elif cargo == "Vendedor":
    salario_bruto = 2400.00
elif cargo == "Gerente":
    salario_bruto = 4000.00
else: 
    salario_bruto = 0.00
    print("Cargo inválido! Não trabalha aqui.")

# 3. Cálculo de desconto e salário líquidos (Apenas se o cargo for válido)
if salario_bruto > 0:
    # Cálculo do INSS (FIXO EM 12%)
    desconto_inss = salario_bruto * 0.12

    # Cálculo do IRRF (Depende do valor do salário Bruto)
    if salario_bruto > 2000.00:
        desconto_irrf = salario_bruto * 0.14
    else:
        desconto_irrf = salario_bruto * 0.08

    # Cálculo do Salário Líquido
    salario_liquido = salario_bruto - desconto_inss - desconto_irrf

    # 4. Saída de dados formatada (Colocada dentro do IF)
    print("\n" + "="*30)
    print("FOLHA DE PAGAMENTO")
    print("="*30)
    print(f"Salário Bruto:   R$ {salario_bruto:>8.2f}")
    print(f"Desconto INSS:   R$ {desconto_inss:>8.2f}")
    print(f"Desconto IRRF:   R$ {desconto_irrf:>8.2f}")
    print("-"*30)
    print(f"Salário Líquido: R$ {salario_liquido:>8.2f}")
    print("="*30)
    