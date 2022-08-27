def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    k = list1
    k2 = list1[-1::-1]
    return k + k2
x=main(['a', 'b', 'c', 'd'])
print(x)