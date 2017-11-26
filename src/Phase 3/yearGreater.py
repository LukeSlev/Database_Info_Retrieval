from bsddb3 import db

def yearSearch(Starting_Year):
    DB_File = "ye.idx"
    database = db.DB()
    database.set_flags(db.DB_DUP) #declare duplicates allowed before you create the database
    database.open(DB_File,None, db.DB_BTREE, db.DB_CREATE)
    curs = database.cursor()

    # while Starting_Year[0] == '0':
    #     Starting_Year = Starting_Year[1:]
    #     print('here', Starting_Year)

    middleSet = set()

    print(str(int(Starting_Year)+1))

    if (int(Starting_Year) < int(curs.first()[0].decode("utf-8"))): # too early
        result = curs.set_range(curs.first()[0])
    elif int(Starting_Year) < int(curs.last()[0].decode("utf-8")):  # Proper Range
        result = curs.set_range(str(int(Starting_Year)+1).encode("utf-8"))
    else:
        result = None  # too late

    print("LUKE: ",result)
    if(result != None):
        while(result != None):
            #print(result[1].decode('utf-8'))
            middleSet.add(result[1].decode('utf-8'))
            result = curs.next()
    else:
        print("No result was found")
        return ()

    curs.close()
    database.close()
    return middleSet


def main():
    print(yearSearch(2018))


if __name__ == "__main__":
    main()
