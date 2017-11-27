from bsddb3 import db

def termSearch(searchTerm):
    DB_File = "te.idx"
    database = db.DB()
    database.set_flags(db.DB_DUP) #declare duplicates allowed before you create the database
    database.open(DB_File,None, db.DB_BTREE, db.DB_CREATE)
    curs = database.cursor()
    resultSet = set()

    # print(searchTerm)

    result = curs.set(searchTerm.encode("utf-8"))
    #In the presence of duplicate key values, result will be set on the first data item for the given key.

    if(result != None):
        #print(str(result[0].decode("utf-8")),str(result[1].decode("utf-8")))
        resultSet.add(result[1].decode('utf-8'))


        #iterating through duplicates:
        dup = curs.next_dup()
        while(dup != None):
            #print(str(dup[0].decode("utf-8")),str(dup[1].decode("utf-8")))
            resultSet.add(dup[1].decode('utf-8'))
            dup = curs.next_dup()


    curs.close()
    database.close()
    return resultSet

def main():
    searchTerm = input("What do you want to search: ")
    ret = termSearch(searchTerm)
    for i in ret:
        print(i)


if __name__ == "__main__":
    main()
