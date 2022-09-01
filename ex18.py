size=float(input("Tamanho do arquivo(MB): "))
speed=float(input("Velocidade do link(Mbps): "))
tempo=(size/(speed/8))/60
print(f"Tempo de download de aproximadamente {tempo:.1f} minutos")
input("Aperte [ENTER] para sair. ")
