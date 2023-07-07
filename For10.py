def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    list=[]
    for i in range(len(list1)):
        list.append(list1[i].capitalize())
    return list
print(main(list1 = ['rustam', 'diyor', 'alisher', 'bektosh']))