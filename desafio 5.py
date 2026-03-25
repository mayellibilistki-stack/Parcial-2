# Primeira função é para calcular a área de um triângulo.
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Essa é a função pincipal de todas
def main():
    print("Cálcular a área de um triângulo")
    
    # Após tudo isso, é preciso solicitar a base e altura do triângulo
    base = float(input("Digite aqui qual é o valor da base do triângulo: "))
    altura = float(input("Digite o valor da altura do triângulo que você deseja medir: "))
    
    # Depois, vem a forma que vai ser usado para calcular a área
    area = calcular_area_triangulo(base, altura)
    
    # E por fim mostra o resultado final
    print(f"A área do triângulo com base {base} e altura {altura} é: {area}")

# Vai chamar a função principal
main()
