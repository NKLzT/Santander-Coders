idade = input("Digite sua idade")
print(idade, type(idade))
idade = int(idade)
print(idade, type(idade))
salario_mensal = input('Digite o seu salario mensal: ')
salario_mensal = float(salario_mensal)

gasto_mensal = input('Digite o seu gasto mensal em media: ')
gasto_mensal = float(gasto_mensal)

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

montate_economizado = salario_total - gasto_total 
print("O montante que voce pode economizar e de " , montate_economizado)