def main():
    try:
        configuration = open("config.txt")
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == "__main__":
    main()

# Nesse exemplo ele pede para criar um diretório com o nome de config.txt, para que ao chamar o método open ele de o seguinte erro:
# Traceback (most recent call last):
#   File "/tmp/config.py", line 9, in <module>
#     main()
#   File "/tmp/config.py", line 3, in main
#     configuration = open('config.txt')
# IsADirectoryError: [Errno 21] Is a # directory: 'config.txt'

# Correção para qualquer tipo de exceção


def main():
    try:
        configuration = open("config.txt")
    except Exception:
        print("Couldn't find the config.txt file!")


# O problema agora é que a mensagem de erro está incorreta. O diretório existe, mas tem permissões diferentes e o Python não pode lê-lo


# Tratar erro de permissão/diretorio e de arquivo não encontrado


def main():
    try:
        configuration = open("config.txt")
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")


# Agrupamento  de exceções


def main():
    try:
        configuration = open("config.txt")
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")


# Imprimir erro

try:
    open("mars.jpg")
except FileNotFoundError as err:
    print("Got a problem trying to read the file:", err)


# Diferenciando exceções pelo código do erro

try:
    open("config.txt")
except OSError as err:
    if err.errno == 2:
        print("Couldn't find the config.txt file!")
    elif err.errno == 13:
        print("Found config.txt but couldn't read it")
