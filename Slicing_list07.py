def main(list1,n):
    """
    A list of several elements is given. Return all items from the beginning in n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    if n >= 0:
       k = list1[n:]
    else:
        k = list1[n::-1]
    return k

x=main(['a', 'b', 'c', 'd', 'e', 'f'], -1)
print(x)