def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    l =[]
    B+=1
    A-=1
    for i in range(B):
        l.append(i)
    return l[B:A:-1]