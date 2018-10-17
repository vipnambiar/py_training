import sys

d = {}

for score in range(90,101):
    d[score] = 'A'

for score in range(80, 90):
    d[score] = 'B'

for score in range(70, 80):
    d[score] = 'C'

for score in range(60, 70):
    d[score] = 'D'

def main():
        while True:
            score = raw_input("Enter a score: ")
            try:
                score = int(score)
            except Exception:
                print "Not a valid score, please enter a number between 1-100"
                continue
            else:
                print "Your score is : %s"  % d.get(score, 'F')

if __name__ == '__main__':
    try:
        main()
    except:
        print "Exiting..."
        sys.exit(0)
