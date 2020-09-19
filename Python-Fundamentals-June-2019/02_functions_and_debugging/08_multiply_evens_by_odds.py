def multiply_evens_by_odds(number):
    """
    Multiplies the sum of the even digits by the sum of the odd digits
    :param number:
    :return: int
    """
    even_sum, odd_sum = 0, 0
    for ch in number:
        if ch.isdigit():
            ch = int(ch)
            if ch % 2 == 0:
                even_sum += ch
            else:
                odd_sum += ch
    return even_sum * odd_sum


if __name__ == '__main__':
    n = input()
    print(multiply_evens_by_odds(n))
