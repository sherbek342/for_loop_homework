def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    list = ""
    for i in range(n):
        list = list + str(i)+","

    return list.strip(",")
print(main(5))