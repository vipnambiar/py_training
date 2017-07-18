import sys
from pkg1 import module1


def hello():
    print "namespace:", __name__


if __name__ == '__main__':
    hello()