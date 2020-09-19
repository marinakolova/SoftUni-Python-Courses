class Website:

    def __init__(self, host, domain, queries):
        self.host = host
        self.domain = domain
        self.queries = queries

    def __str__(self):
        result = f'https://www.{self.host}.{self.domain}'
        if self.queries:
            result += '/query?='
            result += '&'.join([f'[{q}]' for q in self.queries])
        return result


if __name__ == '__main__':
    websites = []

    while True:
        inp = input()
        if inp == 'end':
            for website in websites:
                print(website)
            break

        inp = inp.split(' | ')
        host = inp[0]
        domain = inp[1]
        queries = inp[2].split(',') if len(inp) == 3 else []
        websites.append(Website(host, domain, queries))
