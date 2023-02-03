import sys
from .file_management import txt_importer


def process(path_file, instance):
    for i in range(instance.__len__()):
        dict_from_queue = instance.search(i)
        if dict_from_queue["nome_do_arquivo"] == path_file:
            return

    text_list = txt_importer(path_file)
    new_dict_for_queue = {
      "nome_do_arquivo": path_file,
      "qtd_linhas": len(text_list),
      "linhas_do_arquivo": text_list
    }

    instance.enqueue(new_dict_for_queue)
    print(new_dict_for_queue, file=sys.stdout)


def remove(instance):
    removed_data = instance.dequeue()

    if removed_data is None:
        print("Não há elementos", file=sys.stdout)

    else:
        removed_path_name = removed_data["nome_do_arquivo"]

        print(
            f"Arquivo {removed_path_name} removido com sucesso",
            file=sys.stdout
        )


def file_metadata(instance, position):
    if position >= instance.__len__():
        print("Posição inválida", file=sys.stderr)
    else:
        file_data = instance.search(position)
        print(file_data, file=sys.stdout)
