# Criar uma lista
planets = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

# Alterar uma lista
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

print(planets)

# Para obter o comprimento de uma lista, use a função interna len()
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

# Para adicionar um item a uma lista, use o método .append(value)
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")
print(planets)

# Você pode remover o último item de uma lista chamando o método .pop()
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

# Os índices negativos começam ao final da lista e funcionam de maneira retroativa. No exemplo a seguir, o índice -1 retorna o último item da lista

print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# Para determinar em que local da lista um valor está armazenado, use o método index sobre a lista

jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")
