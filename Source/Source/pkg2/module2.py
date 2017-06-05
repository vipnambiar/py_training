import sys

path = "D:\\Python Training\\Source"

if path not in sys.path:
    sys.path.append(path)

from pkg1.module1 import add

def main():
    print(add(5, 10))

if __name__ == '__main__':
    main()
