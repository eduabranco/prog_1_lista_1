tamanho=float(input("Tamanho em Metros Quadrados: "))
tamanho*=1.1
ltudo=llatas=lgaloes=tamanho/6
latas=galoes=tgaloes=tlatas=0

while llatas>0:
    llatas-=18
    latas+=1
while lgaloes>0:
    lgaloes-=3.6
    galoes+=1
while ltudo>0:
    ltudo-=18
    tlatas+=1
    while ltudo<=10.8 and ltudo>0:
        ltudo-=3.6
        tgaloes+=1
    
latasprice=latas*80.00
galoesprice=galoes*25.00
tlatasprice=tlatas*80.00
tgaloesprice=tgaloes*25

print(f"Você poderá comprar {latas} latas de 18L, que custarão R${latasprice:.2f}.\nTambém, poderá comprar {galoes} galões de 3.6L, custando R${galoesprice:.2f}.\nOu támbém poderá comprar {tlatas} e {tgaloes} galões que juntos custarão um total de R${(tlatasprice+tgaloesprice):.2f}")
input("Aperte [ENTER] para sair. ")