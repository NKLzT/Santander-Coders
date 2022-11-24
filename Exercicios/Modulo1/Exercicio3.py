Suspeito = int(input("Mora perto da vítima? 1 pra sim 0 pra não: "))
Suspeito += int(input("Já trabalhou com a vítima? 1 pra sim 0 pra não: "))
Suspeito += int(input("Telefonou para a vítima? 1 pra sim 0 pra não: "))
Suspeito += int(input("Esteve no local do crime? 1 pra sim 0 pra não: "))
Suspeito += int(input("Devia para a vítima? 1 pra sim 0 pra não: "))

if(Suspeito== 5):{
    print("Voce e o assasino")
}
elif(Suspeito == 4 or Suspeito == 3):{
    print("Voce e um cúmplice")
}
elif(Suspeito== 2):{
    print("Voce e suspeito")
}
elif(Suspeito <= 1):{
    print("Voce foi liberado")
}
else:{
    print("ERRO VOCE ESTA MENTINDO PARA O PROGRAMA OU COLOCOU DADOS INCORRETOS1")
}
