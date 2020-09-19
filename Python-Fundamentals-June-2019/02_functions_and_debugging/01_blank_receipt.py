def print_receipt_header():
    """
    Prints the receipt header
    :return: None
    """
    print('CASH RECEIPT')
    print('------------------------------')


def print_receipt_body():
    """
    Prints the receipt body
    :return: None
    """
    print('Charged to____________________')
    print('Received by___________________')


def print_receipt_footer():
    """
    Prints the receipt footer
    :return: None
    """
    print('------------------------------')
    print('\u00A9 SoftUni')


def print_receipt():
    """
    Prints a blank receipt
    :return: None
    """
    print_receipt_header()
    print_receipt_body()
    print_receipt_footer()


if __name__ == '__main__':
    print_receipt()