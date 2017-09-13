#import pkg2


def add():
    first_val = raw_input("Enter first val:")
    second_val = raw_input("Enter second val:")
    import pdb; pdb.set_trace()
    return int(first_val) + int(second_val)

if __name__ == '__main__':
    print add()
