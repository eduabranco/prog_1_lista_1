tamanho=float(input("Tamanho em Metros Quadrados: "))
l=tamanho/3
latas=0
while l>0:
    l-=18
    latas+=1
price=latas*80.00
print(f"Você deverá comprar {latas} latas, que custarão R${price:.2f}")
input("Aperte [ENTER] para sair. ")