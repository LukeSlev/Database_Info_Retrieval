import bsddb3, sys, re
import termSearch
import yearInBetween, yearGreater, yearLess

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
    return yearinBetween.yearSearch(starting_year, ending_year)

def yearsGreater(starting_year):
    return yearGreater.yearSearch(starting_year)

def yearsLess(ending_year):
    return yearLess.yearSearch(ending_year)

def titeEqualTo(title):
    return termSearch.termSearch('t-' + title)

def authorEqualTo(author):
    return termSearch.termSearch('a-' + title)

def otherEqualTo(other):
    return termSearch.termSearch('o-' + title)

def joinQueries():
    pass


def main():
    for line in sys.stdin:
        parseQuery(line)

if __name__ == '__main__':
    main()
