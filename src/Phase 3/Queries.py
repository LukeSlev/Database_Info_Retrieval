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
        
        it = re.finditer(expression, query)
        for m in it:
            exp=query[m.start():m.end()]
        
            if re.match(yearQuery,exp):
                parseYearSearch(exp)
                return
					
            if re.match(termQuery,exp):
                parseQuerySearch(exp)
                return
					
            if re.match(termQuery,exp):
                parsePhraseSearch(exp)
                return
      
            
    else:
        print("\nincorrect query\n")

	
	
def parseYearSearch(exp):
	for m in re.finditer("<", exp):
		yearsLess(exp[m.start()+1:])

def parseQuerySearch(exp):
	pass

def parsePhraseSearch(exp):
	pass

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

def substringEqualTo(typ, substring):
    ret = set()
    subList = substring.split()
    if typ == "author":
        for word in subList:
            authorEqualTo(word)
    elif typ == "title":
        for word in subList:
            titleEqualTo(word)
    else:
        for word in subList:
            otherEqualTo(word)

def joinQueries():
    pass


def main():
    for line in sys.stdin:
        parseQuery(line)

if __name__ == '__main__':
    main()
