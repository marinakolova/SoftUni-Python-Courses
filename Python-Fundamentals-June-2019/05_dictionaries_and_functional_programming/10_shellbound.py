from collections import defaultdict
from math import ceil

all_shells = defaultdict(list)

while True:
    inp = input()
    if inp == 'Aggregate':
        break

    region, shell_size = inp.split(' ')
    if shell_size not in all_shells[region]:
        all_shells[region].append(shell_size)

for region, shells in all_shells.items():
    sum_of_shells = sum([float(shell) for shell in shells])
    giant_shell = ceil(sum_of_shells - (sum_of_shells / float(len(shells))))
    print(f'{region} -> ' + ', '.join(shells) + f' ({giant_shell})')