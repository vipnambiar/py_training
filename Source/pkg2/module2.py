import sys
from pkg1 import module1 as md


def hello():
    md.add()
    print "namespace:", __name__


if __name__ == '__main__':
    args = sys.argv
    hello()
