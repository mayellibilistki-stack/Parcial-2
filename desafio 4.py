

#Código da Calculadora Simples
#'n1' e 'n2' essas variaveis foram usadas para selecionar os numeros
num1 = float(input("escolha um numero"))
num2 = float(input("escolha outro numero"))
#'operação' a pessoa seleciona a operação que vai ser usada
operação = input("escolha a operação:[soma, subtração, multiplicação, divisão]")
#'if'  coloca a escolha da operação. Desse modo, se for escolhido 'soma' rvai ser ealizarado a primeira opção
if operação == "subtração":
    print(num1-num2)
#'elif' foi usado para dizer que "se não for escolhido a soma, então pode ter sido subtração"
elif operação == "soma":
    print(num1+num2)
#'elif' foi usado para "se não for escolhido soma e nem subtração, então pode ter sido multiplicação"
elif operação == "divisão":
    print(num1/num2)
#'elif'  "se não for escolhido soma, subtração e nem multiplicação, a opção pode ser a divisão"
elif operação == "multiplicação":
    print(num1*num2)
#'else' se  nenhuma das operações acimas for escolhida, vai ser  dado a resposta "não foi possivel realizar essa função"
else:
    print("não foi possivel realizar essa função")
