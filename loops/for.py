# Loops for com listas

from time import sleep


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

countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")

lista = [10, 20, 30, 40, 50, 60]

for indice, valor in enumerate(lista):
    print(f"índice={indice}, valor={valor}")
