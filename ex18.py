diaaula= input("Qual dia da semana atual?")
#horafim = hora que a aula foi finalizada
horafim = float(input("Digite a hora que a Aula foi finalizada, utilize o formato de 24 horas"))
if diaaula== "sexta" and horafim == 21:
    print("Sextou! Você merece 1 refrigerante!")
elif diaaula == "sexta" and horafim == 22:
    print("Sextou! Você merece 2 refrigerantes")
else:
    print("Ainda não sextou, não saia da rotina. Vá estudar!")

