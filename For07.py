def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    l = []
    summ = 0
    for i in range(N):
        l.append(i)
        if i %2==1:
            summ = summ +i
    return summ
print(main(N=12))