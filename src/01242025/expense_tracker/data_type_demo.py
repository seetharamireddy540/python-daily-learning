from typing import List


def process_list(number: List[int]) -> List[int]:
    """
    Docstring for process_list

    :param number: Description
    :type number: List[int]
    :return: Description
    :rtype: List[int]
    """
    return [x * 2 for x in number if x > 0]
