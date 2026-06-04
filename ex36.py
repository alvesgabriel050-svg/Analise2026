nome=""
while nome != "SAIR":
    nome=input("Digite um nome").upper()
    if nome == "SAIR":
        print("Programa encerrado! Sextou!")
        break
print(f"O nome digitado foi {nome}")
    