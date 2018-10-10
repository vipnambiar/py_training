from pkg1 import module1 as md1
from pkg2.module2 import hello
# from pkg2 import module3


def bar():
    hello(__name__)
    print md1.add()

if __name__ == '__main__':
    bar()
