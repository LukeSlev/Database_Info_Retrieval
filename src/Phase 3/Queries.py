import bsddb3, sys, re
import termSearch
import yearGreater, yearLess, yearEqual

returnSet = set()
SHORT, FULL = range(2)
displayMode = SHORT

def parseQuery(query):
    global displayMode
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


    if re.match(querySearch,query):
        print("\ncorrect query\n")

        it = re.finditer(expression, query)
        for m in it:
            exp=query[m.start():m.end()]

            if (exp=="author" or exp=="title" or exp=="other") and m.end()<len(query)-1 and query[m.end()]==":":
                continue

            if re.match(yearQuery,exp):
                parseYearSearch(exp)
                continue

            if re.match(termQuery,exp):
                parseTermSearch(exp)
                continue

            if re.match(phraseQuery,exp):
                if m.start()!=0 and query[m.start()-1]==":":
                    if query[m.start()-2]=="e":
                        phraseTitleEqualTo(exp[1:-1])
                    elif query[m.start()-3]=="e":
                		   phraseOtherEqualTo(exp[1:-1])
                    else:
                        phraseAuthorEqualTo(exp[1:-1])
                else:
                	phraseNamelessEqualTo(exp[1:-1])
                continue

    elif re.match("output=key",query):
        displayMode=SHORT

    elif re.match("output=full",query):
        displayMode=FULL

    else:
        print("\nincorrect query\n")



def parseYearSearch(exp):
    global returnSet
    for m in re.finditer("<", exp):
        ret = yearsLess(exp[m.start()+1:])
        #print(ret)
        joinQueries(ret)
        return
    for m in re.finditer(">", exp):
        ret = yearsGreater(exp[m.start()+1:])
        #print(ret)
        joinQueries(ret)
        return

    for m in re.finditer(":", exp):
        ret = yearsEqualTo(exp[m.start()+1:])
        #print(ret)
        joinQueries(ret)
        return

def parseTermSearch(exp):
    for m in re.finditer("title:", exp):
        joinQueries(titleEqualTo(exp[m.start()+6:]))
        return

    for m in re.finditer("author:", exp):
        joinQueries(authorEqualTo(exp[m.start()+7:]))
        return

    for m in re.finditer("other:", exp):
        joinQueries(otherEqualTo(exp[m.start()+6:]))
        return

    namelessEqualTo(exp)

def yearsGreater(starting_year):
    print("years greater: ",starting_year)
    return yearGreater.yearSearch(starting_year)

def yearsLess(ending_year):
    print("years less: ",ending_year)
    return yearLess.yearSearch(ending_year)

def yearsEqualTo(year):
    print("year equal to: ",year)
    return yearEqual.yearSearch(year)

def titleEqualTo(title):
    print("title: ",title)
    return termSearch.termSearch('t-' + title)

def authorEqualTo(author):
    print("author: ",author)
    return termSearch.termSearch('a-' + author)

def otherEqualTo(other):
    print("other: ",other)
    return termSearch.termSearch('o-' + other)


def namelessEqualTo(nameless):
   print("nameless: ",nameless)
   r1=termSearch.termSearch('t-' + nameless)
   r2=termSearch.termSearch('a-' + nameless)
   r3=termSearch.termSearch('o-' + nameless)
   total=r1.union(r2).union(r3)
   joinQueries(total)

def checkPhraseOrder(typ, substring):
    global returnSet
    global displayMode
    DB_File = "re.idx"
    database = bsddb3.db.DB()
    database.set_flags(bsddb3.db.DB_DUP) #declare duplicates allowed before you create the database
    database.open(DB_File, None, bsddb3.db.DB_HASH, bsddb3.db.DB_CREATE)
    curs = database.cursor()

    for r in returnSet:
        result = curs.set(r.encode('utf-8'))
        xmlRecord = result[1].decode('utf-8')
        xmlReg = "(<{}>)([a-zA-Z0-9_ ]+)(</{}>)".format(typ,typ)  # Looks for the records
        for m in re.finiter(xmlReg, xmlRecord):
            print(xmlRecord[m.start():m.end()])


        # if (substring not in check):
        #     print(check, subtring)
        #     returnSet.remove(r)
        # else:
        #     print("not in")

    curs.close()
    database.close()





def phraseTitleEqualTo(title):
    print("ptitle: ",title)
    subList = title.split()
    for word in subList:
        joinQueries(titleEqualTo(word))
    checkPhraseOrder("title", title)

def phraseAuthorEqualTo(author):
    print("pauther: ",author)
    subList = author.split()
    for word in subList:
        joinQueries(authorEqualTo(word))
    checkPhraseOrder("author", author)

def phraseOtherEqualTo(other):
    print("pother: ",other)
    subList = other.split()
    for word in subList:
        joinQueries(otherEqualTo(word))
    checkPhraseOrder("other", other)

def phraseNamelessEqualTo(nameless):
    print("pnameless: ",nameless)
    subList = nameless.split()
    for word in subList:
        r1=titleEqualTo(word)
        r2=authorEqualTo(word)
        r3=otherEqualTo(word)
        total=r1.union(r2).union(r3)
        joinQueries(total)
    checkPhraseOrder("nameless", nameless)

def joinQueries(resultToAdd):
    global returnSet
    if len(returnSet) == 0:
        returnSet = resultToAdd
    else:
        returnSet = returnSet.intersection(resultToAdd)

def displayResults():
    global returnSet
    global displayMode
    DB_File = "re.idx"
    database = bsddb3.db.DB()
    database.set_flags(bsddb3.db.DB_DUP) #declare duplicates allowed before you create the database
    database.open(DB_File,None, bsddb3.db.DB_HASH, bsddb3.db.DB_CREATE)
    curs = database.cursor()

    for r in returnSet:
        result = curs.set(r.encode('utf-8'))
        if displayMode == FULL:
            print(str(result[1].decode('utf-8')))

        else:
            print(str(result[0].decode('utf-8')))

    curs.close()
    database.close()

def resetResults():
    global returnSet
    global displayMode
    returnSet=set()
    displayMode = SHORT


def main():
    global returnSet
    for line in sys.stdin:
        parseQuery(line.lower())
        displayResults()
        resetResults()



if __name__ == '__main__':
    main()
