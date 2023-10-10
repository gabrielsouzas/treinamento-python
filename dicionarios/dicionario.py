planet = {"name": "Earth", "moons": 1}

print(planet.get("name"))


# planet['name'] is identical to using planet.get('name')
print(planet["name"])

wibble = planet.get("wibble")  # Returns None
# wibble = planet["wibble"]  # Throws KeyError

# Modificar valores do dicionário

# No output: name is now set to Makemake.
planet.update({"name": "Makemake"})

print(planet.get("name"))

planet["name"] = "Makemakemake"

print(planet.get("name"))


# Percorrer dicionarios por chaves

rainfall = {"october": 3.5, "november": 4.2, "december": 2.1}

for key in rainfall.keys():
    print(f"{key}: {rainfall[key]}cm")


# Determinar se uma chave existe em um dicionário

if "december" in rainfall:
    rainfall["december"] = rainfall["december"] + 1
else:
    rainfall["december"] = 1

# Because december exists, the value will be 3.1


# Recuperar todos os valores

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f"There was {total_rainfall}cm in the last quarter.")
