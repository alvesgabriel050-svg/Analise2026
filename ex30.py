num= int(input("Digite um número para ver a sua tabuada"))
print(f"tabuada de {num}")
for i in range(1,11):
    resultado = num * i
    print("=" * 6)   
    print(f"{num}x{i}={resultado}")
    print("=" * 6)   
