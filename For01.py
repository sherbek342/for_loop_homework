import py_compile


def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    list = []
    for i in range(n):
        list.append(i)
    return list
print(main(5))