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
