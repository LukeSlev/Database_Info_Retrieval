import bsddb3, sys, re
import termSearch

def parseQuery(query):
    if re.search("^[a]$",query):
        print("here")

def yearsInRange():
    pass

def titeEqualTo(title):
    return termSearch('t-' + title)

def authorEqualTo(author):
    return termSearch('a-' + title)

def otherEqualTo(other):
    return termSearch('o-' + title)

def joinQueries():
    pass


def main():
    for line in sys.stdin:
        parseQuery(line)

if __name__ == '__main__':
    main()
