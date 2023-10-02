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


# Armazenar números em listas

gravity_on_earth = 1.0
gravity_on_the_moon = 0.166

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

bus_weight = 124054  # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "N")

# A função max() retorna o maior número e a função min() retorna o menor número existente na lista

print(
    "The lightest a bus would be in the solar system is",
    bus_weight * min(gravity_on_planets),
    "N",
)
print(
    "The heaviest a bus would be in the solar system is",
    bus_weight * max(gravity_on_planets),
    "N",
)

# Fatiar listas

planets_before_earth = planets[0:2]
print(planets_before_earth)

planets_after_earth = planets[3:8]
print(planets_after_earth)

# Vai até o último elemento da lista
planets_after_earth = planets[3:]
print(planets_after_earth)

# Junção de listas

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Classificar listas - Para classificar uma lista, use o método .sort() sobre a lista. O Python classifica uma lista de cadeias de caracteres em ordem alfabética e uma lista de números em ordem numérica

regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Ordem reversa

regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
