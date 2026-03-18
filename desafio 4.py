# Função para somar
def somar(a, b):
    return a + b

# Função para subtrair
def subtrair(a, b):
    return a - b

# Função para multiplicar
def multiplicar(a, b):
    return a * b

# Função para dividir
def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    else:
        return a / b

# Função principal que recebe a operação
def calculadora():
    print("Escolha uma operação:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    
    # Solicita a operação escolhida
    operacao = input("Digite o número da operação desejada (1/2/3/4): ")

    # Solicita os números para operar
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Verifica a operação escolhida e executa
    if operacao == '1':
        print(f"{num1} + {num2} = {somar(num1, num2)}")
    elif operacao == '2':
        print(f"{num1} - {num2} = {subtrair(num1, num2)}")
    elif operacao == '3':
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif operacao == '4':
        print(f"{num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Operação inválida!")

# Chama a função principal
calculadora()
