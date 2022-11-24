x1 = int(input("digite o primeiro numero: "))
x2 = int(input("digite o segundonumero: "))
x3 = int(input("digite o terceiro numero: "))
x4 = int(input("digite o quarto numero: "))
x5 = int(input("digite o quinto numero: "))
x6 = int(input("digite o sexto numero: "))
l1 = [x1, x2, x3,x4, x5, x6]
l2 = [l1[0]+l1[3],l1[1]+l1[4],l1[2]+l1[5]]
print("o resultado e: {}".format(l2))