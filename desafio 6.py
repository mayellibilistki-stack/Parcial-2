# Aqui a pessoa vai digitar a quantidade de segundos 
total_segundos = int(input("Digite a quantidade de segundos: "))

# Vai ser realizado os cálculos
horas = total_segundos // 3600
resto_segundos = total_segundos % 3600
minutos = resto_segundos // 60
segundos_finais = resto_segundos % 60

# O final é a exibição do resultado
print(f"{total_segundos} segundos equivalem a:")
print(f"{horas}h {minutos}min {segundos_finais}s")

# Vai ser a entrada do usuário
h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))

# É realizado o cálculo: 1h = 3600s | 1min = 60s
resultado_segundos = (h * 3600) + (m * 60) + s

# É a parte da exibição do resultado
print(f"O total convertido é de {resultado_segundos} segundos.")
