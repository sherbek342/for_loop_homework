def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    num = 1
    l = [1]
    res = 0
    for i in range(N):
        if i > 0:
            l.append(num/i)
    for i in range(len(l)):
        res = res+l[i]
    return res
print(main(4))