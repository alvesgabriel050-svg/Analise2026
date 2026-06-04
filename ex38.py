while True:
    try:
        # Usamos float em vez de int para permitir notas quebradas (ex: 8.5)
        nota = float(input("Digite uma nota entre 0 e 10: "))
        
        # O Python permite encadear comparações dessa forma elegante:
        if 0 <= nota <= 10:
            # Se a nota for válida, saímos do loop
            print(f"Nota válida registrada: {nota}")
            break 
        else:
            # Se for um número, mas fora do limite (ex: 11 ou -2)
            print("Valor incorreto! A nota precisa estar entre 0 e 10.")
            
    except ValueError:
        # Se a pessoa digitar uma letra ou símbolo
        print("Entrada inválida. Por favor, digite um número.")