from typing import Iterable


def merge_two_arrays(n: list[int], m: list[int]) -> Iterable[int]:
    i = j = 0
    count1, count2 = len(n), len(m)

    while i < count1 and j < count2:
        if n[i] < m[j]:
            yield n[i]
            i += 1
        else:
            yield m[j]
            j += 1

    while i < count1:
        yield n[i]
        i += 1

    while j < count2:
        yield m[j]
        j += 1


print(merge_two_arrays([4, 5], [3]))
