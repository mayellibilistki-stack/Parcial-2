# A função para calcular a área de um triângulo é:
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# A principal função
def main():
    print("Cálculo da área de um triângulo")
    
    # Depois disso, solicita a base e altura do triângulo
    base = float(input("Digite o valor da base do triângulo: "))
    altura = float(input("Digite o valor da altura do triângulo: "))
    
    # Forma de calcular a área
    area = calcular_area_triangulo(base, altura)
    
    # Por último exibe o resultado
    print(f"A área do triângulo com base {base} e altura {altura} é: {area}")

# Chama a função principal
main()
