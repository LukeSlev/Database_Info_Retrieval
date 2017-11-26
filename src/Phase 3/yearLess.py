from bsddb3 import db



def yearSearch(Ending_Year):

    DB_File = "ye.idx"
    database = db.DB()
    database.set_flags(db.DB_DUP) #declare duplicates allowed before you create the database
    database.open(DB_File,None, db.DB_BTREE, db.DB_CREATE)
    curs = database.cursor()

    middleSet = set()
    result = curs.first()
    print('result', result)


    if(result != None):
          while(result != None):
            if(int(result[0].decode("utf-8")[0:4])>=(Ending_Year)):
                break

            middleSet.add(result[1])
            print("Name: " + str(result[0].decode("utf-8")) + ", Rest: " + str(result[1].decode("utf-8")))
            result = curs.next()

    else:
        print("No result was found")
        return ()

    curs.close()
    database.close()
    #return middleSet

def main():
    print(yearSearch(20))    
    print(yearSearch(2000))

if __name__ == "__main__":
    main()
