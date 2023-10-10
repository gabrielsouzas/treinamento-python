# Exercicio 01

planet = {"name": "Mars", "moons": 2}

print(f"{planet.get('name')} has {planet.get('moons')} moon(s)")

planet["circumferences (km)"] = {"polar": 6752, "equatorial": 6792}

print(
    f'{planet["name"]} has a polar circumference of {planet["circumferences (km)"]["polar"]}'
)

# Exercicio 2

planet_moons = {
    "mercury": 0,
    "venus": 0,
    "earth": 1,
    "mars": 2,
    "jupiter": 79,
    "saturn": 82,
    "uranus": 27,
    "neptune": 14,
    "pluto": 5,
    "haumea": 2,
    "makemake": 1,
    "eris": 1,
}

planet_moons.pop("eris")

moons = planet_moons.values()
total_planets = len(planet_moons.keys())

print(f"There was {moons} moons. In {total_planets} planets!")

total_moons = 0
for value in planet_moons.values():
    total_moons = total_moons + value

average_moons = total_moons / total_planets

print(f"Each planet has an average of {average_moons} moons")
