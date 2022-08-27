def main(list1,n):
    """
    A list of several elements is given. Return all items from the beginning in n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    # if n > 0:
    #    k = list1[n:]
    # else:
    #     k = list1[n::-1]
    # return k


    # if n > 0:
    #     k = list1[-1::-n]
    # else:
    #     k = list1[0::-n]
    # return k

    if n > 0:
        k = list1[0::n]
    else:
        k = list1[-1::n]
    return k
    
x=main(['a', 'b', 'c'], 2)
print(x)