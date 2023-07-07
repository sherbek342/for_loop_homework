def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    l = []
    summ = 0
    for i in range(A,B):
        l.append(i)
        summ = summ +i
    return summ
print(main(A=3,B=6))