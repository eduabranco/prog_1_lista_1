from operator import irshift


rend=float(input("Rendimento por hora, em reais: R$"))
time=float(input("Horas totais no mês: "))

salario_bruto=rend*time

ir=salario_bruto*0.11
print(f"IR: R${ir:.2f}")

inss=salario_bruto*0.08
print(f"INSS: R${inss:.2f}")

sindicato=salario_bruto*0.05
print(f"Sindicato: R${sindicato:.2f}")

descontos=ir+inss+sindicato
salario_liquido=salario_bruto-descontos

print(f"Com impostos, seu salário bruto de R${salario_bruto:.2f} será de R${salario_liquido:.2f} no mês.")

input("Aperte [ENTER] para sair. ")