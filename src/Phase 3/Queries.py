import bsddb3, sys, re
import termSearch, yearRangeSearch

def parseQuery(query):
    if re.search("^[a]$",query):
        print("here")

def yearsInRange(starting_year, ending_year):
    return yearSearch(starting_year, ending_year)

def yearsGreater(starting_year):
    pass

def yearsLess(ending_year):
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
