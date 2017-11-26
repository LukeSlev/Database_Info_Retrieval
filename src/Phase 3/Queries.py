import bsddb3,sys,re

def parseQuery(query):
    if re.search("^[a]$",query):
        print("here")

def yearGreaterThan(year):
    pass

def yearLessThan(year):
    pass

def yearEqualTo(year):
    pass

def titeEqualTo(title):
    pass

def authorEqualTo(author):
    pass

def otherEqualTo(other):
    pass

def joinQueries():
    pass


def main():
    for line in sys.stdin:
        parseQuery(line)

if __name__ == '__main__':
    main()
