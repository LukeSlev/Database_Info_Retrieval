import re


def main():
    d = set()
    with open("recsOut.txt", "r") as ans, open("t.txt", "r") as terms:
        for line in terms:
            d.add(line)
        for lines in ans:
            if lines not in d:
                print(lines)





if __name__ == '__main__':
    main()
