while True:
    try:
        peso_de_peixes=float(input("Peso total (kg): "))
        break
    except ValueError:
        print("Somente números, por favor.")
if peso_de_peixes>51:
    excesso=int(peso_de_peixes)-50
    multa=excesso*4.00
    print(f"Você pescou {peso_de_peixes}kg. Portanto, você deve pagar uma multa de R${multa}.")
    input("Aperte [ENTER] para sair. ")
else: 
    print("Não será necessário pagar multa.")
    input("Aperte [ENTER] para sair. ")
