from bsddb3 import db

def yearSearch(year):
    DB_File = "ye.idx"
    database = db.DB()
    database.set_flags(db.DB_DUP) #declare duplicates allowed before you create the database
    database.open(DB_File,None, db.DB_BTREE, db.DB_CREATE)
    curs = database.cursor()
    Starting_Year = int(year)
    Ending_Year = int(year) + 1

    middleSet = set()
    #get the record that has the smallest key greater than or equal to the Starting Name:
    result = curs.set_range(str(Starting_Year).encode("utf-8"))

    if(result != None):

        while(result != None):
            #Checking the end condition: If the student's name comes after(or equal to) Ending_Name
            if(str(result[0].decode("utf-8")[0:len(str(Ending_Year))])>=str(Ending_Year)):
                break

         #   print("Year: " + str(result[0].decode("utf-8")) + ", Rest: " + str(result[1].decode("utf-8")))
            middleSet.add(str(result[1].decode("utf-8")))
            result = curs.next()
    else:
        print("No result was found")
        return ()

    if len(middleSet)==0:
        print("No result was found")

    return middleSet




def main():
    print(yearSearch(1977))


if __name__ == "__main__":
    main()
