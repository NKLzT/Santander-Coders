#NOT = inverte o valor logico de um impressão.
#AND = Compor duas impressoes logicas só sera True se ambas as impressoes forem verdadeiras.
#OR = Resuta em True se no minimo uma das impressoes forem verdadeiras e sera falso só quando ambas forem falsas.

x = 50
y = 2
print(x ** y) # ** representa exponenciasão aqui seria X elevado a Y.
print(x // y) # // representa a divisão inteira o valor será necessariamente inteiro. (ignora o valor decimal da divisão)
print(x % y) # divide dois valores e pega o resto da divisão desses dois numeros

tem_cafe = True
tem_pao = False
print(not tem_cafe)
print(tem_cafe or tem_pao)
print(tem_cafe and tem_pao)
