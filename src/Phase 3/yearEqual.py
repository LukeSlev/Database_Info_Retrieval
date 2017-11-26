from bsddb3 import db

def yearSearch(Starting_Year):
    Starting_Year=int(Starting_Year)-1
    DB_File = "ye.idx"
    database = db.DB()
    database.set_flags(db.DB_DUP) #declare duplicates allowed before you create the database
    database.open(DB_File,None, db.DB_BTREE, db.DB_CREATE)
    curs = database.cursor()

    middleSet = set()

    #print(str(int(Starting_Year)))

    if int(Starting_Year) < int(curs.last()[0].decode("utf-8")):  # Proper Range
        result = curs.set_range(str(int(Starting_Year)+1).encode("utf-8"))
        if int(curs.next()[0].decode("utf-8"))>= int(Starting_Year+1):
             return middleSet
    else:
        result = None

    if(result != None):
        while(result != None):
            #print(result[1].decode('utf-8'))
            middleSet.add(result[1].decode('utf-8'))
            #print("Name: " + str(result[0].decode("utf-8")))
            result = curs.next()
    else:
        print("No result was found")
        return ()

    curs.close()
    database.close()
    return middleSet


def main():
    yearSearch(2017)


if __name__ == "__main__":
    main()
