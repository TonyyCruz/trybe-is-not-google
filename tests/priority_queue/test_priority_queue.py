import pytest
from ting_file_management.priority_queue import PriorityQueue


mock_priority_data_three = {
    "nome_do_arquivo": "arquivo_priority.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": ["a", "b", "c"]
}

mock_priority_data_four = {
    "nome_do_arquivo": "arquivo_priority.txt",
    "qtd_linhas": 4,
    "linhas_do_arquivo": ["a", "b", "c", "d"]
}

mock_common_data = {
    "nome_do_arquivo": "arquivo_common.txt",
    "qtd_linhas": 6,
    "linhas_do_arquivo": ["a", "b", "c", "d", "e", "f"]
}


def test_basic_priority_queueing():
    priorityQueue = PriorityQueue()
    priorityQueue.enqueue(mock_common_data)
    priorityQueue.enqueue(mock_common_data)
    priorityQueue.enqueue(mock_priority_data_four)
    priorityQueue.enqueue(mock_common_data)
    priorityQueue.enqueue(mock_priority_data_three)

    assert priorityQueue.search(0) == mock_priority_data_four
    assert priorityQueue.search(1) == mock_priority_data_three
    assert priorityQueue.search(2) == mock_common_data
    assert priorityQueue.__len__() == 5

    with pytest.raises(IndexError, match="Invalid index"):
        priorityQueue.search(5)

    assert priorityQueue.dequeue() == mock_priority_data_four
    assert priorityQueue.dequeue() == mock_priority_data_three
    assert priorityQueue.dequeue() == mock_common_data
