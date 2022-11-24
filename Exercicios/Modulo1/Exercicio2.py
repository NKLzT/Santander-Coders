idade = int(input("Qual sua idade?"))
while ( idade > 150 or idade < 0 ):
	idade=int(input("informe a idade--> "))

salario=float(input("informe um salário--> "))
while ( salario < 0 ):
	salario=float(input("informe um salário--> "))

sexo=str(input("informe a inicial do seu sexo--> "))
while  sexo !="f" and sexo!="m" :
	sexo=str(input("informe a inicial do seu sexo--> "))