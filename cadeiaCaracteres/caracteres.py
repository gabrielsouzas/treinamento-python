# Cadeia simples de caracteres
fact = "The Moon has no atmosphere."
print(fact)

# Imprimir uma cadeia sem concatenar
print(fact + "No sound can be heard on the Moon.")

# Concatenar uma cadeia de caracteres em uma nova cadeia
two_facts = fact + "No sound can be heard on the Moon."
print(two_facts)

# Colocar aspas simples ou duplas entre caracteres
print(
    """We only see about 60% of the Moon's surface, this is known as the "near side"."""
)

# Pular linhas
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

# Pular linhas (NÂO FUNCIONA)
multilineB = """Facts about the Moon: There is no atmosphere. There is no sound."""
print(multilineB)

# Primeira letra de cada palavra em maiusculo
print("temperatures and facts about the moon".title())

heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)

# Dividir uma cadeia de caracteres
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)

# Pesquisar em uma cadeia de caracteres
print("Moon" in "This text will describe facts and challenges with space travel")
# SAIDA: FALSE

print("Moon" in "This text will describe facts about the Moon")
# SAIDA: TRUE

# encontrar o indice da palavra em uma cadeia de caracteres
temperaturesB = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperaturesB.find("Moon"))
# SAIDA: -1 (INDICA QUE A PALAVRA NÃO FOI ENCONTRADA)

print(temperaturesB.find("Mars"))
# SAIDA: 64 (IMPRIME A POSIÇÃO QUE A PALAVRA APARECE NA CADEIA)

# Contar quantas vezes uma palavra aparece
print(temperaturesB.count("Mars"))
print(temperaturesB.count("Moon"))

# Transformar em minusculas e maiusculas
print("The Moon And The Earth".lower())
print("The Moon And The Earth".upper())

# Verificações
temperaturesC = "Mars Average Temperature: -60 C"
parts = temperaturesC.split(":")
print(parts)
# Usar o [-1] para retornar o último item em uma lista
print(parts[-1])

# Verificar se há numeriais na cadeia de caracteres
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

# Validar se um caractere está no começo ou no fim da cadeia
print("-60".startswith("-"))

if "30 C".endswith("C"):
    print("This temperature is in Celsius")

# Substituição de caracteres
print(
    "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace(
        "Celsius", "C"
    )
)

# Verificar um texto na cadeia com lower
text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())

# Concatenar listas
moon_facts = [
    "The Moon is drifting away from the Earth.",
    "On average, the Moon is moving about 4cm every year.",
]
print(" ".join(moon_facts))
