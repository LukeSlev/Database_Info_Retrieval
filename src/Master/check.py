import re


def main():
    d = set()
    with open("answer-long.txt", "r") as ans, open("recs.txt", "r") as terms:
        for line in ans:
            d.add(line)
        for lines in terms:
            if lines not in d:
                print(lines)





if __name__ == '__main__':
    main()