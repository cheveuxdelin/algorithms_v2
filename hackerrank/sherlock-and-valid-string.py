from collections import Counter


def isValid(s):
    c = Counter(s)
    values = sorted(c.values())

    if len(values) == 1:
        return "YES"

    first = values[0]
    second = values[1]
    last = values[-1]
    second_last = values[-2]

    if (first == last) or \
            (first == 1 and second == last) or \
            (last - 1 == second_last and first == second_last):
        return "YES"

    return "NO"
