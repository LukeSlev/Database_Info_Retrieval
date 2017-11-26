import bsddb3, sys, re
import termSearch, yearRangeSearch

def parseQuery(query):
    numeric="[0-9]"
    alphanumeric="[0-9a-zA-Z]"

    term=alphanumeric + "+"
    termPrefix="(title|author|other):"
    termQuery="({})?{}".format(termPrefix,term)

    year=numeric + "+"
    yearPrefix="(year:|year>|year<)"
    yearQuery="{}{}".format(yearPrefix,year)

    phrase="{}(\\s{})*".format(term,term)
    phraseQuery='({})?"{}"'.format(termPrefix,phrase)

    expression="({}|{}|{})".format(yearQuery,termQuery,phraseQuery)
    querySearch="^{}(\\s{})*$".format(expression,expression)


    # y=re.compile(yearQuery)
    # t=re.compile(termQuery)
    # p=re.compile(phraseQuery)
    #

    if re.match(querySearch,query):
        print("\ncorrect query\n")

    else:
        print("\nincorrect query\n")

    # if re.match(yearQuery,query):
    #     print("\nYEAR\n")
    #
    # if re.match(termQuery,query):
    #     print("\nTERM\n")
    #
    # if re.match(phraseQuery,query):
    #     print("\nPHRASE\n")

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
