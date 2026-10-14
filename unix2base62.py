from string import digits, ascii_uppercase, ascii_lowercase
from time import time

D = digits + ascii_uppercase + ascii_lowercase
B = 62


def timename():
    n = int(time())
    out = []

    while n:
        n, r = divmod(n, B)
        out.append(D[r])

    return "".join(reversed(out)) or D[0]
