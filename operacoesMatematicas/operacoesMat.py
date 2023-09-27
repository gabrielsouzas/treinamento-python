answer = 30 + 12
print(f"Adição: {answer}")

difference = 30 - 12
print(f"Subtração: {difference}")

product = 30 * 12
print(f"Multiplicação: {product}")

quotient = 30 / 12
print(f"Divisão: {quotient}")

seconds = 1042
# Arredondar para baixo usando a função piso. Para executar a função piso no Python, use //.
display_minutes = 1042 // 60
# Para encontrar o resto, use o operador de módulo que está em %
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)

# Ordem das operações

# 1. Parênteses
# 2. Exponentes
# 3. Multiplicação e divisão
# 4. Adição e subtração

result_2 = 1032 + (26 * 2)
print(result_2)

# Exercicio - Descobrir a distancia entre dois planetas pelas suas distancias até o sol

first_planet = 149597870
second_planet = 778547200

distance_km = second_planet - first_planet
print(distance_km)

distance_mi = distance_km / 1.609344
print(distance_mi)
