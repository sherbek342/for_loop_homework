def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    list = price
    l=[]
    for i in range(10):
        l.append(price)
        price = list+price
    return l
print(main(price=2.25))