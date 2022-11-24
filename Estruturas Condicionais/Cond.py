valor_passagem = 5
valor_corrida = input('Qual o valor da corrida')

if float(valor_corrida) <= valor_passagem * 5:
    print('Pague a corrida')
elif float(valor_corrida) <= valor_passagem * 6:
    print("Aguarde um momento, o valor pode abaixar")
else:
    print('Pegue o ônibus')
