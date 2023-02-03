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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
