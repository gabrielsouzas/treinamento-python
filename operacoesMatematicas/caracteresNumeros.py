demo_int = int("215")
print(demo_int)

demo_float = float("215.3")
print(demo_float)


# Converter um número para valor absoluto, que é um numero não negativo usando a função abs

print(abs(39 - 16))
print(abs(16 - 39))

# Arredondamento: arredondar o valor para o próximo inteiro acima, se o valor decimal for maior que .5, ou abaixo, se o valor decimal for inferior ou igual a .5.

print(round(14.5))


# Biblioteca de matemática Math

# Arredondar o número inteiro mais próximo para cima com ceil, ou para baixo com floor

from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

# Exercicio

first_planet_input = input("Enter the distance from the sun for the first planet in km")
second_planet_input = input(
    "Enter the distance from the sun for the second planet in km"
)

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

distance_km = first_planet - second_planet
print(abs(distance_km))
