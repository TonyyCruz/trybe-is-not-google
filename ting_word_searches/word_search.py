def exists_word(word, instance):
    response = list()

    for idx in range(instance.__len__()):
        queue_data = instance.search(idx)
        words_found_dict = {
            "palavra": word,
            "arquivo": queue_data["nome_do_arquivo"],
            "ocorrencias": []
        }

        for position, string in enumerate(queue_data["linhas_do_arquivo"]):
            if word.lower() in string.lower():
                words_found_dict["ocorrencias"].append({"linha": position + 1})
        if len(words_found_dict["ocorrencias"]):
            response.append(words_found_dict)
    return response


def find_word_in_list(word, string_list):
    response = list()
    for position, string in enumerate(string_list):
        if word.lower() in string.lower():
            response.append({
                "linha": position + 1,
                "conteudo": string
            })
    return response


def search_by_word(word, instance):
    response = list()

    for idx in range(instance.__len__()):
        queue_data = instance.search(idx)
        occurrences = find_word_in_list(word, queue_data["linhas_do_arquivo"])
        words_found_dict = {
            "palavra": word,
            "arquivo": queue_data["nome_do_arquivo"],
            "ocorrencias": occurrences
        }

        if len(words_found_dict["ocorrencias"]):
            response.append(words_found_dict)
    return response
