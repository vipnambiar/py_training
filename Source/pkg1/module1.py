import pkg2.module2 as md2


def add():
    md2.hello(__name__)
    first_val = raw_input("Enter first val:")
    second_val = raw_input("Enter second val:")
    return int(first_val) + int(second_val)
