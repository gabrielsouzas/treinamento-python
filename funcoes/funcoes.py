# Funções sem argumentos


def rocket_parts():
    print("payload, propellant, structure")


rocket_parts()


def rocket_parts():
    return "payload, propellant, structure"


output = rocket_parts()

print(output)

# Argumentos necessários e opcionais

# Um exemplo de função interna que requer argumento é any(). Essa função usa um objeto iterável (por exemplo, uma lista) e retorna True se algum item do objeto iterável for igual a True. Caso contrário, ele retornará False.

print(any([True, False, False]))

print(any([False, False, False]))

# Usar argumentos de função no Python


def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"


out = distance_from_earth("Moon")

print(out)

# Vários argumentos obrigatórios


def days_to_complete(distance, speed):
    hours = distance / speed
    return hours / 24


print(days_to_complete(238855, 75))

# Funções como argumentos

total_days = days_to_complete(238855, 75)
round(total_days)

round(days_to_complete(238855, 75))
