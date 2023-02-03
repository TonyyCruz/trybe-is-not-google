import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file, "r") as file:
            file_data = file.read()
            file_list = file_data.split("\n")
            return file_list
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
