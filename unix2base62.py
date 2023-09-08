from string import digits, ascii_uppercase, ascii_lowercase


# every character except the dash (-) is allowed as a digit
DIGITS = tuple(digits + ascii_uppercase + ascii_lowercase)
DIGITS_TO_DECIMAL = dict((c, i) for i, c in enumerate(DIGITS))
BASE = len(DIGITS)


def base_decode(string, base=BASE, digits_to_decimal=DIGITS_TO_DECIMAL):
    factor = 1
    if string.startswith("-"):
        string = string[1:]
        factor = -1

    number = 0
    for c in string:
        number = number * base + digits_to_decimal[c]

    return factor * number


def base_encode(number, base=BASE, digits=DIGITS):
    if not number:
        return digits[0]

    prefix = ""
    if number < 0:
        prefix = "-"
        number = abs(number)

    string = ""
    while number:
        number, rem = divmod(number, base)
        string = digits[rem] + string

    return prefix + string


def unix2base62():
    import time
    ms = int( time.time() )
    return base_encode(ms)


def timename():
    return unix2base62()
