from collections import defaultdict, Counter


class Cookbook:
    pass


def create_count_mapping(cookbooks: list[Cookbook]):
    """
    Exercise from page 35
    :param cookbooks:
    :return:
    """
    counter = defaultdict(lambda: 0)
    for cookbook in cookbooks:
        counter[cookbook.author]
    return counter


def create_author_mapping(cookbooks: list[Cookbook]):
    """
    Exercise from page 35
    :param cookbooks:
    :return:
    """
    return Counter(book.author for book in cookbooks)
