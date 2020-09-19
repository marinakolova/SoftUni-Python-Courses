class BankAccount:

    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance

    def __str__(self):
        return f"{self.name} -> {self.balance:.2f} ({self.bank})"


if __name__ == '__main__':
    accounts = []
    while True:
        inp = input()
        if inp == 'end':
            break

        inp = inp.split(' | ')
        bank = inp[0]
        account_name = inp[1]
        balance = float(inp[2])
        accounts.append(BankAccount(account_name, bank, balance))

    accounts = sorted(accounts, key=lambda x: (x.balance, -len(x.bank)), reverse=True)
    for a in accounts:
        print(a)
