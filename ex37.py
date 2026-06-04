senha_correta = "python123"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    tentativa = input(f"Digite a senha (Tentativa {tentativas+1}/{max_tentativas}): ")
    
    if tentativa == senha_correta:
        print("Acesso concedido! Bem vindo!")
        break
    else:
        # Estas duas linhas precisam de um "tab" (espaçamento) 
        # para o Python entender que fazem parte do "else"
        print("Senha incorreta.")
        tentativas += 1

# O else do while continua no mesmo nível de alinhamento do while
else:
    print("Você excedeu o número máximo de tentativas. Acesso bloqueado")
    