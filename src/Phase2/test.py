import re


def main():
    d = set()
    with open("recsOut.txt", "r") as ans, open("test.txt", "r") as terms:
        print(set(ans.read()) - set(terms.read()))





if __name__ == '__main__':
    main()
