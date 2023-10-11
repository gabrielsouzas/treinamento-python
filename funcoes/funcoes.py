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

# Usar argumentos de palavra-chave no Python

from datetime import timedelta, datetime


def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")


print(arrival_time())
print(arrival_time(2))

# Combinação de argumentos comuns e argumentos de palavra-chave


def arrival_time_1(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")


print(arrival_time_1("Moon"))
print(arrival_time_1("Orbit", hours=0.13))

# Número variável de argumentos

# A sintaxe para usar um número variável de argumentos é inserir como prefixo um asterisco (*) antes do nome do argumento


def variable_length(*args):
    print(args)


# Não é necessário chamar o número variável de argumentos args. Você pode usar qualquer nome de variável válido. Embora seja comum ver *args ou *a, você deve tentar usar a mesma convenção em todo o projeto.

variable_length()
# ()
variable_length("one", "two")
# ("one", "two")
variable_length(None)
# (None,)


def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"


print(sequence_time(4, 14, 48))


# Número variável de argumentos de palavra-chave


def variable_length(**kwargs):
    print(kwargs)


variable_length(tanks=1, day="Wednesday", pilots=3)
# {"tanks": 1, "day": "Wednesday", "pilots": 3}


def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")


crew_members(
    captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins"
)
