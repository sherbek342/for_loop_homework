def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    l =[]
    B +=1
    for i in range(B):
        l.append(i)
    return l[A:B]
print(main(A=5,B=9))