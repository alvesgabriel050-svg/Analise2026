n1=float(input("Digite o valor da sua Primeira prova"))
n2=float(input("Digite o valor da sua Segunda prova"))
media = (n1+n2)/2 
print(F"Sua média é {media}")
if media > 5:
    print(f"Parabéns você foi APROVADO!")
else: 
    print(f"Aluno em recuperação com média")
    