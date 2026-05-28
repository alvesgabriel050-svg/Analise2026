temperatura= float(input("Qual a temperatura do dia?"))
if temperatura >= 0 and temperatura <= 18:
    print(f"Está FRIO: {temperatura}°")
elif temperatura >= 18 and temperatura <= 30:
    print(f"A temperatura está agradavel:{temperatura}°")
else:
    print (f"Está Calor:{temperatura}°")
   
    