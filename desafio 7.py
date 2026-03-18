# Primeira parte do trabalho é solicitar os dados ao usuário
# Usamos float() para permitir valores com vírgula (ex: 1500.50)
capital = float(input("Digite o capital (C): "))
taxa = float(input("Digite a taxa de juros (I) em porcentagem: "))
tempo = float(input("Digite o tempo (T): "))

# Aplica a fórmula: J = (C * I * T) / 100
juros = (capital * taxa * tempo) / 100

# Exibe o resultado formatado com duas casas decimais
print(f"\nCom um capital de R$ {capital:.2f}, taxa de {taxa}% e tempo {tempo},")
print(f"o valor dos juros simples será de: R$ {juros:.2f}")
