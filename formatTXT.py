from itertools import zip_longest


def grouper(group_size, iterable, fill_value=None):
    """grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"""
    args = [iter(iterable)] * group_size
    return zip_longest(fillvalue=fill_value, *args)


if __name__ == "__main__":
    with open("redeem.txt", 'r') as fin, open("out.txt", 'w') as fout:
        for name, desc, code, _ in grouper(4, fin.read().splitlines()):
            fout.write(f"{name}\t{code}\n")
            fout.write(f"{desc}\n")
            fout.write('\n')
