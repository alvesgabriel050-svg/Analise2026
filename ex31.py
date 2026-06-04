num = int(input("Digite um número para ver a sua tabuada"))
print(f"tabuada de {num}")
i = 1
while i < 11:
    resultado = num * i
    print("=" * 10)   
    print(f"{num} x {i} = {resultado}")
    print("=" * 10)   
    i = i + 1 